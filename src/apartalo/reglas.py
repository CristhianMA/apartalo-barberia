"""
Módulo de reglas de negocio para Apártalo — Barbería Filo.
Implementa las reglas R1 (Precios y descuentos) y R2 (Cancelaciones).
"""

from typing import List, Union

# Tarifas base fijas del negocio
PRECIO_CORTE: float = 180.0
PRECIO_BARBA: float = 120.0
DESCUENTO_COMBO: float = 0.15
DESCUENTO_FRECUENTE: float = 20.0


def calcular_costo_cita(servicios: List[str], visitas_mes: int = 0) -> float:
    """
    Calcula el costo total de una cita según la regla R1.

    Reglas:
    - Corte: $180.00 MXN
    - Barba: $120.00 MXN
    - Combo (Corte + Barba): 15% de descuento sobre el total combinado ($255.00 MXN base).
    - Cliente frecuente (>= 5 visitas en el mes): $20.00 MXN de descuento adicional.

    :param servicios: Lista con los nombres de los servicios ('corte', 'barba').
    :param visitas_mes: Cantidad de visitas previas completadas en el mes calendario.
    :return: Costo final a pagar en MXN (redondeado a 2 decimales).
    :raises ValueError: Si la lista de servicios está vacía, contiene servicios no válidos
                        o si visitas_mes es negativo.
    """
    if not servicios:
        raise ValueError("Debe seleccionar al menos un servicio.")

    if visitas_mes < 0:
        raise ValueError("El número de visitas mensuales no puede ser negativo.")

    # Normalizar nombres de servicios
    servicios_norm = [s.strip().lower() for s in servicios]
    servicios_permitidos = {"corte", "barba"}

    for s in servicios_norm:
        if s not in servicios_permitidos:
            raise ValueError(f"Servicio no reconocido: '{s}'. Opciones válidas: corte, barba.")

    tiene_corte = "corte" in servicios_norm
    tiene_barba = "barba" in servicios_norm

    # 1. Cálculo base y combo
    if tiene_corte and tiene_barba:
        subtotal = (PRECIO_CORTE + PRECIO_BARBA) * (1.0 - DESCUENTO_COMBO)
    elif tiene_corte:
        subtotal = PRECIO_CORTE
    elif tiene_barba:
        subtotal = PRECIO_BARBA
    else:
        subtotal = 0.0

    # 2. Descuento por cliente frecuente (>= 5 visitas)
    if visitas_mes >= 5:
        subtotal -= DESCUENTO_FRECUENTE

    # El cobro no puede ser menor a cero
    total = max(0.0, subtotal)
    return round(float(total), 2)


def calcular_penalizacion_cancelacion(
    costo_servicio: float,
    horas_anticipacion: Union[int, float],
    no_show: bool = False
) -> float:
    """
    Calcula la penalización por cancelación según la regla R2.

    Reglas:
    - >= 24 horas de anticipación: Sin costo (0% de penalización, cargo = $0.00 MXN).
    - Entre 2 y 24 horas (2 <= horas < 24): 50% del valor del servicio.
    - Menos de 2 horas (horas < 2) o no se presenta (no_show=True): 100% del valor del servicio.

    :param costo_servicio: Importe original presupuestado del servicio.
    :param horas_anticipacion: Horas que faltan para la cita al momento de cancelar.
    :param no_show: Indica si el cliente simplemente no se presentó a su cita.
    :return: Monto de penalización a cobrar en MXN (redondeado a 2 decimales).
    :raises ValueError: Si el costo del servicio o las horas de anticipación son negativos.
    """
    if costo_servicio < 0:
        raise ValueError("El costo del servicio no puede ser negativo.")

    if horas_anticipacion < 0:
        raise ValueError("Las horas de anticipación no pueden ser un valor negativo.")

    if no_show or horas_anticipacion < 2.0:
        cargo = costo_servicio * 1.0
    elif 2.0 <= horas_anticipacion < 24.0:
        cargo = costo_servicio * 0.50
    else:
        # 24 horas o más
        cargo = 0.0

    return round(float(cargo), 2)
