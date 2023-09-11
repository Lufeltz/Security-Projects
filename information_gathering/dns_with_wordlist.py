import socket, os

# Obtém o diretório do script atual
script_directory = os.path.dirname(os.path.abspath(__file__))

# Constrói o caminho completo para o arquivo subdomains.txt
file_path = os.path.join(script_directory, "subdomains.txt")

domain = "vulnweb.com"

with open(file_path) as sub:
  subdomains = sub.readlines()
  
for sub in subdomains:
  dns = f'{sub.rstrip()}.{domain}'
  try:
    print(f"{dns}: {socket.gethostbyname(dns)}")
  except socket.gaierror:
    print(f'Error getting DNS')
    
print(f'\nEnumeration completed')