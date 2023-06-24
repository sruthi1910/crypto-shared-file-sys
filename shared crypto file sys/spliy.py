
from split_helper import write_file, split_into_chunks, retrieve_all_chunks, join_chunks, read_chunk
import os


def split(filename,pwd,n):
    chunks = split_into_chunks(filename,4)
    # print("The chunks are : ", chunks)
    write_file(filename,pwd,n,chunks)
    os.remove(filename)


def recreate_file(filename,pwd):
    chunks = retrieve_all_chunks(filename,pwd)
    data_chunk = read_chunk(filename,chunks)
    data = join_chunks(filename,data_chunk,pwd)
    print("File created")
    f = open(filename, "w")
    f.write(data)
    f.close()
    # print(data)