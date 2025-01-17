import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            print(f"\n{message}")
        except ConnectionResetError:
            print("Connection to server lost.")
            break

    client_socket.close()

def start_client(host='127.0.0.1', port=12345):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    print("Connected to the chat server.")
    
    # Start a thread to listen for incoming messages
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    while True:
        message = input("You: ")
        if message.lower() == 'exit':
            print("Disconnecting from server...")
            client_socket.close()
            break
        client_socket.sendall(message.encode())

if __name__ == "__main__":
    start_client()
