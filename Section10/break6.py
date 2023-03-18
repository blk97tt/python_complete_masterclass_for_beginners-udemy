try:
    print(4 / 2)
except NameError:
    print("Name Error!")
finally:
    print("I don't care, I'm getting printed either way!")