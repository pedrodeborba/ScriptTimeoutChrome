import time
import pyautogui
import subprocess
import psutil

def is_chrome_open():
    """
    Verifica se o Google Chrome está aberto.
    """
    chrome_process = "chrome.exe"
    for proc in psutil.process_iter():
        if proc.name() == chrome_process:
            return True
    return False

def close_chrome():
    """
    Fecha o Google Chrome.
    """
    subprocess.run(["taskkill", "/F", "/IM", "chrome.exe"])

def main():
    # Tempo limite de inatividade em segundos
    timeout = 120 #2min
    timeout_counter = 0  # Inicialize timeout_counter

    print("Iniciando monitoramento de inatividade...")

    while True:
        while True:
            # Obter a posição atual do mouse
            x, y = pyautogui.position()

            # Aguardar por 1 segundo
            time.sleep(1)

            # Verificar se a posição do mouse mudou
            if pyautogui.position() != (x, y):
                # O mouse se moveu... Reseta o contador de tempo
                timeout_counter = 0
            else:
                # O mouse não se moveu... Incrementa o contador de tempo
                timeout_counter += 1

            # Verifica se o contador de tempo atingiu o tempo limite
            if timeout_counter >= timeout:
                print("Inatividade detectada por mais de 2 minutos.")
                # Verifica se o Google Chrome está aberto
                if is_chrome_open():
                    # Fecha o Google Chrome
                    print("Fechando o Google Chrome...")
                    close_chrome()
                    print("Google Chrome fechado após inatividade.")
                else:
                    print("Google Chrome não está aberto.")
                break

        # Aguarda por um período antes de começar a monitorar novamente
        time.sleep(10)  # Aguarda 10 segundos antes de começar a monitorar novamente

if __name__ == "__main__":
    main()
