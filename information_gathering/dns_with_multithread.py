from queue import Queue
import threading, socket, os

script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, "subdomains.txt")

dominio = "vulnweb.com"
lock = threading.Lock()
q = Queue()

def enumeration():
    while True:
        dns = q.get()
        if dns is None:
            break
        full_dns = f'{dns}.{dominio}'
        try:
            ip = socket.gethostbyname(full_dns)
            lock.acquire()
            print(f'{full_dns}:\t{ip}')
        except socket.gaierror:
            print(f'Error getting DNS')
        else:
            lock.release()
        q.task_done()

# Ler subdomínios e colocá-los na fila
with open(file_path) as sub:
    for line in sub:
        dns = line.strip()
        q.put(dns)

# Iniciar as threads
threads = []
num_threads = 10  # Altere o número de threads conforme necessário

for _ in range(num_threads):
    t = threading.Thread(target=enumeration)
    threads.append(t)
    t.start()

# Aguardar até que todas as threads terminem
for _ in range(num_threads):
    q.put(None)

for t in threads:
    t.join()

print(f'\nEnumeration completed')
