# Setup

## Requisitos
- Linux x64
- Node.js 22+
- Python 3.12+
- ffmpeg

## Instalación rápida
```bash
# Dependencias de Python
autopep8 --version >/dev/null 2>&1 || true
python3 -m pip install --user -U "yt-dlp[default,curl-cffi]" --break-system-packages

# Herramientas del sistema
sudo apt-get update
sudo apt-get -y install ffmpeg
```

## YouTube pipeline
Ver `youtube_summary/README.md`.
