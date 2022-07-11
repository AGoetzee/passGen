import numpy as np

NUMBER_OF_PWD = 3
LENGTH = 16
SPECIAL_CHARS = True
NUMBERS = True


def convert_to_chr(x):
    return list(map(chr, x))


uppers = np.array(range(ord('A'), ord('Z')))
lowers = np.array(range(ord('a'), ord('z')))
nums = np.array(range(ord('0'), ord('9')))
special = np.array(list(map(ord, ['[', ']', '!', '@', '#', '$', '%', '&', '*'])))

charset = np.concatenate((uppers, lowers))
if SPECIAL_CHARS:
    charset = np.concatenate((charset, special))
if NUMBERS:
    charset = np.concatenate((charset, nums))

for i in range(0, NUMBER_OF_PWD + 1):
    a = np.random.choice(charset, LENGTH)
    b = convert_to_chr(list(a))
    print(b)
    print(''.join(b))
