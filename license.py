# Jordan Marcelo COMSC 078 @ EVC, 9/30/24
# This program is designed to grade a test based on user inputted answers and an assumed answer key
def correct_answers(test, key):
    """returns number of correct answers (elements where the corresponding elements between
    the inputted test and answer key are the same) and a list of the element numbers whose
    answers are incorrect"""
    num_correct, i, wrong_answers = 0, 0, []
    for i, ans in enumerate(key):
        if test[i] == ans:
            num_correct += 1
        else:
            wrong_answers.append(i+1)
    return num_correct, wrong_answers

def collect_answers(test_length):
    """Collects answers for every question on the test based on the number of test questions, test_length"""
    user_input = []
    for i in range(test_length):
        user_input.append(str(input("Answer to question " + str(i + 1) + ": ")).upper())
    return user_input

def main():
    """Collects user answers to the test, compares them to the answer key"""
    answer_key = "A C A A D B C A C B A D C A D C B B D A".split()
    test_length = len(answer_key)
    user_answers = collect_answers(test_length)

    num_correct, wrong_answers = correct_answers(user_answers, answer_key)
    print("Number of correct answers:", num_correct)
    print("Number of incorrect answers:", test_length-num_correct)
    if num_correct >= 15:
        print("You passed the test.")
    else:
        print("You did not pass the test.")
    print("Questions you answered incorrectly:", wrong_answers)

if __name__ == "__main__":
    main()