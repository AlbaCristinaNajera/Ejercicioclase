def calculo_promedio(notas):
    suma = sum(notas)
    promedio = suma / len(notas)
    return promedio

def guardar(alumnos):
    with open("promedios.txt", "w") as archivo:
        for alumno in alumnos:
            datos = alumno.split(",")
            nombre = datos[0]
            notas = [int(nota) for nota in datos[1:]]
            promedio = calculo_promedio(notas)
            archivo.write(f"{nombre}: {promedio}\n")

alumnos = ["Juan,99,85,89,95", "Jose,90,83,88,81", "Pedro,100,80,99,90"]
guardar(alumnos)