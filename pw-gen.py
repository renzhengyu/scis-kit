# This program generates passwords for SCIS student accounts.
# Password Complexity designed by Paul Pavao.
# The complexity is designed to match the cognitive capacity of LS and US.
# Version 1.0 coded by Zhengyu Ren, Feb 7, 2023.
# This code requires Python 3.10 or above.
import random
import re

# Specify the complexity of the passwords. 'LS' for Lower School, or 'US' for Upper School;
complexity = 'LS'

# Specifiy how many passwords to generate
pw_to_generate = 10

# CONST
# Case insensitive
short_adjs = ['big', 'dry', 'fab', 'far', 'fun', 'icy', 'low', 'new', 'odd', 'old',
              'one', 'red', 'sad', 'shy', 'six', 'sly', 'ten', 'tin', 'top', 'two', 'zap', 'zip']
short_nouns = ['ape', 'arm', 'bat', 'bed', 'bee', 'bot', 'bug', 'bus', 'can', 'cat', 'cow', 'cup', 'dog', 'egg', 'fog',
               'fox', 'hat', 'hat', 'hen', 'jam', 'jar', 'map', 'owl', 'pet', 'rat', 'sun', 'toe', 'toe', 'toy', 'tub', 'wig', 'zoo']
num_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
              'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
vowels = ['a', 'e', 'i', 'o', 'u']
special_chars = ['!', '@', '#', '$', '%', '&']
taboos = ['420', '69', 'a55', 'caca', 'coc', 'cok', 'cum', 'dic', 'dik', 'diq', 'fag', 'feca1', 'fuc', 'fuk', 'homo', 'hore', 'jew',
          'jiz', 'kike', 'los', 'lus', 'nig', 'nude', 'ora1', 'paki', 'pedo', 'peni', 'peni5', 'pus', 'rape', 'sex', 'tit', 'vag', 'vaj']


def contains_taboo_word(the_word):
    for taboo_word in taboos:
        if re.search(taboo_word, the_word, re.IGNORECASE):
            return True
    return False


def main():
    match complexity:
        case 'LS':
            pw_generated = 0
            while pw_generated < pw_to_generate:
                pw_segments = []
                pw_segments.append(random.choice(short_adjs))
                pw_segments.append(random.choice(short_nouns))
                pw_segments.append(random.choice(num_chars))
                pw_segments.append(random.choice(num_chars))
                password = ''.join(pw_segments)
                if not contains_taboo_word(password):
                    print(password.title())
                    pw_generated += 1
        case 'US':
            pw_generated = 0
            while pw_generated < pw_to_generate:
                pw_segments = []
                pw_segments.append(random.choice(consonants))
                pw_segments.append(random.choice(vowels))
                pw_segments.append(random.choice(consonants))
                pw_segments.append(random.choice(vowels))
                pw_segments.append(random.choice(num_chars))
                pw_segments.append(random.choice(num_chars))
                pw_segments.append(random.choice(num_chars))
                pw_segments.append(random.choice(num_chars))
                pw_segments.append(random.choice(special_chars))
                password = ''.join(pw_segments)
                if not contains_taboo_word(password):
                    print(password.title())
                    pw_generated += 1
        case _:
            print('Specify the complexity.')


if __name__ == "__main__":
    main()
