"""
Pruebas de aceptación automatizadas para las historias de Sprint 1 (R1 y R2).
"""

import pytest
from apartalo.reglas import (
    calcular_costo_cita,
    calcular_penalizacion_cancelacion,
)


@pytest.mark.aceptacion
def test_hu3_calculo_costos_individuales():
    """Criterio de aceptación HU #3: Corte $180 y Barba $120."""
    assert calcular_costo_cita(["corte"]) == 180.0
    assert calcular_costo_cita(["barba"]) == 120.0


@pytest.mark.aceptacion
def test_hu4_calculo_descuento_combo():
    """Criterio de aceptación HU #4: Combo corte + barba con 15% de descuento."""
    costo = calcular_costo_cita(["corte", "barba"])
    assert costo == 255.0


@pytest.mark.aceptacion
def test_hu5_descuento_cliente_frecuente():
    """Criterio de aceptación HU #5: Bono de $20 a partir de 5 visitas."""
    assert calcular_costo_cita(["corte"], visitas_mes=4) == 180.0
    assert calcular_costo_cita(["corte"], visitas_mes=5) == 160.0


@pytest.mark.aceptacion
def test_hu6_cancelacion_anticipada_sin_penalizacion():
    """Criterio de aceptación HU #6: Cancelación con >= 24h genera cargo de $0.00."""
    cargo = calcular_penalizacion_cancelacion(costo_servicio=255.0, horas_anticipacion=24.0)
    assert cargo == 0.0


@pytest.mark.aceptacion
@pytest.mark.parametrize("horas", [2.0, 10.0, 23.9])
def test_hu7_cancelacion_intermedia_cincuenta_porciento(horas):
    """Criterio de aceptación HU #7: Cancelación entre 2h y 24h cobra el 50%."""
    cargo = calcular_penalizacion_cancelacion(costo_servicio=200.0, horas_anticipacion=horas)
    assert cargo == 100.0


@pytest.mark.aceptacion
def test_hu8_cancelacion_tardia_o_noshow():
    """Criterio de aceptación HU #8: Cancelación < 2h o No Show cobra el 100%."""
    assert calcular_penalizacion_cancelacion(costo_servicio=180.0, horas_anticipacion=1.5) == 180.0
    assert calcular_penalizacion_cancelacion(costo_servicio=180.0, horas_anticipacion=5.0, no_show=True) == 180.0
