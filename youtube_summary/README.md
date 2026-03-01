# YouTube Summary API (local)

API local para:
1) descargar video o audio con `yt-dlp`
2) transcribir con `faster-whisper`
3) devolver resumen estructurado

## Ejecutar

```bash
cd ./youtube_summary
python3 service.py
```

Disponible en: `http://127.0.0.1:8091`

## Probar

```bash
curl -s http://127.0.0.1:8091/health

curl -s -X POST http://127.0.0.1:8091/summarize \
  -H 'content-type: application/json' \
  -d '{
    "url":"https://youtu.be/nJzd1MyVS24",
    "language":"es",
    "model_size":"small"
  }' | jq
```

## Cuando YouTube bloquea (usar cookies)

Si YouTube pide inicio de sesión o muestra bloqueo anti-bot, usa `cookies_file`.

### 1) Exportar cookies desde el navegador
1. Inicia sesión en YouTube en tu navegador.
2. Instala la extensión **Get cookies.txt LOCALLY**.
3. En `https://www.youtube.com`, exporta cookies.
4. Guarda el archivo como, por ejemplo:
   - `/home/USUARIO/Descargas/www.youtube.com_cookies.txt`

### 2) Probar con cookies en la API

```bash
curl -s -X POST http://127.0.0.1:8091/summarize \
  -H 'content-type: application/json' \
  -d '{
    "url":"https://youtu.be/ID_DEL_VIDEO",
    "language":"es",
    "model_size":"small",
    "cookies_file":"/home/USUARIO/Descargas/www.youtube.com_cookies.txt"
  }' | jq
```

## Descarga directa (sin API)

### Video + audio
```bash
yt-dlp \
  --cookies /home/USUARIO/Descargas/www.youtube.com_cookies.txt \
  --js-runtimes node \
  --impersonate chrome \
  -f "bestvideo+bestaudio/best" \
  -o "%(title)s.%(ext)s" \
  "https://youtu.be/ID_DEL_VIDEO"
```

### Solo audio (mp3)
```bash
yt-dlp \
  --cookies /home/USUARIO/Descargas/www.youtube.com_cookies.txt \
  --js-runtimes node \
  --impersonate chrome \
  -x --audio-format mp3 \
  -o "%(title)s.%(ext)s" \
  "https://youtu.be/ID_DEL_VIDEO"
```
