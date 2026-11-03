# 7. Requisitos no funcionales
> Ejercicio 7 · Tema 9 · 🎩 PO y 🎩 desarrollador Cada restricción va como **issue** (formulario "Requisito no funcional"). Aquí va el resumen.

| Issue | Restricción SMART | Externa / interna | Cualidad | Historia (T) | Prueba práctica (Tabla 2) o práctica (Tabla 4) |
|---|---|---|---|---|---|
| #16 | Tiempo de ejecución medio de cotización $\le 5$ ms en una muestra de 1,000 ejecuciones consecutivas. | Interna | Rendimiento (Comportamiento temporal) | #3, #4, #5 | Prueba automatizada con `pytest` y `time.perf_counter()`. |
| #17 | 100% de entradas inválidas (valores negativos o servicios inexistentes) disparan excepciones `ValueError`. | Interna | Seguridad (Integridad y tolerancia a fallos) | #3, #6, #7, #8 | Prueba de inyección de valores frontera negativos en `pytest`. |
| #18 | Cobertura de ramas y líneas $\ge 90\%$ en `src/apartalo/reglas.py` sin dependencias externas pesadas. | Interna | Mantenibilidad (Capacidad para ser probado) | #3, #4, #5, #6, #7, #8 | Medición de cobertura con `pytest-cov`. |

## 7.3 La que compruebo con código

- **Restricción:** #16
- **Prueba:** `tests/rnf/test_rnf.py`

## 7.4 Una por sprint

- **La que agrego a mi DoD en el Sprint 1:**  
  La restricción **#16** (Rendimiento del cálculo $\le 5$ ms) y la **#17** (Validación defensiva con `ValueError`). Ambas se integran como criterio de no regresión antes de dar una historia por terminada.
- **Las que dejo para después y por qué:**  
  La restricción **#18** (Cobertura completa con suite de integración continua en GitHub Actions) y los requisitos no funcionales de concurrencia de base de datos para la regla R3 se programan para el Sprint 2, ya que en el Sprint 1 el enfoque estuvo centrado exclusivamente en la lógica de negocio pura de cotizaciones y cancelaciones (R1 y R2).
