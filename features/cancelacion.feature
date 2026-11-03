# language: es
Característica: Penalizaciones por cancelación tardía o inasistencia (Regla R2)
  Como Don Rogelio
  Quiero aplicar penalizaciones automáticas según el tiempo de anticipación
  Para proteger los ingresos de la barbería ante cancelaciones imprevistas

  Esquema del escenario: Cálculo de penalización según horas de anticipación
    Dado que una cita confirmada tiene un costo de <costo> pesos
    Cuando el cliente cancela con <horas> horas de anticipación
    Entonces la penalización cobrada es de <penalizacion> pesos

    Ejemplos:
      | costo  | horas | penalizacion |
      | 255.00 | 48.0  | 0.00         |
      | 255.00 | 24.0  | 0.00         |
      | 200.00 | 23.9  | 100.00       |
      | 200.00 | 2.0   | 100.00       |
      | 180.00 | 1.9   | 180.00       |
      | 180.00 | 0.0   | 180.00       |
