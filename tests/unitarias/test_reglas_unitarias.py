"""
Pruebas unitarias para las reglas de negocio R1 y R2.
"""

import pytest
from apartalo.reglas import (
    calcular_costo_cita,
    calcular_penalizacion_cancelacion,
)


def test_costo_individual_corte():
    """Valida tarifa base de corte."""
    assert calcular_costo_cita(["corte"]) == 180.0


def test_costo_individual_barba():
    """Valida tarifa base de barba."""
    assert calcular_costo_cita(["barba"]) == 120.0


def test_descuento_combo_corte_barba():
    """Valida 15% de descuento por corte y barba juntos ($300 -> $255)."""
    assert calcular_costo_cita(["corte", "barba"]) == 255.0


@pytest.mark.parametrize(
    "visitas, esperado",
    [
        (0, 180.0),
        (4, 180.0),
        (5, 160.0),
        (7, 160.0),
    ],
)
def test_descuento_cliente_frecuente_limites(visitas, esperado):
    """Valida bonificación de $20 a partir de 5 visitas mensuales."""
    assert calcular_costo_cita(["corte"], visitas_mes=visitas) == esperado


def test_combo_con_cliente_frecuente():
    """Valida combo ($255) menos cliente frecuente ($20) = $235."""
    assert calcular_costo_cita(["corte", "barba"], visitas_mes=5) == 235.0


def test_excepciones_costo_cita():
    """Valida que entradas no válidas lancen ValueError."""
    with pytest.raises(ValueError):
        calcular_costo_cita([])

    with pytest.raises(ValueError):
        calcular_costo_cita(["tinte"])

    with pytest.raises(ValueError):
        calcular_costo_cita(["corte"], visitas_mes=-1)


def test_penalizacion_cancelacion_excepciones():
    """Valida excepciones por montos u horas negativas."""
    with pytest.raises(ValueError):
        calcular_penalizacion_cancelacion(costo_servicio=-100.0, horas_anticipacion=5.0)

    with pytest.raises(ValueError):
        calcular_penalizacion_cancelacion(costo_servicio=180.0, horas_anticipacion=-1.0)
