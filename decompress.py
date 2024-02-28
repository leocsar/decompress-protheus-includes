import zlib
import sys

with open(sys.argv[1], 'rb') as f:
    content = f.read()

decompress = zlib.decompressobj(-zlib.MAX_WBITS)
inflated = decompress.decompress(content[14:])
inflated += decompress.flush()

newFile = open(sys.argv[2], 'a')
newFile.write(inflated[:-1].decode('utf-8', errors='ignore'))
newFile.close()

# print(inflated[:-1].decode('utf-8', errors='ignore'))
