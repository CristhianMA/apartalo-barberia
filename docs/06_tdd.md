# 6. Pruebas de aceptación y TDD
> Ejercicio 6 · Tema 8 · 🎩 desarrollador

## 6.2 Mis ciclos de TDD

| Ciclo | Commit ROJO | Commit VERDE | Commit REFACTOR (si hubo) | Qué aprendí |
|---|---|---|---|---|
| 1 | `test(r1): prueba tarifa base individual corte/barba falla` | `feat(r1): retorna precios base corte 180 y barba 120` | `refactor(r1): extraer constantes PRECIO_CORTE y PRECIO_BARBA` | Escribir primero el assert define claramente la firma de la función antes de codificar la lógica. |
| 2 | `test(r1): prueba combo 15% descuento corte+barba falla` | `feat(r1): aplica factor 0.85 al detectar combo corte y barba` | `refactor(r1): normalizar servicios con strip y lower` | Prever entradas con espacios o mayúsculas accidentales evita roturas en producción. |
| 3 | `test(r2): prueba cobro 50% en cancelacion intermedia falla` | `feat(r2): rama condicional para rango 2h a 24h` | `refactor(r2): agregar guardas defensivas ValueError para negativos` | Las pruebas de límites en rangos temporales (2.0h y 23.9h) blindan la política de cancelación ante reclamos. |

## 6.6 Cobertura de caminos

- **Función:** `calcular_costo_cita` y `calcular_penalizacion_cancelacion`
- **Caminos (cada `return` y cada `raise`):**
  1. `raise ValueError("Debe seleccionar al menos un servicio.")` (servicios vacíos).
  2. `raise ValueError("El número de visitas mensuales no puede ser negativo.")` (visitas < 0).
  3. `raise ValueError(f"Servicio no reconocido...")` (servicio inválido).
  4. `return round(float(total), 2)` para solo corte ($180).
  5. `return round(float(total), 2)` para solo barba ($120).
  6. `return round(float(total), 2)` para combo corte + barba ($255).
  7. `return round(float(total), 2)` para cliente frecuente con >=5 visitas ($180 - $20).
  8. `return round(float(total), 2)` para combo + cliente frecuente ($235).
  9. `raise ValueError("El costo del servicio no puede ser negativo.")` (costo < 0).
  10. `raise ValueError("Las horas de anticipación no pueden ser un valor negativo.")` (horas < 0).
  11. `return round(float(cargo), 2)` con 0% de penalización (horas >= 24).
  12. `return round(float(cargo), 2)` con 50% de penalización (2 <= horas < 24).
  13. `return round(float(cargo), 2)` con 100% de penalización (horas < 2 o no_show=True).
- **Caminos que recorren mis pruebas:** Todos los 13 caminos son ejecutados por la suite de pruebas unitarias y de aceptación (`test_reglas_unitarias.py` y `test_reglas_aceptacion.py`).
- **Cobertura:** 100% de cobertura de líneas y ramas en `src/apartalo/reglas.py`.
- **Pruebas que agregué para completar:** Pruebas de bordes en horas de cancelación (`horas_anticipacion=2.0` y `horas_anticipacion=23.9`), prueba de valor límite en visitas (`visitas=4` vs `visitas=5`), y pruebas de excepciones explícitas con `pytest.raises(ValueError)`.

## 6.7 Regresión

- **Defecto (encontrado o provocado):** Al aplicar el descuento de $20 de cliente frecuente en servicios menores o promociones acumuladas, el subtotal podía resultar en montos negativos si se ingresaba un descuento mayor al costo base.
- **Prueba que lo detecta:** `test_descuento_cliente_frecuente_limites` y `test_combo_con_cliente_frecuente`.
- **Qué pasaba y cómo lo corregí:** No existía una guarda que limitara el piso del importe a pagar; se corrigió introduciendo la protección `total = max(0.0, subtotal)` antes del redondeo y retorno del valor.
