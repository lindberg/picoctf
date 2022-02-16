def swap_elements(b, p1, p2):
    b[p1], b[p2] = b[p2], b[p1]


def get_flag(expected):
    password = ""
    for e in expected:
        # divide into bits
        bits = [
            (e >> 7) & 1,
            (e >> 6) & 1,
            (e >> 5) & 1,
            (e >> 4) & 1,
            (e >> 3) & 1,
            (e >> 2) & 1,
            (e >> 1) & 1,
            e & 1
        ]

        # swap the bits
        # note: this is done in reverse order to decrypt
        swap_elements(bits, 6, 7)
        swap_elements(bits, 2, 5)
        swap_elements(bits, 3, 4)
        swap_elements(bits, 0, 1)
        swap_elements(bits, 4, 7)
        swap_elements(bits, 5, 6)
        swap_elements(bits, 0, 3)
        swap_elements(bits, 1, 2)

        # convert to bit string
        bits = [str(bit) for bit in bits]


        # convert bit string to character
        c = chr(int("".join(bits), 2))

        # append chracter to password
        password += c

    return "picoctf{" + password + "}"



if __name__ == "__main__":
    expected = [
        0xF4,
        0xC0,
        0x97,
        0xF0,
        0x77,
        0x97,
        0xC0,
        0xE4,
        0xF0,
        0x77,
        0xA4,
        0xD0,
        0xC5,
        0x77,
        0xF4,
        0x86,
        0xD0,
        0xA5,
        0x45,
        0x96,
        0x27,
        0xB5,
        0x77,
        0xD2,
        0xD0,
        0xB4,
        0xE1,
        0xC1,
        0xE0,
        0xD0,
        0xD0,
        0xE0
    ]

    flag = get_flag(expected)

    print(flag)