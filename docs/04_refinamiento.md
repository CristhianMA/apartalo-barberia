# 4. Refinamiento y escenarios

> Ejercicio 4 · Tema 7 · 🎩 PO y 🎩 desarrollador Los escenarios BDD van en la carpeta `features/`.

## 4.1 Pesar (MoSCoW)

Criterio que usé:  
Se clasificó como **Must** todo lo indispensable para la operación básica y el cálculo monetario (R1 y R2). Como **Should**, las restricciones de capacidad física de 3 sillas (R3) y usabilidad. Como **Could**, herramientas de apoyo logístico y supervisión diaria. Como **Won't**, dependencias externas complejas como pasarelas bancarias.

## 4.2 Ilustrar

Historia: #9 (HU: Botón accesible de RESERVAR en la interfaz principal)  
Boceto: `![boceto](img/boceto_reservar.png)`  
*(En la interfaz principal de móvil y escritorio destaca un botón centralizado con llamada a la acción "RESERVAR AHORA" que dirige al selector de servicio y fecha).*

## 4.3 Medir

Escala de puntos: 1, 2, 3, 5, 8, 13, 21.

## 4.4 Dividir

- **Velocidades de referencia de mi variante:** 16 puntos por sprint (2 semanas).
- **Operación:** $\text{Carga máxima por historia} = 16 \times 0.35 = 5.6 \text{ puntos}$.
- **Carga máxima por historia:** 5 puntos (ninguna historia debe superar 5 puntos para entrar al sprint).
- **Historias que rebasan la carga máxima:** Ninguna de las historias seleccionadas para el Sprint 1 rebasó este umbral (máximo 3 puntos). En el backlog general, la historia de citas simultáneas fue calibrada en 5 puntos.

| Historia original | Puntos | Subhistorias (issues) | Puntos de cada una | ¿Cómo la partí? |
|---|---|---|---|---|
| Épica: Gestión Integral de Políticas de Citas | 8 | #9 (Restringir 3 citas simultáneas), #10 (Limitar 1 cita por cliente) | 5, 3 | Se separó por regla física de capacidad de local (R3.1) vs. regla de equidad por cliente (R3.2). |

## 4.6 R2 como tabla FIT

Escríbela antes de programar. Al terminar el Ejercicio 6, agrega la columna "Resultado real" y marca cada fila:  si pasó,  si falló (con el valor esperado y el real).

| (costo_servicio) | (horas_anticipacion) | Resultado esperado | Resultado real |
|:---:|:---:|:---:|:---:|
| 255.00 | 24.0 | 0.00 | ✅ 0.00 |
| 180.00 | 48.0 | 0.00 | ✅ 0.00 |
| 200.00 | 12.0 | 100.00 | ✅ 100.00 |
| 255.00 | 2.0 | 127.50 | ✅ 127.50 |
| 180.00 | 1.5 | 180.00 | ✅ 180.00 |
| 300.00 | 0.0 (o no_show) | 300.00 | ✅ 300.00 |
