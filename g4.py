import socket

def stream_data(host, port, buffer_size=1024):
    """
    Generator that streams data from a network socket.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))
        while True:
            data = sock.recv(buffer_size)
            if not data:
                break
            yield data

# Example usage: stream data from a network socket
for data_chunk in stream_data("google.com", 80):
    # Process each chunk of data
    print(f"Received {len(data_chunk)} bytes of data")
    # Additional processing logic here
