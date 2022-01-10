# Converts any integer into a base [BASE] number. I have chosen 62
# as it is meant to represent the integers using all the alphanumeric
# characters, [no special characters] = {0..9}, {A..Z}, {a..z}
#
# I plan on using this to shorten the representation of possibly long ids,
# a la url shortenters
#
# saturate()  takes the base 62 key, as a string,
# and turns it back into an integer
# dehydrate() takes an integer and turns it into the base 62 string

import math
from hashlib import md5
import re


BASE = 62

UPPERCASE_OFFSET = 55
LOWERCASE_OFFSET = 61
DIGIT_OFFSET = 48


def get_re_url(string):
    """
    Using re, takes 3 matches, 's' for 'https' or  'http' as for 'p',
    get match after www.,
    last one is domain.
    Create string.
    """
    regex = r"^((ftp|http|https):\/\/)?www\.([A-z]+)\.([A-z]{2,})"
    matches = re.search(regex, string)
    return matches[2][-1] + matches[3] + matches[4]


def true_ord(char):
    """
    Turns a digit [char] in character representation
    from the number system with base [BASE] into an integer.
    """
    if char.isdigit():
        return ord(char) - DIGIT_OFFSET
    elif "A" <= char <= "Z":
        return ord(char) - UPPERCASE_OFFSET
    elif "a" <= char <= "z":
        return ord(char) - LOWERCASE_OFFSET
    else:
        raise ValueError("%s is not a valid character" % char)


def true_chr(integer):
    """
    Turns an integer [integer] into digit in base [BASE]
    as a character representation.
    """
    if integer < 10:
        return chr(integer + DIGIT_OFFSET)
    elif 10 <= integer <= 35:
        return chr(integer + UPPERCASE_OFFSET)
    elif 36 <= integer < 62:
        return chr(integer + LOWERCASE_OFFSET)
    else:
        raise ValueError("%d is not a valid integer, base %d" % (integer, BASE))


def saturate(key):
    """
    Turn the base [BASE] number [key] into an integer
    """
    int_sum = 0
    reversed_key = key[::-1]
    for idx, char in enumerate(reversed_key):
        int_sum += true_ord(char) * int(math.pow(BASE, idx))
    return int_sum


def dehydrate(integer):
    """
    Turn an integer [integer] into a base [BASE] number
    in string representation
    """
    if integer == 0:
        return "0"

    string = ""
    while integer > 0:
        remainder = integer % BASE
        string = true_chr(remainder) + string
        integer = int(integer // BASE)
    return string


def hash_m5(int_sum):
    """
    Hash and grab the first 6 values.
    """
    hash = md5(str(int_sum).encode())
    digest = hash.hexdigest()[:6]
    return digest


def to_short_url(user_url):
    """
    Combine all functions into one in order to create short url.
    """
    new_url = get_re_url(user_url)
    sate = saturate(new_url)
    short_url = hash_m5(sate)
    return short_url
