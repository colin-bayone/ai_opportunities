import sys

def read_chunk(filepath, start, length):
    with open(filepath, 'r') as f:
        f.seek(start)
        chunk = f.read(length)
    print(f"[Bytes {start}-{start+len(chunk)} of file]")
    print(chunk)
    return len(chunk)

if __name__ == "__main__":
    filepath = sys.argv[1]
    start = int(sys.argv[2])
    length = int(sys.argv[3])
    read_chunk(filepath, start, length)
