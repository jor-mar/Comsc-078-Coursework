import numpy as np

def randomize_caps(word):
    liszt = list()
    for i, l in enumerate(word):
        if np.random.choice([True, False]):
            liszt.append(l.upper())
        else:
            liszt.append(l.lower())
    return "".join(liszt)

def main():
    while True:
        text = input("Text to be randomly capitalized: ")
        if text == "":
            break
        print(randomize_caps(text), "\n")

if __name__ == '__main__':
    main()