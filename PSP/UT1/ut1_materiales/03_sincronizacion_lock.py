# 03_sincronizacion_lock.py
# Demostracion de race condition y uso de Lock para exclusión mutua.

from multiprocessing import Process, Lock, Manager
import time
import os

def incrementar(shared, key, vueltas, lock):
    pid = os.getpid()
    for _ in range(vueltas):
        with lock:
            shared[key] += 1
        time.sleep(0.001)
    print(f'Proceso {pid} finalizado')

def ejemplo_con_lock(vueltas=200, n=3):
    mgr = Manager(); shared = mgr.dict(); shared['contador']=0
    lock = Lock(); ps=[]
    for _ in range(n):
        p=Process(target=incrementar,args=(shared,'contador',vueltas,lock))
        ps.append(p); p.start()
    for p in ps: p.join()
    print('Valor final (con lock):', shared['contador'])

def main():
    ejemplo_con_lock()

if __name__=='__main__':
    main()
