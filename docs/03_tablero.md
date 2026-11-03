# 3. El tablero kanban

> Ejercicio 3 · Tema 3 · 🎩 SM

## 3.2 Límites WIP

| Columna | Límite | Por qué ese número |
|---|---|---|
| Aceptación | 2 | Permite refinar la historia activa y preparar la siguiente sin saturar el análisis previo al desarrollo. |
| Desarrollo | 1 | Al ser un equipo de un solo desarrollador, enfoca el esfuerzo en una única historia a la vez evitando el multitasking. |
| Pruebas | 1 | Asegura que la verificación y las pruebas automatizadas se concluyan antes de pasar a un nuevo ítem. |

## 3.3 Políticas explícitas

| Para pasar a... | La tarjeta debe cumplir... |
|---|---|
| Aceptación | Estar priorizada en el Sprint Backlog con sus criterios INVEST definidos y rol claro. |
| Desarrollo | Tener criterios de aceptación redactados en formato BDD (Dado / Cuando / Entonces) aprobados por el PO. |
| Desarrollo listo | Tener el código de producción escrito, pasando localmente las pruebas unitarias básicas. |
| Pruebas | Estar lista para integrarse a la suite de pruebas automatizadas en `tests/` y revisión de cobertura. |
| Pruebas listo | Haber pasado el 100% de las pruebas automatizadas de aceptación con pytest sin fallos ni regresiones. |
| Liberación | Cumplir con la Definición de Terminado (DoD), documentación actualizada y commit en rama principal. |

## 3.4 Las seis prácticas de kanban en mi tablero

| Práctica | Cómo la aplico (o por qué todavía no aplica) |
|---|---|
| 1. Visualizar el trabajo | Mediante el tablero de 7 columnas en GitHub Projects con etiquetas MoSCoW, puntos y sprint visibles en cada tarjeta. |
| 2. Limitar el WIP | Configurando límites estrictos (WIP: 2 en Aceptación, WIP: 1 en Desarrollo y Pruebas) para evitar cuellos de botella. |
| 3. Administrar el flujo | Utilizando columnas intermedias búfer (*Desarrollo listo* y *Pruebas listo*) para suavizar transiciones y medir tiempos. |
| 4. Hacer explícitas las políticas | Definiendo reglas públicas y obligatorias para que una tarjeta cambie de estado en el tablero. |
| 5. Implementar ciclos de retroalimentación | A través de reuniones diarias (Daily Scrum) y revisiones al término del sprint con Don Rogelio. |
| 6. Mejora colaborativa y evolución experimental | Evaluando métricas empíricas de Cycle Time y Lead Time en la retrospectiva para refinar estimaciones en el Sprint 2. |
