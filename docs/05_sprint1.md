# 5. Sprint 1 (27 oct – 9 nov 2026)
> Ejercicio 5 · Temas 4 y 11

## A. Planeación del sprint
> 🎩 SM facilita · 🎩 PO presenta · 🎩 desarrollador se compromete

**Objetivo del sprint:**  
Implementar y verificar mediante pruebas automatizadas con pytest las reglas de negocio de cotización de servicios (R1) y de penalizaciones por cancelación (R2) para el MVP de la barbería.

**Capacidad en horas (Figura 2 del Tema 11):**

| Concepto | Horas |
|---|---|
| Horas disponibles en las dos semanas | 80 |
| − Otras actividades (clases, trabajo, tareas) | 32 |
| = Disponibilidad | 48 |
| ÷ 2 = **Capacidad** | **24** |

**Compromiso (historias del Sprint 1):**

| Historia | Puntos | Horas estimadas |
|---|---|---|
| #3 HU: Calcular costo individual de corte y barba | 2 | 3.0 |
| #4 HU: Aplicar 15% de descuento por combo corte y barba | 3 | 4.5 |
| #5 HU: Aplicar descuento de $20 a clientes frecuentes | 3 | 4.5 |
| #6 HU: Cancelar cita con 24 horas o más de anticipación sin penalización | 2 | 3.0 |
| #7 HU: Aplicar penalización del 50% por cancelación intermedia | 3 | 4.5 |
| #8 HU: Cobrar el 100% por cancelación con menos de 2 horas o inasistencia | 3 | 4.5 |
| **Total** | **16** | **24.0** |

**Definición de Terminado (DoD):**
1. El código cumple con las reglas de estilo PEP 8 y está documentado con docstrings en español.
2. Cada regla de negocio cuenta con sus pruebas automatizadas unitarias y de aceptación en pytest en estado verde (100% aprobadas).
3. La cobertura de pruebas sobre el módulo `src/apartalo/reglas.py` es superior al 90% sin advertencias ni fallos.
4. Los cambios cuentan con un commit descriptivo en GitHub y la tarjeta correspondiente se movió a la columna *Liberación*.

