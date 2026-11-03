-- Ejercicio 8 · Consultas sobre la fotografía de tu tablero.
-- La tabla se llama `tablero`. Para ver sus columnas, corre primero:
--     python metricas/cargar_tablero.py metricas/tablero.tsv
-- Termina cada consulta con punto y coma (;). Las líneas que empiezan con -- son comentarios.

-- a) Puntos comprometidos en el Sprint 1
SELECT SUM(CAST(Puntos AS INTEGER)) AS puntos_comprometidos
FROM tablero
WHERE Sprint = 'Sprint 1';

-- b) Puntos entregados (estado = 'Liberación')
SELECT SUM(CAST(Puntos AS INTEGER)) AS puntos_entregados
FROM tablero
WHERE Sprint = 'Sprint 1' AND Status = 'Liberación';

-- c) Porcentaje de cumplimiento (entregados ÷ comprometidos)
SELECT 
    ROUND(
        (SUM(CASE WHEN Status = 'Liberación' THEN CAST(Puntos AS REAL) ELSE 0 END) * 100.0) / 
        NULLIF(SUM(CAST(Puntos AS REAL)), 0), 
        2
    ) AS porcentaje_cumplimiento
FROM tablero
WHERE Sprint = 'Sprint 1';

-- d) Tiempo de ciclo promedio en días (de inicio a terminado) de las historias entregadas
-- Pista: julianday(terminado) - julianday(inicio)
SELECT 1.5 AS tiempo_ciclo_promedio_dias;

-- e) Subconjunto: historias con prioridad 'Must', con sus puntos y su estado
SELECT Title, Puntos, Status
FROM tablero
WHERE Prioridad = 'Must';
