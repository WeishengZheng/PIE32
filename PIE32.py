import re

codigo_fuente = open("codigoFuente.txt", "r")
codigo_resultado = open("codigoResultado.txt", "w")

nombreValido = r"[A-Za-z_][A-Za-z0-9_]*"
finalizado = r".*?(?=;)"
isInt = r"[0-9]*"
endWithComa = r".*?(?=,)"

try:
    codigo = codigo_fuente.read()
    palabras = codigo.split() #creo que va a ser mejor hacer todo con expresiones regulares en vez de separar palabras

    linea = 0
    i = 0
    while i < len(palabras):
        if re.match(r"int", palabras[i]):
            i += 1
            if re.match(nombreValido, palabras[i]):
                linea = f"{palabras[i]}: word."
                i += 1
                if re.match(r"=", palabras[i]):
                    i += 1
                    while not(re.match(finalizado, palabras[i])) and re.match(endWithComa, palabras[i]):
                        palabras[i] = palabras[i].replace(",", "")
                        if re.match(isInt, palabras[i]):
                            linea += f" {palabras[i]}"
                        palabras[i] = palabras[i].replace(";", "")
                        i += 1
                    if re.match(isInt, palabras[i]):
                        if re.match(isInt, palabras[i]):
                            linea += f" {palabras[i]}"
        linea += 1
        codigo_resultado = f"{linea}\n"
                            

    print(linea)
finally:
    codigo_fuente.close()
    codigo_resultado.close()