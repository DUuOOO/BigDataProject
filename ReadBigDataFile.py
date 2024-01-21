# This code is suitable for data that does not require parsing.
# read content in chunks can run the code in a low memory
# as for a big data file of 10G, even 1T, if the data exclude '\n'
# efficiency has been improved by nearly 4 times
# and memory usage is now less than 1% of the original just use for line in file
def chunked_file_reader(fp, block_size=1024 * 8): # 8K
    """
    Generator Function: Reads file content in chunks using the iter function
    """
    # construct a new parameterless function using partial(fp.read, block_size)
    # The loop will continuously return the result of fp.read(block_size) calls until it is '' to terminate
    for chunk in iter(partial(fp.read, block_size), ''):
        yield chunk

def read_file_info(file):
    with open(file) as fp:
        for chunk in chunked_file_reader(fp):
            data.append(chunk)
    return data