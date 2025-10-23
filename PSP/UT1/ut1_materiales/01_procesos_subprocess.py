# 01_procesos_subprocess.py
# Uso de subprocess para ejecutar comandos del sistema y guardar salida.

import subprocess
import sys
import os

def listar_directorio_y_guardar(ruta, fichero_salida='salida.txt'):
    # Detecta sistema operativo
    if os.name == 'nt':
        comando = ['cmd', '/C', 'dir', ruta]
    else:
        comando = ['ls', '-la', ruta]
    try:
        resultado = subprocess.run(comando, capture_output=True, text=True, check=False)
    except FileNotFoundError as e:
        print('Error: ejecutable no encontrado.', e)
        return False
    except Exception as e:
        print('Error al ejecutar proceso.', e)
        return False
    if resultado.stderr:
        print('STDERR:', resultado.stderr)
    try:
        with open(fichero_salida, 'w', encoding='utf-8') as f:
            f.write(resultado.stdout)
    except Exception as e:
        print('Error al escribir fichero:', e)
        return False
    print(f"Listado de '{ruta}' guardado en '{fichero_salida}' (rc={resultado.returncode})")
    return True

def main():
    ruta='.'
    if len(sys.argv)>1:
        ruta=sys.argv[1]
    listar_directorio_y_guardar(ruta)

if __name__=='__main__':
    main()
