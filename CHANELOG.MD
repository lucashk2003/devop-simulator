# Changelog

Todas las cambios notables del proyecto serán documentados en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/),  
y este proyecto adhieren a [Semantic Versioning](https://semver.org/lang/es/).

## [v0.2.0] - 2025-04-06 (pre-release) — Monte Carlo Real

### Added
- **Múltiples corridas Monte Carlo** en una sola ejecución (1 → 20.000 corridas).
- Nuevo campo en el formulario: **Cantidad de corridas Monte Carlo**.
- Una ejecución en batch = **una sola fila en la DB** (historial limpio y escalable).
- Cálculo automático de estadísticas robustas:
  - Media ± desviación estándar
  - Percentil 95 del Lead Time
  - Mínimo / máximo
- Interfaz inteligente en resultados:
  - Si es 1 corrida → gráficos por sprint (como antes)
  - Si son >1 corridas → mensaje claro + métricas estadísticas (sin gráficos por sprint)
- Columna `batch_size` en la base de datos + migración automática.
- Límite seguro de 20.000 corridas por ejecución.
- Badge visual en historial y resultados indicando cantidad de corridas.

### Changed
- `results_summary` reemplaza al antiguo `results` (mejor estructura).
- `results.html` ahora detecta automáticamente si es batch o corrida simple.
- `history.html` muestra cantidad de corridas con badge.

### Fixed
- Compatibilidad total hacia atrás: simulaciones antiguas siguen funcionando.
- Evita errores en Jinja al intentar acceder a `sprint_data` en batches grandes.

> **¡Ahora sí es un simulador Monte Carlo de verdad!** Listo para análisis estadístico serio.

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