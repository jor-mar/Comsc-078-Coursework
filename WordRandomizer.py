import numpy as np

def word_randomizer(sentence):
    words = sentence.split(" ")
    liszt = list()
    for i in range(len(words)):
        chosen = np.random.choice(words)
        liszt.append(chosen)
        words.remove(chosen)
    return " ".join(liszt)

def main():
    while True:
        text = input("Sentence to be randomized: ")
        if text == "":
            break
        print(word_randomizer(text), "\n")

if __name__ == '__main__':
    main()