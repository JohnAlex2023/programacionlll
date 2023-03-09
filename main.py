from API import api
from UI import filtro_datos
from UI import interfaz


if __name__ == '__main__':
    registers_limit, departament_name = interfaz.menu()
    data = api.get_data(registers_limit, departament_name)
    filtered_data = filtro_datos.filter_columns(data)
    print(filtered_data)
