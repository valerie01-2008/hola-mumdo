def validar_edad_para_conducir():
    try:
        edad = int(input("Introduce la edad de la persona: "))
    except ValueError:
        print("Por favor, ingresa un número válido.")
        return

    if edad < 16:
        print("No puede obtener licencia.")
    elif 16 <= edad <= 17:
        print("Puedes solicitar licencia de aprendiz.")
    else:  # edad >= 18
        print("Puedes obtener licencia completa.")

if __name__ == "__main__":
    validar_edad_para_conducir()
