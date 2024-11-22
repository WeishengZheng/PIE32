import re

codigo_fuente = open("codigoFuente.txt", "r")
codigo_resultado = open("codigoResultado.txt", "w")

nombreValido = r"[A-Za-z_][A-Za-z0-9_]*"

finalizado = r".*?(?=;)"

try:
    codigo = codigo_fuente.read()
    print(len(codigo))
    palabras = codigo.split() #creo que va a ser mejor hacer todo con expresiones regulares en vez de separar palabras
    for i in range(0, len(palabras)):
        if palabras[i] == "int":
            if re.match(nombreValido, palabras[i+1]):
                linea = f"{palabras[i+1]}: word."
                if palabras[i+2] == "=":
                    n = 3;
                    #while (not(re.match(finalizado, palabras[i+n]))):
                        #linea += f" {palabras[i+n]}"
                        #n += 1

    print(linea)
finally:
    codigo_fuente.close()
    codigo_resultado.close()