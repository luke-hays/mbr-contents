# https://thestarman.pcministry.com/asm/mbr/index.html
# https://learning.oreilly.com/videos/mastering-python/9781771373104/9781771373104-video193401/
# Struct allows us to examin data structure piece by piece
import struct

# Parsing a ByteArray(MBR - First 512 Bytes of Disk)
# The main drive im working on is a GUID partion table (GPT) - so a little different than MBR
# Looks like a window feature. possible way to extend this includes being able to differentiate between platforms

# GPT - https://thestarman.pcministry.com/asm/mbr/GPT.htm
# NT Disk signature is set to zero "00 00 00 00"
def main():
    # Windows file path to disk
    mbr_path = '\\\\.\\PhysicalDrive0'
    mbr = bytearray()

    # read byte array in
    f = open(mbr_path, "rb")
    try:
        mbr = f.read(512) # '
    finally:
        f.close()

    # dumping the hex out to understand how this is broken up
    print(mbr)
    print()
    # No disk signature found here
    sig = struct.unpack('<I', mbr[0x1B8:0x1BC])
    print('Disk Signature: ', sig[0])

    # Bootable is considered active
    # GPT will not be bootable ot ensure legacy BIOS or OS will not boot
    active = mbr[0x1BE]
    if active == 0x80:
        print('Active flag: Active')
    else:
        print('Active flag: Not active')
    
    # Three bytes indicate partition starts at CHS (0,0,2) absolute sector 1
    print('Start sectors: ' + str(mbr[0x1BF:0x1C2]))

    # byte indicating GPT partitioned disk
    if (mbr[0x1C2] == 0xEE):
        print('GPT Partitioned Disk')
    else:
        print('MBR Disk')

    # CHS ending values - only used if partition didnt end beyond 16,450,560 sectors
    print('Ending Sectors: ' + str(mbr[0x1C3:0x1C6]))

    # next four bytes indicate numbers of sectors preceding partition
    # - 01 00 00 00 - one sector - the mbr
    print('sectors preceding partion: ' + str(mbr[0x1C6:0x1CA]))

    # the unpack is the number of sectors
    print('partition size: ' + str(mbr[0x1CA:0x1CE]) + ' or ' + str(struct.unpack('<I', mbr[0x1CA:0x1CE])[0]))

    # At this point probably look into GPT Header

    lbastart = struct.unpack('<I', mbr[0x1C6:0x1CA])
    print('Partition Start (LBA): ', lbastart[0])
    lbaend = struct.unpack('<I', mbr[0x1C9:0x1CD])
    print('Partition End (LBA): ', lbaend[0])

if __name__ == '__main__':
    main()

