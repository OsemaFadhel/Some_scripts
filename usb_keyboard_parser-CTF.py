#!/usr/bin/python3

def get_character(keycode, shift, num_lock):
    # Windows keyboard mapping with NUM LOCK ON
    keymap_numlock_on = {
        0x04: ('a', 'A'), 0x05: ('b', 'B'), 0x06: ('c', 'C'), 0x07: ('d', 'D'),
        0x08: ('e', 'E'), 0x09: ('f', 'F'), 0x0A: ('g', 'G'), 0x0B: ('h', 'H'),
        0x0C: ('i', 'I'), 0x0D: ('j', 'J'), 0x0E: ('k', 'K'), 0x0F: ('l', 'L'),
        0x10: ('m', 'M'), 0x11: ('n', 'N'), 0x12: ('o', 'O'), 0x13: ('p', 'P'),
        0x14: ('q', 'Q'), 0x15: ('r', 'R'), 0x16: ('s', 'S'), 0x17: ('t', 'T'),
        0x18: ('u', 'U'), 0x19: ('v', 'V'), 0x1A: ('w', 'W'), 0x1B: ('x', 'X'),
        0x1C: ('y', 'Y'), 0x1D: ('z', 'Z'),

        # Numbers row
        0x1E: ('1', '!'), 0x1F: ('2', '@'), 0x20: ('3', '#'), 0x21: ('4', '$'),
        0x22: ('5', '%'), 0x23: ('6', '^'), 0x24: ('7', '&'), 0x25: ('8', '*'),
        0x26: ('9', '('), 0x27: ('0', ')'),

        # Special keys
        0x28: ('\n', '\n'), 0x29: ('\x1b', '\x1b'), 0x2A: ('\b', '\b'),  # Backspace
        0x2B: ('\t', '\t'),  # Tab
        0x2C: (' ', ' '),    # Space
        0x2D: ('-', '_'),    # - and _
        0x2E: ('=', '+'),    # = and +
        0x2F: ('[', '{'),    # [ and {
        0x30: (']', '}'),    # ] and }
        0x31: ('\\', '|'),   # \ and |
        0x32: ('#', '~'),    # # and ~ (Non-US keyboards)
        0x33: (';', ':'),    # ; and :
        0x34: ("'", '"'),    # ' and "
        0x35: ('`', '~'),    # ` and ~
        0x36: (',', '<'),    # , and <
        0x37: ('.', '>'),    # . and >
        0x38: ('/', '?'),    # / and ?

        # Numpad with NUM LOCK ON
        0x53: ('NumLock', 'NumLock'), 0x54: ('/', '/'), 0x55: ('*', '*'), 0x56: ('-', '-'),
        0x57: ('+', '+'), 0x58: ('Enter', 'Enter'),
        0x59: ('1', '1'), 0x5A: ('2', '2'), 0x5B: ('3', '3'),
        0x5C: ('4', '4'), 0x5D: ('5', '5'), 0x5E: ('6', '6'),
        0x5F: ('7', '7'), 0x60: ('8', '8'), 0x61: ('9', '9'),
        0x62: ('0', '0'), 0x63: ('.', '.')
    }

    # Windows keyboard mapping with NUM LOCK OFF
    keymap_numlock_off = {
        0x04: ('a', 'A'), 0x05: ('b', 'B'), 0x06: ('c', 'C'), 0x07: ('d', 'D'),
        0x08: ('e', 'E'), 0x09: ('f', 'F'), 0x0A: ('g', 'G'), 0x0B: ('h', 'H'),
        0x0C: ('i', 'I'), 0x0D: ('j', 'J'), 0x0E: ('k', 'K'), 0x0F: ('l', 'L'),
        0x10: ('m', 'M'), 0x11: ('n', 'N'), 0x12: ('o', 'O'), 0x13: ('p', 'P'),
        0x14: ('q', 'Q'), 0x15: ('r', 'R'), 0x16: ('s', 'S'), 0x17: ('t', 'T'),
        0x18: ('u', 'U'), 0x19: ('v', 'V'), 0x1A: ('w', 'W'), 0x1B: ('x', 'X'),
        0x1C: ('y', 'Y'), 0x1D: ('z', 'Z'),

        # Numbers row
        0x1E: ('1', '!'), 0x1F: ('2', '@'), 0x20: ('3', '#'), 0x21: ('4', '$'),
        0x22: ('5', '%'), 0x23: ('6', '^'), 0x24: ('7', '&'), 0x25: ('8', '*'),
        0x26: ('9', '('), 0x27: ('0', ')'),

        # Special keys
        0x28: ('\n', '\n'), 0x29: ('\x1b', '\x1b'), 0x2A: ('\b', '\b'),  # Backspace
        0x2B: ('\t', '\t'),  # Tab
        0x2C: (' ', ' '),    # Space
        0x2D: ('-', '_'),    # - and _
        0x2E: ('=', '+'),    # = and +
        0x2F: ('[', '{'),    # [ and {
        0x30: (']', '}'),    # ] and }
        0x31: ('\\', '|'),   # \ and |
        0x32: ('#', '~'),    # # and ~ (Non-US keyboards)
        0x33: (';', ':'),    # ; and :
        0x34: ("'", '"'),    # ' and "
        0x35: ('`', '~'),    # ` and ~
        0x36: (',', '<'),    # , and <
        0x37: ('.', '>'),    # . and >
        0x38: ('/', '?'),    # / and ?

        # Numpad with NUM LOCK OFF
        0x53: ('NumLock', 'NumLock'), 0x54: ('/', '/'), 0x55: ('*', '*'), 0x56: ('-', '-'),
        0x57: ('+', '+'), 0x58: ('Enter', 'Enter'),
        0x59: ('End', '1'), 0x5A: ('DownArrow', '2'), 0x5B: ('PageDown', '3'),
        0x5C: ('LeftArrow', '4'), 0x5D: ('Clear', '5'), 0x5E: ('RightArrow', '6'),
        0x5F: ('Home', '7'), 0x60: ('UpArrow', '8'), 0x61: ('PageUp', '9'),
        0x62: ('Insert', '0'), 0x63: ('Delete', '.')
    }

    keymap = keymap_numlock_on if num_lock else keymap_numlock_off

    if keycode in keymap:
        return keymap[keycode][1 if shift else 0]
    return ''

