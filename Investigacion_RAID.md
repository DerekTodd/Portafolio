# Investigación sobre RAID (Arreglo Redundante de Discos Independientes)

## Introducción a RAID

RAID (*Redundant Array of Independent Disks* o Arreglo Redundante de Discos Independientes) es una tecnología de almacenamiento que combina múltiples discos duros o SSD en una o más unidades lógicas para mejorar redundancia, rendimiento o capacidad. RAID distribuye o replica datos entre discos, permitiendo al sistema operativo tratarlos como una sola unidad. Es común en servidores, NAS y sistemas de alto rendimiento como edición de video o bases de datos, donde la pérdida de datos sería crítica.

Originalmente, RAID usaba discos económicos para superar las limitaciones de discos costosos, pero hoy se integra en chipsets de placas base y soporta HDD y SSD, siendo más accesible.

## Historia de RAID

El término RAID fue acuñado en 1987 por investigadores de la Universidad de California, Berkeley (David Patterson, Garth Gibson y Randy Katz) en el artículo *"A Case for Redundant Arrays of Inexpensive Disks"*. Inicialmente, se enfocaba en discos "económicos" (Inexpensive), pero evolucionó a "independientes" (Independent). RAID se estandarizó en niveles, y su uso creció con la caída de precios de discos. Actualmente, soporta NVMe y usa IA para optimizar rendimiento y eficiencia energética. Sin embargo, alternativas como *erasure coding* y la infraestructura hiperconvergida están reduciendo su dependencia, especialmente con SSD.

## Niveles de RAID

RAID se clasifica en niveles estándar, anidados y no estándar, usando técnicas como *striping* (división de datos), *mirroring* (espejo) o *parity* (paridad). A continuación, una tabla comparativa de los niveles más comunes:

| Nivel | Descripción | Mínimo de Discos | Tolerancia a Fallos | Ventajas | Desventajas | Usos Típicos |
|-------|-------------|------------------|---------------------|----------|-------------|--------------|
| **RAID 0** (Striping) | Divide datos entre discos sin redundancia. | 2 | Ninguna (falla un disco, se pierden todos los datos). | Máximo rendimiento; 100% capacidad; fácil y barato. | Sin protección; riesgo alto con más discos. | Edición de video, juegos, cachés no críticos. |
| **RAID 1** (Mirroring) | Crea copias exactas en discos pares. | 2 | Tolera fallo de 1 disco por par. | Alta fiabilidad; lecturas rápidas; fácil recuperación. | Solo 50% capacidad; escritura lenta; caro. | Servidores críticos (email, contabilidad). |
| **RAID 5** (Striping con Paridad) | Divide datos y paridad entre discos. | 3 | Tolera fallo de 1 disco. | Equilibrio rendimiento/capacidad; lecturas rápidas; hot-swap. | Escrituras lentas; reconstrucción riesgosa; pierde datos si fallan 2 discos. | Servidores de archivos, NAS, aplicaciones de lectura intensiva. |
| **RAID 6** (Striping con Doble Paridad) | Similar a RAID 5, con dos bloques de paridad. | 4 | Tolera fallo de 2 discos. | Mayor redundancia; lecturas rápidas; ideal para arrays grandes. | Escrituras más lentas; reconstrucción lenta; caro. | Bases de datos, backups, videos grandes. |
| **RAID 10** (1+0: Mirroring + Striping) | Espeja datos y los divide en stripes. | 4 | Tolera 1 fallo por par (hasta mitad de discos). | Alto rendimiento; reconstrucción rápida; buena redundancia. | Solo 50% capacidad; caro; escalabilidad limitada. | Bases de datos, servidores web, transacciones. |

**Otros niveles**:
- **RAID 2/3/4**: Obsoletos o nicho; usan paridad dedicada con limitaciones (e.g., RAID 3 para video).
- **Anidados**: RAID 50 (5+0) o RAID 01 (0+1) combinan niveles, pero son costosos.
- **No estándar**: RAID 7 (con caché) o Adaptive RAID, son propietarios y poco comunes.

## RAID Hardware vs Software

- **RAID Hardware**: Usa controladores dedicados. **Ventajas**: Mayor rendimiento, menor carga en CPU, hot-swap fácil. **Desventajas**: Costoso.
- **RAID Software**: Gestionado por el sistema operativo. **Ventajas**: Barato, flexible. **Desventajas**: Carga CPU, menor rendimiento, compatibilidad limitada.

## Ventajas y Desventajas Generales

**Ventajas**:
- Protección contra pérdida de datos (niveles redundantes).
- Mejora de rendimiento (I/O solapado).
- Mayor capacidad y escalabilidad.
- Costo-efectivo con discos baratos.
- Alta disponibilidad post-fallo.

**Desventajas**:
- Configuración y mantenimiento complejos.
- Costo inicial alto en niveles redundantes.
- Riesgo de fallo en cascada si no se reconstruye rápido.
- No protege contra virus o errores humanos.
- Menos necesario con SSD por su durabilidad.

## Desarrollos Recientes y Conclusión

En 2025, RAID evoluciona con soporte para discos de mayor capacidad, controladores NVMe y optimización mediante IA. Sin embargo, *erasure coding* y SSD están reduciendo su uso en algunos casos. RAID sigue siendo clave para almacenamiento confiable, pero la elección del nivel depende de las necesidades: RAID 0 para velocidad, RAID 1/5/6 para redundancia, RAID 10 para equilibrio. Se recomienda combinar RAID con backups, ya que no los reemplaza. Consulta guías de fabricantes como QNAP o HPE para implementaciones.