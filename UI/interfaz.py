def menu():
    print("\nBIENVENIDOS A CONSULTAS DE REPORTE DE COVID-19")
    registers_limit = int(input("Ingrese el limite de registros: "))
    departament_name = input("Digite el departamento: ")
    departament_name = departament_name.upper()
    return [registers_limit, departament_name]



