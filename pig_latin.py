# Jordan Marcelo Pig Latin Program assignment for COMSC 078 @ EVC, 9/30/24
# This program is designed to translate user-inputted sentences into pig Latin, under the following rules:
# If the word begins with a vowel, add “way” at the end of the word.
# Otherwise, move all the consonants from the beginning of the word [consonants until first vowel] to the end, and add “ay” to the end.
def to_pig_latin(word):
    """Translates a word into pig latin."""
    vowels = set("aeiouy")

    if word[0] in vowels: #if word begins with a vowel:
        return word + "way"

    modified_word = word
    for i, letter in enumerate(word):
        if letter in vowels: #finds first vowel
            return modified_word[i:] + modified_word[:i] + "ay" #returns pig latin word
    return modified_word + "ay" #if no vowels, returns pig latin word

def translate_to_pig_latin(sentence):
    """Translates a sentence into pig latin"""
    words = sentence.split()  # breaks sentence into list of words
    latin_words = []
    for word in words:
        latin_words.append(to_pig_latin(word))  # adds each individually translated pig latin word to list of pig latin words
    return " ".join(latin_words) # turns list of pig latin words into a sentence string to be returned

def main():
    """Takes user inputted sentence, splits it into a list of words, translates each word into pig latin,
    and then reassembles the sentence as a sentence in pig Latin."""
    while True:
        sentence = input("Your sentence to be translated to pig latin: ").lower() #makes inputted sentence lowercase
        if not sentence: #exits program if no text is inputted
            break
        print(translate_to_pig_latin(sentence), "\n") #prints sentence in pig latin

if __name__ == "__main__":
    main()