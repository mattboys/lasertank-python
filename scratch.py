filename="legacy_resources/Files/LaserTank.lvl"
chrs = {}
for i in range(2030):
    number = i + 1
    LEVEL_DATA_SIZE = 576
    byte_offset = (number - 1) * LEVEL_DATA_SIZE
    with open(filename, "rb") as f:
        f.seek(byte_offset, 0)  # Seek to byte offset relative to start of file
        chunk = f.read(LEVEL_DATA_SIZE)
        if chunk:
            playfield_bytes = chunk[0:256]
            text = chunk[256:574]
            for b in text:
                if b in chrs:
                    chrs[b] += 1
                else:
                    chrs[b] = 1
            difficulty = chunk[574:576]
        else:
            break
for b in sorted(chrs.keys()):
    print(f'{int(b)}\t{chrs[b]}\t({chr(b)})')