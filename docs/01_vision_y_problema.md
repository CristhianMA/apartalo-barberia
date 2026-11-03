# 1. Visión y problema correcto

> Ejercicio 1 · Temas 1, 2 y 5 · 🎩 PO La visión va en el `README.md`. Aquí van los puntos 2 a 6.

## 1.2 ¿Por qué no cascada?

| Causa de falla de cascada | Cómo se vería en mi proyecto |
|---|---|
| Requisitos congelados al inicio | Asumir que Don Rogelio conoce de antemano el impacto de las penalizaciones de cancelación y no poder ajustar los porcentajes ante el descontento de los clientes. |
| Integración tardía y pruebas al final | Programar toda la agenda y pasarelas de pago durante meses para descubrir al final que la regla de cálculo de combos genera descuadres en caja. |
| Retorno de inversión retrasado | Don Rogelio no vería ningún beneficio operativo hasta entregar el sistema completo meses después, en lugar de automatizar su cálculo de citas en 2 semanas. |

¿Usaría prototipos? ¿En qué momento y para qué?  
Sí, utilizaría wireframes y prototipos interactivos de baja fidelidad en el Sprint 0 y al inicio del Sprint 1 para validar con Don Rogelio y sus clientes el flujo de reserva de 3 clics y la visibilidad de los precios antes de implementar la interfaz final.

## 1.3 El manifiesto en mi proyecto

| Valor o principio | Decisión concreta en mi proyecto |
|---|---|
| **Valor:** Individuos e interacciones sobre procesos y herramientas | Conversar directamente con Don Rogelio para entender la dinámica de sus 3 sillas antes de imponer un flujo rígido en el software. |
| **Valor:** Software funcionando sobre documentación extensiva | Priorizar que la función de cotizaciones y cancelaciones pase sus pruebas automatizadas en `reglas.py` antes que escribir manuales exhaustivos. |
| **Principio:** Entregar software funcional frecuentemente | Entregar al término de las dos semanas del Sprint 1 el núcleo matemático validado con `pytest` para uso en la barbería. |
| **Principio:** Aceptamos requisitos cambiantes | Permitir ajustar las ventanas de tiempo de cancelación (24h y 2h) según el comportamiento real de los clientes de los sábados. |

## 1.4 Frameworks

| Framework | Lo que tomo de él |
|---|---|
| Scrum | Timebox de 2 semanas, roles definidos (PO, SM, Dev), ceremonias (Planning, Daily, Review, Retro) y Sprint Backlog. |
| Kanban | Visualización con tablero de 7 columnas, políticas explícitas de paso y límites estrictos de trabajo en progreso (WIP). |
| XP | Desarrollo Guiado por Pruebas (TDD), refactorización continua, estándares de código y diseño simple sin código innecesario. |

La combinación de Scrum y Kanban se llama: **Scrumban**

## 1.5 Requisito o solución

| # | Lo que dijo mi cliente | ¿Requisito o solución? | Si es solución: el requisito que hay detrás |
|---|---|---|---|
| 1 | "Quiero una base de datos Oracle con réplica en la nube para guardar las citas." | Solución | Alta disponibilidad y respaldo seguro del historial de reservaciones. |
| 2 | "Los clientes no deben poder apartar más de una cita por día para que no acaparen turnos." | Requisito | — |
| 3 | "Pongan un botón flotante color azul con animación para cancelar." | Solución | Mecanismo visible, accesible e intuitivo para solicitar cancelaciones. |
| 4 | "Si alguien cancela con menos de 2 horas o no viene, hay que cobrarle el 100%." | Requisito | — |
| 5 | "Necesito un lector de huellas digitales en la entrada para registrar a los barberos." | Solución | Control confiable de asistencia y asignación de barberos a sus sillas. |

## 1.6 Incertidumbre

- **Incertidumbre del qué:** Baja, porque las reglas de precios base, combos y ventanas de cancelación fueron claramente delimitadas por Don Rogelio.
- **Incertidumbre del cómo:** Media, debido a la integración de fechas/horas y validaciones de borde en Python sin un framework web completo todavía.
- **Zona del diagrama:** Zona Complicada (requiere análisis técnico pero no experimentación a ciegas).
- **Qué haré en este sprint para bajar la incertidumbre del qué:** Escribir pruebas de aceptación automatizadas en `pytest` basadas en los escenarios BDD acordados con el cliente antes de programar la lógica definitiva.
