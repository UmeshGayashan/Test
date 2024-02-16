import sys

def dog():
    print("Baw")

def default():
    print("Hello")

def main():
    if sys =.argv[1]=='dog':
        dog()
    else:
        default()

if _name_=='_main_':
    main()