**DoD vs. criterios de aceptación (con un ejemplo de mi backlog):**  
Los criterios de aceptación son únicos para cada historia de usuario y validan la regla de negocio funcional específica desde la perspectiva del cliente (por ejemplo, para la **HU #4**, el criterio exige: *"Si el cliente elige corte y barba juntos, se descuenta el 15% ($45) dando un total de $255.00 MXN"*). Por el contrario, la **Definición de Terminado (DoD)** es un estándar de calidad técnico global que aplica a **todas** las historias por igual antes de considerarse entregadas (por ejemplo: *"Las pruebas pasan en verde, no hay deuda técnica y el commit está en la rama principal"*).

---

## B. Junta diaria — bitácora
> 🎩 desarrollador responde · 🎩 SM anota impedimentos

### 27 de octubre de 2026
- **¿Qué hice?** Configuración del entorno de pruebas con pytest y refinamiento de los criterios de aceptación de la HU #3 en la columna Aceptación.
- **¿Qué haré?** Mover la HU #3 a Desarrollo y diseñar las primeras pruebas unitarias para servicios base individuales.
- **¿Qué me lo impide?** Ningún impedimento el día de hoy.

### 29 de octubre de 2026
- **¿Qué hice?** Implementación de la función base en `reglas.py` y resolución del caso de corte ($180) y barba ($120).
- **¿Qué haré?** Pasar HU #3 a Pruebas, mover a Liberación y comenzar el refinamiento de la HU #4 (descuento combo).
- **¿Qué me lo impide?** Duda sobre cómo manejar servicios no válidos en la entrada de datos.

### 31 de octubre de 2026
- **¿Qué hice?** Completada la lógica de cálculo del 15% de descuento para la combinación corte y barba (HU #4) con sus pruebas unitarias.
- **¿Qué haré?** Mover HU #4 a Liberación y pasar HU #5 (clientes frecuentes) a Desarrollo.
- **¿Qué me lo impide?** Ninguno.

### 3 de noviembre de 2026
- **¿Qué hice?** Codificación de la regla de bonificación de $20 para clientes con 5 o más visitas mensuales (HU #5).
- **¿Qué haré?** Diseñar las pruebas de límites de borde (4 visitas vs 5 visitas) y liberar la historia.
- **¿Qué me lo impide?** Ninguno.

### 5 de noviembre de 2026
- **¿Qué hice?** Implementación de la lógica de cancelación con anticipación >= 24h sin cobro de penalización (HU #6).
- **¿Qué haré?** Mover HU #7 (penalización del 50%) a Desarrollo y codificar el rango de 2 a 24 horas.
- **¿Qué me lo impide?** El límite WIP de la columna Pruebas (límite: 1) requirió liberar HU #6 antes de avanzar la siguiente tarjeta.

### 7 de noviembre de 2026
- **¿Qué hice?** Implementadas y validadas las pruebas para cancelaciones con penalización del 50% (HU #7) y 100% por inasistencia o < 2h (HU #8).
- **¿Qué haré?** Ejecutar la suite completa de pruebas para verificar que no haya regresiones y preparar la sesión de revisión con Don Rogelio.
- **¿Qué me lo impide?** Ninguno.

**Impedimentos y qué hizo el SM:**

| Fecha | Impedimento | Qué hizo el SM |
|---|---|---|
| 29 oct 2026 | Duda en el manejo de excepciones cuando se reciben nombres de servicios no registrados o precios negativos. | El SM revisó los lineamientos y definió lanzar excepciones estándar `ValueError` con mensajes claros y descriptivos. |
| 5 nov 2026 | Bloqueo temporal en el flujo del tablero Kanban al alcanzarse el límite WIP = 1 en la columna Pruebas. | El SM facilitó la priorización de la verificación de la HU #6 para liberarla y abrir espacio para la HU #7 sin violar las políticas del tablero. |

---

## C. Revisión del sprint
> 🎩 PO revisa como si fuera mi cliente

| Historia | ¿Cumple sus criterios? | ¿Aceptada? | Evidencia |
|---|---|---|---|
| #3 HU: Calcular costo individual de corte y barba | Sí | Sí | Pruebas pytest en verde calculando $180 corte y $120 barba con validación de entradas. |
| #4 HU: Aplicar 15% de descuento por combo corte y barba | Sí | Sí | Pruebas aprobadas arrojando exactamente $255.00 MXN al elegir ambos servicios. |
| #5 HU: Aplicar descuento de $20 a clientes frecuentes | Sí | Sí | Validación de regla de negocio descontando $20 únicamente a partir de la quinta visita. |
| #6 HU: Cancelar cita con >=24h sin penalización | Sí | Sí | Pruebas unitarias confirmando cobro de $0.00 MXN al cancelar con más de 24 horas. |
| #7 HU: Aplicar penalización del 50% por cancelación intermedia | Sí | Sí | Cobro validado del 50% del total contratado al cancelar entre 2 y 24 horas. |
| #8 HU: Cobrar 100% por cancelación <2h o inasistencia | Sí | Sí | Cobro total validado ante cancelaciones de último momento o inasistencias (No Show). |

**Cambio que pediría mi cliente → historia nueva:** #14 (HU: Generar reporte de insumos requeridos para el día siguiente). Don Rogelio solicita anticipar toallas y material limpio según las citas del día posterior.

---

## D. Retrospectiva
> 🎩 SM facilita

**¿Qué salió bien?**
* La estimación de 16 puntos coincidió exactamente con la capacidad neta calculada de 24 horas.
* El enfoque de desarrollo guiado por pruebas (TDD) permitió blindar las fórmulas de dinero y descuentos sin errores en los cálculos.
* El respeto a los límites WIP en Kanban impidió acumular tareas a medias en la columna de Desarrollo.

**¿Qué hay que mejorar?**
* Mejorar la granularidad en la documentación de pruebas de borde temporales (manejo de horas y minutos).
* Automatizar la verificación de pruebas mediante un workflow de integración continua (CI) en GitHub Actions para no depender únicamente de ejecuciones manuales.

**Acciones para el Sprint 2:**
1. Configurar un pipeline de GitHub Actions que ejecute automáticamente `pytest` con cada Pull Request o push a la rama principal.
2. Iniciar el desarrollo de las historias de la regla R3 (límite de 3 citas simultáneas y 1 cita por cliente al día) en el siguiente Sprint Backlog.
