import time

def generate_infinite_data():
    """
    Generator that generates an infinite data stream.
    """
    while True:
        # Generate data or fetch data from a network source
        data = fetch_data_from_network()
        yield data
        time.sleep(1)  # Simulate delay between data items

# Example usage: processing an infinite data stream
data_stream = generate_infinite_data()

for data in data_stream:
    # Process each data item from the infinite stream
    print(data)
    # Additional processing logic here
