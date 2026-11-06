"""Ejercicio 1521: procesamiento de oraciones y vocales."""

import unicodedata


def normalizar(texto: str) -> str:
    """Elimina acentos y convierte el texto a minúsculas."""
    texto = texto.lower()
    caracteres = unicodedata.normalize("NFD", texto)
    return "".join(
        caracter for caracter in caracteres
        if unicodedata.category(caracter) != "Mn"
    )


def palabras_con_vocales(texto: str) -> list[str]:
    """Obtiene palabras con al menos tres vocales diferentes."""
    palabras = texto.replace(".", " ").split()
    resultado: list[str] = []

    for palabra in palabras:
        vocales = set(normalizar(palabra)) & set("aeiou")
        if len(vocales) >= 3:
            resultado.append(palabra)

    return resultado


def analizar_oraciones(texto: str) -> tuple[int, float]:
    """Cuenta oraciones y calcula el porcentaje de las largas."""
    oraciones = texto.split(".")
    cantidad = 0
    largas = 0

    for oracion in oraciones:
        if oracion.strip():
            cantidad += 1
            if len(oracion.split()) > 5:
                largas += 1

    porcentaje = largas * 100 / cantidad if cantidad else 0.0
    return cantidad, porcentaje


def main() -> None:
    """Lee un texto y presenta sus estadísticas."""
    lineas: list[str] = []
    continuar = True

    while continuar:
        linea = input("Ingrese una línea: ")
        if linea.endswith("*"):
            lineas.append(linea[:-1])
            continuar = False
        else:
            lineas.append(linea)

    texto = " ".join(lineas)
    palabras = palabras_con_vocales(texto)
    cantidad, porcentaje = analizar_oraciones(texto)

    print("Palabras con tres vocales diferentes:", palabras)
    print("Cantidad de oraciones:", cantidad)
    print("Porcentaje de oraciones con más de cinco palabras:", porcentaje)


if __name__ == "__main__":
    main()
