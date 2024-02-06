MORSE_CODE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
                   'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
                   'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                   'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                   'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ',': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-', '!': '-.-.--'}


def encode(txt1):
    cyphertxt = ""

    case_info = {}

    for i, alpha in enumerate(txt1):
        if alpha.islower():
            case_info[i] = 0
        elif alpha.isupper():
            case_info[i] = 1
        else:
            case_info[alpha] = None

    for char in txt1:
        if char == " ":
            cyphertxt += "  "
        else:
            cyphertxt += (MORSE_CODE_DICT.get(char.upper()))
            cyphertxt += " "

    return cyphertxt, case_info


def decode(cyphrtxt, dict1):
    plntxt = ""
    check = ""
    fnl_lst = ""

    tstlst = cyphrtxt.split(" ")

    for char in tstlst:
        if char == "":
            check += " "
            if check == "  ":
                plntxt += " "
                check = ""
        else:
            for ke, val in MORSE_CODE_DICT.items():
                if char == val:
                    plntxt += ke

    for i, char in enumerate(plntxt):
        if dict1.get(i) == 1:
            fnl_lst += char.upper()
        elif dict1.get(i) == 0:
            fnl_lst += char.lower()
        else:
            fnl_lst += char

    return fnl_lst


if __name__ == "__main__":
    inp = input("Enter your text:\n")
    ret1, ret2 = encode(inp)
    print()
