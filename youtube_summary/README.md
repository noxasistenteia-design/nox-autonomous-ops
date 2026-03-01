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

Si un video requiere sesión, pasa `cookies_file` con cookies exportadas.
