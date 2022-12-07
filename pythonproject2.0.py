from random import random
import random
from sre_parse import SPECIAL_CHARS
from tokenize import Special

uppercase = "abcdefghijklmnopqrstuvwxyz"
lowercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
special_characters = "!@#%^&*{[]_}-+=?/;:,"


all = uppercase + lowercase + special_characters + numbers
length = int(input())
password = "".join(random.sample(all,length))

print(password)
