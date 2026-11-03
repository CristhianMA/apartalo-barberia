# Apártalo — Barbería Filo

Repositorio de la **Evidencia 1** de *Proyecto de ingeniería de software* (Tecmilenio, CRN 13241).

| Dato | |
|---|---|
| Estudiante | Maximus Cristian Hernandez Garcia |
| Matrícula | AL03007777 |
| Variante | 1 — Barbería Filo |
| Project (tablero) | [apartalo-barberia](https://github.com/users/CristhianMA/projects/1) |

## Visión del producto

Apártalo - Barbería Filo es una solución web de gestión y apartado de citas diseñada para Don Rogelio y los clientes de su barbería tradicional en la colonia Narvarte. La plataforma centraliza la agenda de sus 3 sillas, automatiza las tarifas y promociones por servicios combinados o clientes frecuentes, y mitiga las pérdidas financieras por inasistencias de los sábados mediante una política clara y automatizada de cancelaciones.

## Mi equipo Scrum (los tres sombreros)

| Sombrero | Lo que hago con él en este proyecto |
|---|---|
| 🎩 PO | Defino la visión, priorizo el backlog (MoSCoW) y valido los criterios de aceptación con Don Rogelio. |
| 🎩 SM | Configuro el tablero kanban, monitoreo límites WIP, facilito las ceremonias y resuelvo bloqueos. |
| 🎩 Desarrollador | Implemento la lógica en Python (reglas.py) bajo TDD y construyo la suite de pruebas en pytest. |

## Cómo está organizado este repositorio

| Carpeta o archivo | Qué contiene | Ejercicio |
|---|---|---|
| `docs/01_vision_y_problema.md` | Paradigmas, manifiesto, requisito vs. solución, incertidumbre | 1 |
| Issues `historia` y `epica` + `docs/02_backlog.md` | Product backlog, plantilla invertida, glosario, iceberg | 2 |
| `docs/03_tablero.md` | Columnas, límites WIP, políticas y prácticas de kanban | 3 |
| `docs/04_refinamiento.md` + `features/` | Grooming, carga máxima, división, escenarios BDD, tabla FIT | 4 |
| `docs/05_sprint1.md` | Planeación, bitácora, revisión y retrospectiva | 5 |
| `src/apartalo/` + `tests/` + `docs/06_tdd.md` | Código, pruebas y ciclos de TDD | 6 |
| Issues `rnf` + `docs/07_rnf.md` | Requisitos no funcionales | 7 |
| `metricas/` + `docs/08_metricas.md` | Fotografía del tablero y consultas SQL | 8 |
| `ENTREGA.md` | Enlaces a cada evidencia | Entrega |

## Cómo correr las pruebas

```bash
python -m venv .venv
source .venv/bin/activate       # En Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest                          # todas las pruebas
pytest -m aceptacion            # solo la suite de aceptación
pytest -m unitaria              # solo las unitarias
pytest -m rnf                   # solo las de requisitos no funcionales
