# Nox YouTube Intelligence Toolkit

Convierte videos de YouTube en información accionable: **descarga**, **transcripción** y **resumen** en un flujo local y reproducible.

## ¿Qué hace este proyecto?
Este proyecto está pensado para creadores, analistas y equipos que necesitan procesar contenido largo de YouTube sin hacerlo manualmente.

Con este toolkit puedes:
- Descargar video completo (video + audio)
- Extraer solo audio en MP3
- Obtener transcripción (cuando aplique)
- Generar resumen estructurado por API local

## Casos de uso
- Analizar entrevistas largas en minutos
- Resumir contenido para newsletters o research
- Crear base de conocimiento desde videos
- Preparar material para guiones, clases o reportes

## Módulos
- `youtube_summary/` → API local de resumen + transcripción
- `docs/` → instalación y guía de uso
- `config/` → plantillas de configuración sin secretos
- `scripts/` → automatizaciones auxiliares

## Resultado esperado
Entrada: URL de YouTube  
Salida: archivo descargado (video/audio) + transcripción + resumen útil.

## Inicio rápido
1. Clona el repositorio.
2. Sigue `docs/SETUP.md`.
3. Ejecuta el servicio de `youtube_summary`.
4. Envía una URL y recibe resumen.

## Seguridad
Este repositorio público está sanitizado:
- sin contraseñas
- sin tokens
- sin cookies
- sin credenciales privadas

---

**Autor:** Nox