def main():
    result = []
    last_keycode = 0
    num_lock = True  # Assume NUM LOCK is initially enabled

    with open('hiddata.txt', 'r') as f:
        lines = f.readlines()

    for i in range(len(lines)):
        try:
            # Parse the HID data
            data = bytes.fromhex(lines[i].strip())

            if len(data) == 8:
                modifier = data[0]  # First byte is modifier
                keycode = data[2]   # Third byte is keycode

                # Check for shift
                shift = (modifier & 0x22) != 0

                if keycode == 0x53:  # NUM LOCK keycode
                    num_lock = not num_lock
                # Only process if it's a new keypress
                elif keycode != 0 and keycode != last_keycode:
                    # Convert special characters
                    if keycode == 0x36 and shift:  # < key
                        char = ','
                    elif keycode == 0x37 and shift:  # > key
                        char = '.'
                    elif keycode == 0x27 and not shift:  # 0 key
                        char = "'"  # For apostrophes
                    else:
                        char = get_character(keycode, shift, num_lock)

                    print(f"Modifier: {modifier}, Keycode: {keycode}, Shift: {shift}, Num Lock: {num_lock} | char: {char}")


                    if char:
                        result.append(char)

                last_keycode = keycode

            # Reset last_keycode on key release (all zeros)
            if data == bytes.fromhex('00' * 8):
                last_keycode = 0

        except Exception as e:
            print(f"Error processing line {lines[i].strip()}: {e}")

    # Replace "39" with apostrophe and "34" with double quote
    decoded_text = ''.join(result)

    # Write the result to a file
    with open('decoded_text.txt', 'w') as f:
        f.write(decoded_text)

    # Also print the result
    print('Decoded text:')
    print(decoded_text)

if __name__ == "__main__":
    main()
