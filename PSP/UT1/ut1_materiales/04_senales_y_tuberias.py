# 04_senales_y_tuberias.py
# Manejo de señales y ejemplo de tuberia estilo shell.

import signal
import time
import sys
import subprocess
import os

def handler(signum, frame):
    print(f'Proceso {os.getpid()}: recibido {signum}. Saliendo.')
    sys.exit(0)

def ejemplo_senales():
    signal.signal(signal.SIGINT, handler)
    try:
        signal.signal(signal.SIGTERM, handler)
    except AttributeError:
        print('SIGTERM no disponible en esta plataforma')
    print(f'PID: {os.getpid()} - espera señales')
    while True:
        time.sleep(1)

def ejemplo_pipe():
    try:
        p1 = subprocess.Popen(['ls','-la'], stdout=subprocess.PIPE, text=True)
        p2 = subprocess.Popen(['grep','py'], stdin=p1.stdout, stdout=subprocess.PIPE, text=True)
        p1.stdout.close()
        out = p2.communicate()[0]
        print('Salida filtrada:'); print(out)
    except FileNotFoundError as e:
        print('Comando no encontrado', e)

def main():
    if len(sys.argv)>1 and sys.argv[1]=='pipe':
        ejemplo_pipe()
    else:
        ejemplo_senales()

if __name__=='__main__':
    main()
