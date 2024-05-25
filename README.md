# Proyecto de Control de Acceso al Data Center

Este proyecto es un sistema de control de acceso para un data center, que permite el monitoreo en tiempo real del acceso de personal y visitantes a través de más de 60 puertas, utilizando tarjetas magnéticas. El sistema guarda toda la información de acceso en una base de datos para auditorías futuras y proporciona una vista en tiempo real del estatus de entrada y salida de cada oficina.

## Requisitos

- Python 3.8+
- Django 3.2+
- Django Channels
- Django REST Framework
- Channels Redis
- Django Simple JWT
- Arduino o Raspberry Pi
- Lectores RFID
- Relays para controlar cerraduras eléctricas

## Instalación

1. **Crear y Activar un Entorno Virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
