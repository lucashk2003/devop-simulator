# DevOps CI/CD Simulator  
**v0.1.1-pre** – Simulador de Pipeline Ágil con Monte Carlo

![Flask](https://img.shields.io/badge/Flask-3.0.3-000000?style=for-the-badge&logo=flask&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## Descripción

**Simulador educativo** de un pipeline DevOps CI/CD en un entorno ágil. Permite configurar equipos, automatización, probabilidad de bugs y sprints, luego ejecuta una simulación **Monte Carlo** para modelar el flujo real de tareas.

Ideal para:
- Entender el impacto de la **automatización** en lead time y despliegues.
- Analizar cómo el **tamaño del equipo** y los **bugs** afectan el rendimiento.
- Experimentar con **métricas reales**: lead time, defectos, éxito de deploy.

> **No es un producto final**, es una **herramienta didáctica** para cátedras de DevOps, Simulación y Gestión Ágil.

---

## Características

| Funcionalidad | Descripción |
|---------------|-----------|
| **Configuración flexible** | Desarrolladores, testers, duración de sprints, % de automatización, bugs |
| **Simulación Monte Carlo** | Tiempos variables, bugs aleatorios, éxito de deploy probabilístico |
| **Persistencia** | Resultados guardados en SQLite (`data/devops_simulator.db`) |
| **Gráficos interactivos** | Lead Time, Defectos y Despliegues por sprint (Chart.js) |
| **Historial completo** | Compara múltiples corridas |
| **UI responsive** | Bootstrap 5 + diseño limpio |

---

## Capturas de Pantalla

<div align="center">
  <img src="https://i.imgur.com/placeholder.png" alt="Dashboard Principal" width="48%" />
  <img src="https://i.imgur.com/placeholder.png" alt="Resultados con Gráficos" width="48%" />
</div>

> *(Las imágenes se pueden agregar luego con capturas reales)*

---

## Requisitos

- Python 3.11+
- `pip` (gestor de paquetes)

---

## Instalación Rápida

```bash
# 1. Clonar el repositorio
git clone https://github.com/tu-usuario/devops-simulator.git
cd devops-simulator

# 2. Crear entorno virtual (recomendado)
python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar
python app.py