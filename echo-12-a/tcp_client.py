import socket

def start_tcp_client(host='127.0.0.1', port=12345):
    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        message = input("Enter message to send (type 'exit' to quit): ")
        if message.lower() == 'exit':
            break

        client_socket.sendall(message.encode())
        data = client_socket.recv(1024)
        print(f"Echo from server: {data.decode()}")

    client_socket.close()

if __name__ == "__main__":
    start_tcp_client()
