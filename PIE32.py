import re

codigo_fuente = open("codigoFuente.txt", "r")
codigo_resultado = open("codigoResultado.txt", "w")

nombreValido = r"[A-Za-z_][A-Za-z0-9_]*"

try:
    codigo = codigo_fuente.read()
    palabras = codigo.split()
    for i in range(0, len(palabras)):
        if palabras[i] == "int":
            if re.match(nombreValido, palabras[i+1]):
                linea = f"{palabras[i+1]}: word."
                if palabras[i+2] == "=":
                    linea += f" {palabras[i+3]}"


    print(linea)
finally:
    codigo_fuente.close()
    codigo_resultado.close()