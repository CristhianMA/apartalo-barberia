# 2. El product backlog

> Ejercicio 2 · Tema 6 · 🎩 PO Las historias van como **issues** (formulario "Historia de usuario"). Aquí va lo demás.

## 2.1 Roles

| Rol | Quién es | Qué desea |
|---|---|---|
| Cliente | Usuario que acude a la barbería a cortarse el cabello o arreglarse la barba. | Reservar citas rápidamente, consultar tarifas claras y recibir promociones por servicios combinados o visitas frecuentes. |
| Don Rogelio | Dueño y administrador de Barbería Filo. | Maximizar la ocupación de sus 3 sillas, proteger sus ingresos ante inasistencias y supervisar la agenda diaria. |
| Barbero | Profesional del local asignado a una estación de trabajo. | Conocer su agenda diaria con antelación para preparar sus herramientas y atender puntualmente a sus clientes. |

## 2.4 Plantilla invertida: historias que me faltaban

`Para poder <beneficio>, como <rol>, quiero <deseo>`

| Beneficio que revisé | Historia que encontré | Issue |
|---|---|---|
| Abastecer la barbería con insumos y toallas limpias oportunamente | Como Don Rogelio, quiero generar un reporte de insumos requeridos según las citas agendadas al día siguiente. | #14 |
| Conservar mi espacio y evitar penalizaciones económicas | Como Cliente, quiero reagendar la fecha u hora de mi cita con al menos 24 horas de anticipación sin costo extra. | #15 |

¿Cómo me ayudó ordenar por beneficio?  
Permitió detectar necesidades operativas invisibles desde la perspectiva de la interfaz: al pensar primero en el valor de no quedarse sin toallas limpias o de no perder clientes por agendas rígidas, surgieron requerimientos logísticos indispensables que no estaban contemplados en los formularios iniciales.

## 2.5 Glosario (lenguaje ubicuo)

| Término | Qué significa para mi cliente |
|---|---|
| Cita | Bloque de tiempo reservado por un cliente en una silla específica para recibir uno o más servicios. |
| Silla | Estación física de trabajo atendida por un barbero; el local cuenta con exactamente 3 sillas disponibles. |
| Combo | Contratación simultánea de corte y barba en la misma cita, sujeta a un 15% de descuento sobre el costo base. |
| Cliente Frecuente | Cliente con 5 o más citas completadas dentro del mismo mes calendario, acreedor a una bonificación de $20. |
| No Show | Situación donde el cliente no se presenta a su cita pactada ni cancela previamente; amerita cobro del 100%. |

## 2.6 El iceberg

- **En la punta:** Historias pequeñas, claras y prioritarias del Sprint 1 (cálculo de corte/barba, combo del 15%, cliente frecuente y penalizaciones R2).
- **En el fondo:** Épicas grandes y de alta incertidumbre técnica o legal (pasarela de pagos directos `#1` y sincronización con software contable `#2`).
- **Por qué:** Porque lo que está en la punta aporta valor inmediato para el negocio y está listo para codificarse, mientras que lo que está en el fondo requiere exploración, dependencias externas o contratos antes de poder descomponerse en historias pequeñas (INVEST).
