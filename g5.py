def process_data_batch(data_batch):
    """
    Function to process a batch of data.
    """
    # Processing logic for the data batch goes here
    for data in data_batch:
        # Process each data item
        processed_data = process_data_batch(data)
        yield processed_data

def process_network_data(data_stream, batch_size):
    """
    Generator that processes network data in batches.
    """
    data_batch = []
    for data in data_stream:
        data_batch.append(data)
        if len(data_batch) == batch_size:
            yield from process_data_batch(data_batch)
            data_batch = []
    # Process the remaining data in the last batch
    if data_batch:
        yield from process_data_batch(data_batch)

# Example usage: processing network data in batches
data_stream = ['data1', 'data2', 'data3', 'data4', 'data5', 'data6']  # Example data stream
batch_size = 3

for processed_data in process_network_data(data_stream, batch_size):
    # Process the processed data
    print(processed_data)
