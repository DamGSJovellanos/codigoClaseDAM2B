# 02_ipc_pipes_queue.py
# Ejemplos de Pipe y Queue para IPC.

from multiprocessing import Process, Pipe, Queue
import os
import sys

def worker_pipe(conn):
    try:
        msg = conn.recv()
    except EOFError:
        print('Hijo: conexion cerrada')
        return
    print(f'Hijo (PID {os.getpid()}): recibido -> {msg}')
    conteo = sum(1 for c in msg if c.isalpha())
    conn.send(conteo)
    conn.close()

def ejemplo_pipe():
    parent_conn, child_conn = Pipe()
    p = Process(target=worker_pipe, args=(child_conn,))
    p.start()
    texto = 'Hola Mundo' if len(sys.argv)<=1 else sys.argv[1]
    parent_conn.send(texto)
    res = parent_conn.recv()
    print(f'Padre: el hijo contó {res} letras')
    p.join()

def productor(q, items):
    for it in items:
        q.put(it)
    q.put(None)

def consumidor(q):
    total=0
    while True:
        item=q.get()
        if item is None:
            break
        total += sum(1 for c in item if c.isalpha())
    print(f'Consumidor (PID {os.getpid()}): total={total}')

def ejemplo_queue():
    q=Queue()
    datos=['hola','prueba','multiproceso']
    p_prod=Process(target=productor,args=(q,datos))
    p_cons=Process(target=consumidor,args=(q,))
    p_prod.start(); p_cons.start()
    p_prod.join(); p_cons.join()

def main():
    ejemplo_pipe()
    ejemplo_queue()

if __name__=='__main__':
    main()
