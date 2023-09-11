import socket

domain = "vulnweb.com"

names = [
    "testphp", "testasp", "testaspnet", "rest", "testhtml5", "www", "intranet",
    "ns1", "ftp"
]

for name in names:
    dns = f'{name}.{domain}'
    try:
        print(f'{dns}:{socket.gethostbyname(dns)}')
    except socket.gaierror:
        print(f'Error getting DNS')

print(f'\nEnumeration completed')