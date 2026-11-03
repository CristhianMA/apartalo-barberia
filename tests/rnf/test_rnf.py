"""
Pruebas automatizadas de Requisitos No Funcionales (RNF).
Valida rendimiento y tiempos de respuesta (ISO/IEC 25010).
"""

import time
import pytest
from apartalo.reglas import calcular_costo_cita


@pytest.mark.rnf
def test_rnf01_tiempo_respuesta_calculo_costo():
    """RNF-01: El cálculo de costo debe ejecutarse en menos de 5 ms promedio."""
    iteraciones = 1000
    inicio = time.perf_counter()

    for _ in range(iteraciones):
        calcular_costo_cita(["corte", "barba"], visitas_mes=5)

    fin = time.perf_counter()
    tiempo_total_ms = (fin - inicio) * 1000.0
    tiempo_promedio_ms = tiempo_total_ms / iteraciones

    assert tiempo_promedio_ms < 5.0, (
        f"El tiempo promedio ({tiempo_promedio_ms:.3f} ms) excedió el límite de 5 ms."
    )
