import socket

def data_stream_generator(host, port):
    # Create a TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))

    try:
        while True:
            # Receive data from the socket
            data = sock.recv(1024)
            if not data:
                break
            yield data

    finally:
        # Close the socket when done
        sock.close()

# Example usage
host = '127.0.0.1'
port = 9999

# Create the data stream generator
data_gen = data_stream_generator('google.com', 80)

# Process the data stream
for data in data_gen:
    print(data)
