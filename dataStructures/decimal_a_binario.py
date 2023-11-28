
def decimal_a_binario(numero):
    # Convierte un número decimal a binario
    if numero < 0:
        raise ValueError("El número debe ser un entero no negativo.")

    binario = format(numero, '06b')

    return binario

def binario_a_decimal(binario):
    # Convierte un número binario a decimal
    decimal = int(binario, 2)

    return decimal

def main():
    try:
        # Solicitamos al usuario que elija la dirección de conversión
        direccion = input("Ingrese 'db' para convertir de decimal a binario o 'bd' para convertir de binario a decimal: ")

        if direccion == 'db':
            # Convertir de decimal a binario
            numero_entero = int(input("Ingrese un número entero no negativo en decimal: "))
            binario = decimal_a_binario(numero_entero)
            print(f"El número {numero_entero} en binario (6 bits) es: {binario}")

        elif direccion == 'bd':
            # Convertir de binario a decimal
            binario = input("Ingrese un número binario (6 bits): ")
            
            if len(binario) != 6:
                raise ValueError("El número binario debe tener exactamente 6 bits.")
            
            decimal = binario_a_decimal(binario)
            print(f"El número binario {binario} en decimal es: {decimal}")

        else:
            print("Dirección no válida. Debe ingresar 'db' o 'bd'.")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()