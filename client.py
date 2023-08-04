import socket
import sys

def main():
    host = "127.0.0.1"
    port = 8080

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    while True:
        try:
            message = input("Mensagem: ")
            client.send(message.encode())
            if message.lower() == 'sair':
                break
            response = client.recv(1024)
            print(f"Resposta do servidor: {response.decode()}")
            if response.decode() == 'sair':
                print("Servidor encerrado. Conexão encerrada.")
                
                client.send('sair'.encode())
                break
        except KeyboardInterrupt:
            print("Conexão encerrada pelo cliente.")
            client.send("sair".encode())
            break
        except:
            break

    client.close()

if __name__ == "__main__":
    main()
