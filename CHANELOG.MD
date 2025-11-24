# Changelog

Todas las cambios notables del proyecto serán documentados en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/),  
y este proyecto adhieren a [Semantic Versioning](https://semver.org/lang/es/).

## [v0.1.1] - 2025-04-05 (pre-release)

### Fixed
- Arreglado error crítico en plantillas (`index.html` y `history.html`) al acceder a parámetros de simulación usando notación de punto (`.num_developers`) cuando `params` es un diccionario → `jinja2.exceptions.UndefinedError`.
- Corregida función `get_simulations()` en `database.py`: ahora convierte correctamente el campo `params` de JSON string a diccionario real antes de devolverlo.
- Solucionado bloqueo permanente del archivo `devops_simulator.db` en Windows al usar Flask con `debug=True` + reloader:
  - Se desactiva el reloader (`use_reloader=False`) en desarrollo local.
- Actualizadas todas las referencias a `sim.params` en plantillas para usar notación de diccionario segura (`sim.params['clave']`).
- Asegurada consistencia en el acceso a valores numéricos con filtro `|float` en sliders (automatización y bugs).

### Changed
- Mejora en robustez del acceso a parámetros en Jinja2 (más resistente a cambios futuros).
- Comentarios internos aclarando el motivo del `use_reloader=False` (evita doble inicialización y bloqueo de SQLite en Windows).

## [v0.1.0] - 2025-04-04 (pre-release)

### Added
- Versión inicial funcional del Simulador DevOps CI/CD.
- Formulario de configuración con sliders y parámetros realistas.
- Simulación Monte Carlo completa con cálculo de Lead Time, tasa de defectos y éxito de despliegues.
- Persistencia en SQLite (`data/devops_simulator.db`) con almacenamiento de params y results en JSON.
- Dashboard de resultados con gráficos interactivos (Chart.js): Lead Time, Defectos y Despliegues por sprint.
- Historial de simulaciones y lista de últimas ejecuciones.
- Estructura MVC limpia con Flask + Jinja2 + Bootstrap.

**¡Primera versión completamente operativa!**

---

**Estado actual del proyecto**: `v0.1.1-pre` → funcional, estable y sin errores críticos conocidos.