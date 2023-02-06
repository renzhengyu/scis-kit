import random
import re

# Specify the complexity of the password. 'LS' for Lower School, or 'US' for Upper School;
complexity_level = 'US'

# Specifiy how many passwords you need to generate
passwords_to_generate = 100

# CONST
# Case insensitive
word_pool_short_adj = ["old", "big", "red", "odd", "low", "dry", "fun", "tin", "far", "new",
                       "top", "two", "six", "one", "ten", "sad", "shy", "fab", "icy", "sly", "zap", "zip"]
word_pool_short_noun = ["ape", "toy", "dog", "cat", "cup", "egg", "bat", "bed", "cow", "hat", "jar", "map", "fog", "toe", "arm",
                        "owl", "bee", "fox", "pet", "hat", "rat", "hen", "bus", "jam", "toe", "wig", "bug", "sun", "tub", "zoo", "bot", "can"]
word_pool_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
word_pool_consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k',
                        'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
word_pool_vowels = ['a', 'e', 'i', 'o', 'u']
word_poop_special_characters = ['!', '@', '#', '$', '%', '&']
word_pool_taboo = ['cum', 'dic', 'dik', 'diq', 'fag', 'fuk', 'fuc', 'homo', 'hore', 'jew', 'jiz', 'kike', 'los', 'lus', 'nig',
                   'peni', 'pus', 'rape', 'sex', 'tit', 'vag', 'vaj', '69', '420']


def contains_taboo_word(the_word):
    for taboo_word in word_pool_taboo:
        if re.search(taboo_word, the_word, re.IGNORECASE):
            return True
    return False


match complexity_level:
    case 'LS':
        password_generated = 0
        while password_generated < passwords_to_generate:
            password_segments = []
            password_segments.append(random.choice(word_pool_short_adj))
            password_segments.append(random.choice(word_pool_short_noun))
            password_segments.append(random.choice(word_pool_numbers))
            password_segments.append(random.choice(word_pool_numbers))
            password = ''.join(password_segments)
            if not contains_taboo_word(password):
                print(password.title())
                password_generated += 1
    case 'US':
        password_generated = 0
        while password_generated < passwords_to_generate:
            password_segments = []
            password_segments.append(random.choice(word_pool_consonants))
            password_segments.append(random.choice(word_pool_vowels))
            password_segments.append(random.choice(word_pool_consonants))
            password_segments.append(random.choice(word_pool_vowels))
            password_segments.append(random.choice(word_pool_numbers))
            password_segments.append(random.choice(word_pool_numbers))
            password_segments.append(random.choice(word_pool_numbers))
            password_segments.append(random.choice(word_pool_numbers))
            password_segments.append(
                random.choice(word_poop_special_characters))
            password = ''.join(password_segments)
            if not contains_taboo_word(password):
                print(password.title())
                password_generated += 1

    case _:
        print("Specify the complexity level.")
