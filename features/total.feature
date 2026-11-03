# language: es
Característica: Cálculo de costos y descuentos en citas (Regla R1)
  Como Don Rogelio y cliente de Barbería Filo
  Quiero que el sistema calcule las tarifas automáticamente
  Para cobrar lo justo y aplicar las promociones vigentes

  Esquema del escenario: Cálculo de tarifas con combo y visitas mensuales
    Dado que un cliente solicita los servicios <servicios>
    Y cuenta con <visitas> visitas completadas en el mes
    Cuando el sistema calcula el costo total de la cita
    Entonces el total a pagar es de <total> pesos

    Ejemplos:
      | servicios       | visitas | total  |
      | corte           | 0       | 180.00 |
      | barba           | 0       | 120.00 |
      | corte, barba    | 0       | 255.00 |
      | corte           | 4       | 180.00 |
      | corte           | 5       | 160.00 |
      | corte, barba    | 5       | 235.00 |
