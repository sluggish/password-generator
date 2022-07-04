import random
import string
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--length", type=int, dest="length", default=16)
    args = parser.parse_args()
    generate_pw(args.length)

def generate_pw(length: int):
    options = string.ascii_letters + string.punctuation + string.digits
    pw = "".join(random.choices(options, k=length))
    print("generated password: '{0}'".format(pw))

main()
