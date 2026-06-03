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
