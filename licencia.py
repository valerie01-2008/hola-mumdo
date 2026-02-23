# Programa para determinar tipo de licencia según la edad

edad = int(input("¿Cuántos años tienes? "))

if edad < 16:
    print("No puede obtener licencia.")
elif edad == 16 or edad == 17:
    print("Puede obtener licencia de aprendiz.")
else:  # edad >= 18
    print("Puede obtener licencia completa.")
