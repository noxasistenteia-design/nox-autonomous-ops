#!/usr/bin/env python3
import json
import re
import subprocess
import tempfile
from pathlib import Path
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="YouTube Summary API", version="1.0")


class RequestBody(BaseModel):
    url: str
    language: str = "es"
    model_size: str = "small"  # tiny/base/small/medium/large-v3
    cookies_file: Optional[str] = None  # ruta a cookies.txt exportado del navegador


def run(cmd: list[str], cwd: Optional[Path] = None) -> tuple[int, str, str]:
    p = subprocess.run(cmd, cwd=str(cwd) if cwd else None, capture_output=True, text=True)
    return p.returncode, p.stdout, p.stderr


def clean_text(text: str) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    return text


def basic_summary(text: str, max_points: int = 8) -> list[str]:
    # Resumen extractivo simple para no depender de una API externa.
    sents = re.split(r"(?<=[\.!?])\s+", text)
    sents = [s.strip() for s in sents if len(s.strip()) > 50]
    return sents[:max_points]


@app.get("/health")
def health():
    return {"ok": True}


@app.post("/summarize")
def summarize(body: RequestBody):
    url = body.url.strip()
    with tempfile.TemporaryDirectory(prefix="yt_summary_") as td:
        work = Path(td)
        outtmpl = str(work / "%(id)s.%(ext)s")

        # 1) Intentar video completo
        cookie_args = []
        if body.cookies_file:
            cookie_args = ["--cookies", body.cookies_file]

        video_cmd = [
            "yt-dlp",
            "--no-playlist",
            *cookie_args,
            "-f",
            "bestvideo+bestaudio/best",
            "-o",
            outtmpl,
            url,
        ]
        rc_v, so_v, se_v = run(video_cmd)

        downloaded = list(work.glob("*"))
        mode = "video" if rc_v == 0 and downloaded else "none"

        # 2) Si falla video, intentar audio
        if mode == "none":
            audio_cmd = [
                "yt-dlp",
                "--no-playlist",
                *cookie_args,
                "-x",
                "--audio-format",
                "mp3",
                "-o",
                outtmpl,
                url,
            ]
            rc_a, so_a, se_a = run(audio_cmd)
            downloaded = list(work.glob("*"))
            if rc_a == 0 and downloaded:
                mode = "audio"
            else:
                return {
                    "ok": False,
                    "error": "No fue posible descargar ni video ni audio.",
                    "video_error": se_v[-1200:],
                    "audio_error": se_a[-1200:],
                }

        # Seleccionar archivo más grande (normalmente media principal)
        media = max(downloaded, key=lambda p: p.stat().st_size)

        # 3) Transcribir con faster-whisper
        try:
            from faster_whisper import WhisperModel

            model = WhisperModel(body.model_size, device="cpu", compute_type="int8")
            segments, info = model.transcribe(str(media), language=body.language, vad_filter=True)
            chunks = []
            for seg in segments:
                t = seg.text.strip()
                if t:
                    chunks.append(t)
            transcript = clean_text(" ".join(chunks))
        except Exception as e:
            return {
                "ok": False,
                "error": f"Descarga lista ({mode}), pero falló transcripción: {e}",
                "media_file": str(media),
            }

        if not transcript:
            return {"ok": False, "error": "Transcripción vacía.", "mode": mode}

        points = basic_summary(transcript, max_points=8)

        return {
            "ok": True,
            "mode": mode,
            "media_file": media.name,
            "language": body.language,
            "transcript_chars": len(transcript),
            "resumen": points,
            "transcripcion_preview": transcript[:2000],
        }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("service:app", host="127.0.0.1", port=8091, reload=False)
