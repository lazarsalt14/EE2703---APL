keys={
    # Left side - Number row
    '1': {'pos': (0, 4), 'side': 'left', 'start': 's'},
    '2': {'pos': (1, 4), 'side': 'left', 'start': 's'},
    '3': {'pos': (2, 4), 'side': 'left', 'start': 'd'},
    '4': {'pos': (3, 4), 'side': 'left', 'start': 'f'},
    '5': {'pos': (4, 4), 'side': 'left', 'start': 'g'},

    # Left side - Top row
    'q': {'pos': (0, 3), 'side': 'left', 'start': 's'},
    'w': {'pos': (1, 3), 'side': 'left', 'start': 's'},
    'e': {'pos': (2, 3), 'side': 'left', 'start': 'd'},
    'r': {'pos': (3, 3), 'side': 'left', 'start': 'f'},
    't': {'pos': (4, 3), 'side': 'left', 'start': 'g'},

    # Left side - Home row
    'a': {'pos': (0, 2), 'side': 'left', 'start': 's'},
    's': {'pos': (1, 2), 'side': 'left', 'start': 's'},
    'd': {'pos': (2, 2), 'side': 'left', 'start': 'd'},
    'f': {'pos': (3, 2), 'side': 'left', 'start': 'f'},
    'g': {'pos': (4, 2), 'side': 'left', 'start': 'g'},

    # Left side - Bottom row
    'z': {'pos': (0, 1), 'side': 'left', 'start': 's'},
    'x': {'pos': (1, 1), 'side': 'left', 'start': 's'},
    'c': {'pos': (2, 1), 'side': 'left', 'start': 'd'},
    'v': {'pos': (3, 1), 'side': 'left', 'start': 'f'},
    'b': {'pos': (4, 1), 'side': 'left', 'start': 'g'},

    # Right side - Number row
    '6': {'pos': (0+10, 4), 'side': 'right', 'start': 'h'},
    '7': {'pos': (1+10, 4), 'side': 'right', 'start': 'j'},
    '8': {'pos': (2+10, 4), 'side': 'right', 'start': 'k'},
    '9': {'pos': (3+10, 4), 'side': 'right', 'start': 'l'},
    '0': {'pos': (4+10, 4), 'side': 'right', 'start': 'l'},

    # Right side - Top row
    'y': {'pos': (0+10, 3), 'side': 'right', 'start': 'h'},
    'u': {'pos': (1+10, 3), 'side': 'right', 'start': 'j'},
    'i': {'pos': (2+10, 3), 'side': 'right', 'start': 'k'},
    'o': {'pos': (3+10, 3), 'side': 'right', 'start': 'l'},
    'p': {'pos': (4+10, 3), 'side': 'right', 'start': 'l'},

    # Right side - Home row
    'h': {'pos': (0+10, 2), 'side': 'right', 'start': 'h'},
    'j': {'pos': (1+10, 2), 'side': 'right', 'start': 'j'},
    'k': {'pos': (2+10, 2), 'side': 'right', 'start': 'k'},
    'l': {'pos': (3+10, 2), 'side': 'right', 'start': 'l'},
    ';': {'pos': (4+10, 2), 'side': 'right', 'start': 'l'},

    # Right side - Bottom row
    'n': {'pos': (0+10, 1), 'side': 'right', 'start': 'h'},
    'm': {'pos': (1+10, 1), 'side': 'right', 'start': 'j'},
    ',': {'pos': (2+10, 1), 'side': 'right', 'start': 'k'},
    '.': {'pos': (3+10, 1), 'side': 'right', 'start': 'l'},
    '/': {'pos': (4+10, 1), 'side': 'right', 'start': 'l'},

    # Special keys
    'Shift_L': {'pos': (0, 0), 'side': 'left', 'start': 's'},
    'Ctrl_L': {'pos': (1, 0), 'side': 'left', 'start': 's'},
    'Alt_L': {'pos': (2, 0), 'side': 'left', 'start': 's'},
    'Space1': {'pos': (4, 0), 'side': 'center', 'start': 'h'},
    'Space2': {'pos': (10, 0), 'side': 'center', 'start': 'h'},
    'Alt_R': {'pos': (2+10, 0), 'side': 'right', 'start': 'j'},
    'Ctrl_R': {'pos': (3+10, 0), 'side': 'right', 'start': 'l'},
    'Shift_R': {'pos': (4+10, 0), 'side': 'right', 'start': 'l'},
}

characters = {
    # Lowercase letters
    'a': ('A',), 'b': ('B',), 'c': ('C',), 'd': ('D',), 'e': ('E',),
    'f': ('F',), 'g': ('G',), 'h': ('H',), 'i': ('I',), 'j': ('J',),
    'k': ('K',), 'l': ('L',), 'm': ('M',), 'n': ('N',), 'o': ('O',),
    'p': ('P',), 'q': ('Q',), 'r': ('R',), 's': ('s',), 't': ('T',),
    'u': ('U',), 'v': ('V',), 'w': ('W',), 'x': ('X',), 'y': ('Y',),
    'z': ('Z',),

    # Uppercase letters (Shift combinations)
    'A': ('Shift_L', 'a'), 'B': ('Shift_L', 'b'), 'C': ('Shift_L', 'c'),
    'D': ('Shift_L', 'd'), 'E': ('Shift_L', 'e'), 'F': ('Shift_L', 'f'),
    'G': ('Shift_L', 'g'), 'H': ('Shift_R', 'h'), 'I': ('Shift_R', 'i'),
    'J': ('Shift_R', 'j'), 'K': ('Shift_R', 'k'), 'L': ('Shift_R', 'l'),
    'M': ('Shift_R', 'm'), 'N': ('Shift_R', 'n'), 'O': ('Shift_R', 'o'),
    'P': ('Shift_R', 'p'), 'Q': ('Shift_L', 'q'), 'R': ('Shift_L', 'r'),
    'S': ('Shift_L', 's'), 'T': ('Shift_L', 't'), 'U': ('Shift_R', 'u'),
    'V': ('Shift_L', 'v'), 'W': ('Shift_L', 'w'), 'X': ('Shift_L', 'x'),
    'Y': ('Shift_R', 'y'), 'Z': ('Shift_L', 'z'),

    # Numbers
    '1': ('1',), '2': ('2',), '3': ('3',), '4': ('4',), '5': ('5',),
    '6': ('6',), '7': ('7',), '8': ('8',), '9': ('9',), '0': ('0',),

    # Other symbols
    '-': ('-',), '=': ('=',), '[': ('[',), ']': (']',), '\\': ('\\',),
    ';': (';',), "'": ("'",), ',': (',',), '.': ('.',), '/': ('/',),
    '`': ('`',),
    
    # Space
    ' ': ('Space1',)
}
