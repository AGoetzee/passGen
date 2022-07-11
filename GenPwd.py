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


def convert_to_chr(x: list) -> list:
    """Converts a number (obtained through ord()) to a character.

    :param x: int - Number to be converted.
    :return: list - List of converted characters
    """
    return list(map(chr, x))


def create_pwd(charset: np.array, length: int) -> str:
    """Generates a random string of characters

    :param charset: np.array - List of characters to choose from
    :param length: int - Length of the string
    :return: str - Generated random string
    """
    ord_arr = np.random.choice(charset, length)
    chr_list = convert_to_chr(list(ord_arr))
    chr_string = ''.join(chr_list)
    return chr_string


def create_charset(inc_lowers: bool, inc_uppers: bool, inc_spec_chars: bool, inc_num: bool) -> np.array:
    """Generates character set for password

    :param inc_lowers: bool - Include lowercase characters
    :param inc_uppers: bool - Include uppercase characters
    :param inc_spec_chars: bool - Include special characters
    :param inc_num: bool - Include numbers
    :return: np.array - Character set
    """
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


def run(params: tuple = (True, True, True, True), length: int = 8) -> str:
    """Generates a random password.

    :param params: tuple - Parameters for generating passwords (INCLUDE_LOWERS, INCLUDE_UPPERS,
    INCLUDE_SPECIAL_CHARS, INCLUDE_NUMBERS)
    :param length: int - Password length
    :return: str - Password string
    """
    if True not in params:
        print('Need at least one character set.')
        return ''

    charset = create_charset(*params)
    pwd = create_pwd(charset, length=length)
    return pwd


if __name__ == '__main__':
    # For testing purposes
    for i in range(NUMBER_OF_PWD):
        print(run(params=(INCLUDE_LOWERS, INCLUDE_UPPERS, INCLUDE_SPECIAL_CHARS, INCLUDE_NUMBERS), length=LENGTH))