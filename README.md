# Nox OpenClaw Ops

Proyecto profesionalizado para operación autónoma de OpenClaw.

## Objetivo
Estandarizar el entorno de trabajo de Nox para automatización local, continuidad multicanal y despliegue reproducible.

## Estructura
- `docs/`: arquitectura, operación y seguridad
- `config/`: ejemplos de configuración (sin secretos)
- `scripts/`: utilidades de automatización
- `youtube_summary/`: pipeline de descarga/transcripción/resumen

## Seguridad
Este repositorio está sanitizado para publicación pública:
- Sin tokens
- Sin contraseñas
- Sin memoria privada
- Sin credenciales operativas

## Flujo recomendado
1. Clonar
2. Revisar `docs/SETUP.md`
3. Copiar `config/openclaw.example.json` a ruta real
4. Inyectar secretos por variables de entorno
