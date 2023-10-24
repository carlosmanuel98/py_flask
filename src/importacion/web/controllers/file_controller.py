
from flask import request, jsonify

import csv#libreria directa de py
from decouple import config#paquete para variable de entorno

def leer_csv():
    try:
        print('paso por bff y llego al back')
        name_file = 'datos.csv'
        archivo_csv = config('PATH_STATIC') + f'/csv/{name_file}'

        # Nombre del archivo CSV
        # Inicializa una lista para almacenar los datos del CSV
        datos = []
        
        # Abre el archivo CSV y lee sus contenidos
        with open(archivo_csv, newline='') as file:
            csv_reader = csv.reader(file, delimiter=',')
            
            for row in csv_reader:
                # datos.append(row)

                dni, nombre, edad, sexo = row
                if dni.strip() == "95020363":
                    datos.append(row)
                    print( f'Este dni es el bueno {dni}' )
                else:
                    print(f'DNI: {dni} Nombre: {nombre} Edad: {edad} Sexo: {sexo}')

        # Retorna los datos como una respuesta HTML (puedes personalizar esto)
        return datos
        #return jsonify(datos)
    except Exception as e:
        # return f"Se produjo una excepción no manejada: {e}"
        return {'error': str(e)}

#Retorna ruta actual
def get_url(value):
    current_url = request.url
    print("********************->", request)
    return f'{current_url}{value}'