def media(suma_total_numeros, cantidad_valores):
    return suma_total_numeros / cantidad_valores
    # Función no necesaria para funcionar


def main():
    contador = 0
    suma_total = 0
    while contador <= 7:
        try:
            if contador >= 7:
                print(f"Media: {media(suma_total, contador):.1f}")
                # Calcula la media con la suma total / contador
                break
            nota = float(input(f"Nota {contador+1}: "))
            suma_total += nota
            contador += 1
        except ValueError as error:
            print(f"Ha ocurrido un error, valor no esperado (solo numeros)")
            print(error)
            exit()


if __name__ == '__main__':
    main()