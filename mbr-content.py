# https://thestarman.pcministry.com/asm/mbr/index.html
# Struct allows us to examin data structure piece by piece
import struct

# Parsing a ByteArray(MBR - First 512 Bytes of Disk)
def main():
    # Windows file path MBR
    mbr_path = '\\\\.\\PhysicalDrive0'
    mbr = bytearray()

    # read byte array in
    f = open(mbr_path, "rb")
    try:
        mbr = f.read(512) # '
    finally:
        f.close
        

    # look for locations in byte array
    # interpret data in there

    print()

if __name__ == '__main__':
    main()