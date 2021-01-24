def get_playback(filename="Files/Playback_0001.lpb"):
    """ Reimplementation of LoadPlayback. Open .lpb file and return
    a keyboard buffer of the moves """
    LEVEL_DATA_SIZE = 576

    # Data to collect:
    # from tRecordRec PBRec
    {
        char
    LName[31]; // Level
    Name
    char
    Author[31]; // Author
    of
    the
    recording
    WORD
    Level; // Level
    Number
    WORD
    Size; // Size
    of
    Data - - Data
    to
    fallow
    }

    byte_offset = (self.number - 1) * LEVEL_DATA_SIZE
    with open(self.filename, "rb") as f:
        f.seek(byte_offset, 0)  # Seek to byte offset relative to start of file
        chunk = f.read(LEVEL_DATA_SIZE)
        if chunk:
            playfield_bytes = chunk[0:256]
            self.playfield_initial_ints = [
                [playfield_bytes[i + (16 * j)] for i in range(16)]
                for j in range(16)
            ]
            self.title = chunk[256:287].decode("utf-8").rstrip("\x00")
            self.hint = chunk[287:543].decode("utf-8").rstrip("\x00")
            self.author = chunk[543:574].decode("utf-8").rstrip("\x00")
            self.difficulty = int.from_bytes(
                chunk[574:576], byteorder="little", signed=False
            )
            return True
        else:
            return False
