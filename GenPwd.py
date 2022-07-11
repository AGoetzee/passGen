import numpy as np

# Default values
NUMBER_OF_PWD = 3
LENGTH = 16
INCLUDE_SPECIAL_CHARS = True
INCLUDE_NUMBERS = True
INCLUDE_LOWERS = True
INCLUDE_UPPERS = True

# Character sets
UPPERS = np.array(range(ord('A'), ord('Z')))
LOWERS = np.array(range(ord('a'), ord('z')))
NUMS = np.array(range(ord('0'), ord('9')))
SPECIAL = np.array(list(map(ord, ['!', '@', '#', '$', '%', '&', '*'])))


def convert_to_chr(x):
    return list(map(chr, x))


def create_pwd(charset, length):
    ord_arr = np.random.choice(charset, length)
    chr_list = convert_to_chr(list(ord_arr))
    chr_string = ''.join(chr_list)
    return chr_string


def create_charset(inc_lowers, inc_uppers, inc_spec_chars, inc_num):
    c = np.array([], dtype='int')
    if inc_uppers:
        c = np.concatenate((c, UPPERS))
    if inc_lowers:
        c = np.concatenate((c, LOWERS))
    if inc_spec_chars:
        c = np.concatenate((c, SPECIAL))
    if inc_num:
        c = np.concatenate((c, NUMS))
    return c


if __name__ == '__main__':
    charset = create_charset(INCLUDE_LOWERS, INCLUDE_UPPERS, INCLUDE_SPECIAL_CHARS, INCLUDE_NUMBERS)
    for i in range(NUMBER_OF_PWD + 1):
        print(create_pwd(charset, LENGTH))
