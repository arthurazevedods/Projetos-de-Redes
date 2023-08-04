#O servidor usa a biblioteca socket 
#para criar um socket de rede, que será usado para ouvir conexões de clientes.
import socket
import threading


#A função handle_client é uma função que será executada em uma thread separada para cada
#cliente conectado. Essa função lida com a comunicação com cada cliente individualmente.
def handle_client(server,client_socket, client_address):
    #loop infinito para ler os dados do cliente individualmente
    while True:
        try:
            
            #1024 é o tamanho máximo de dados enviados de uma só vez    
            data = client_socket.recv(1024)
            if not data:
                break
            message = data.decode()
            print(f"Recebido de {client_address[0]}:{client_address[1]}: {message}")
            if message.lower() == 'sair':
                
                print(f"Conexão com {client_address[0]}:{client_address[1]} encerrada.")
                return server.close()
                
            response = input("Resposta: ")
            if response.lower() == 'sair':
                client_socket.send("sair".encode())
                
                return server.close()
                
            client_socket.send(response.encode())
        except KeyboardInterrupt:
            print("Conexão encerrada pelo cliente.")
            client_socket.send("sair".encode())
            server.close()
            break
        except:
            break

    client_socket.close()
    print(f"Conexão com {client_address[0]}:{client_address[1]} encerrada.")

def main():
    host = "127.0.0.1"
    port = 8080

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)

    print(f"[*] Servidor ouvindo em {host}:{port}")

    while True:
        client_socket, client_address = server.accept()
        print(f"[*] Conexão aceita de {client_address[0]}:{client_address[1]}")

        #threading: É o módulo em Python que fornece suporte para trabalhar com threads.

        #Thread: É uma classe dentro do módulo threading que nos permite criar e gerenciar threads.

        # uma thread é uma unidade básica de um processo, onde o processo é um programa em execução 
        #no sistema operacional. Cada processo pode ter uma ou várias threads que compartilham o 
        #mesmo espaço de endereçamento e recursos do processo pai.

        #target: É um argumento que recebe a função que será executada na thread. 
        
        #Neste caso, estamos passando handle_client como a função que será executada na nova thread.
         
        #Essa função trata a comunicação com o cliente e recebe o socket do cliente e o endereço 
        #do cliente como argumentos.
        client_handler = threading.Thread(target=handle_client, args=(server,client_socket, client_address))
        client_handler.start()

if __name__ == "__main__":
    main()
