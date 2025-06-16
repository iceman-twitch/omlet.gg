import json
from random_username.generate import generate_username


def Gen():
    fake = generate_username(1)
    fake = fake[0]
    return fake


data = {}
data[0] = Gen()

print( data )