# YouTube Summary API (local)

API local para:
1) intentar descargar **video** con `yt-dlp`
2) si falla, intentar **audio**
3) transcribir con `faster-whisper`
4) devolver resumen básico

## Ejecutar

```bash
cd /home/nox/.openclaw/workspace/youtube_summary
python3 service.py
```

Queda en: `http://127.0.0.1:8091`

## Probar

```bash
curl -s http://127.0.0.1:8091/health

curl -s -X POST http://127.0.0.1:8091/summarize \
  -H 'content-type: application/json' \
  -d '{
    "url":"https://youtu.be/nJzd1MyVS24?si=VU3lHre5rR6dFD4Q",
    "language":"es",
    "model_size":"small"
  }' | jq
```

Si YouTube pide sesión, puedes pasar cookies exportadas:

```bash
curl -s -X POST http://127.0.0.1:8091/summarize \
  -H 'content-type: application/json' \
  -d '{
    "url":"https://youtu.be/nJzd1MyVS24?si=VU3lHre5rR6dFD4Q",
    "language":"es",
    "model_size":"small",
    "cookies_file":"/ruta/cookies.txt"
  }' | jq
```


> Nota: si YouTube bloquea la descarga en este entorno, la API devolverá errores de descarga.
