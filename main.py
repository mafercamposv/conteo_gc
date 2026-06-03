# Elemento | Descripción |
# Responsabilidad | Leer un archivo FASTA y extraer la secuencia de ADN. |
# Entrada | `ruta_archivo`, una cadena de texto con el nombre o ruta del archivo FASTA. |
# Salida | Una cadena de texto con la secuencia de ADN. |
def leer_fasta(ruta_archivo):
    secuencia = ""
    with open(ruta_archivo, "r") as archivo:
        for linea in archivo:
            if not linea.startswith(">"):
                secuencia += linea.strip()
    return secuencia


# Elemento | Descripción |
# Responsabilidad | Calcular el porcentaje de GC de una secuencia de ADN. |
# Entrada | Una secuencia de ADN como cadena de texto. |
# Salida | Un número decimal con el porcentaje de GC. |
def calcular_porcentaje_gc(secuencia):
    gc_count = secuencia.upper().count("G") + secuencia.upper().count("C")
    total_count = len(secuencia)
    if total_count == 0:
        return 0
    return (gc_count / total_count) * 100
