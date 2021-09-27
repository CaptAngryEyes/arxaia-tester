from random import shuffle

from verb import energitiki, mesi

def get_energitiki_questions():
    keys = list(energitiki.keys())
    shuffle(keys)
    questions = [(key, energitiki[key]) for key in keys]
    return questions

def get_mesi_questions():
    keys = list(mesi.keys())
    shuffle(keys)
    questions = [(key, mesi[key]) for key in keys]
    return questions

def get_all_questions():
    ener_keys = list(energitiki.keys())
    shuffle(ener_keys)
    ener_questions = [(key, energitiki[key]) for key in ener_keys]

    mesi_keys = list(mesi.keys())
    shuffle(mesi_keys)
    mesi_questions = [(key, mesi[key]) for key in mesi_keys]

    questions = (ener_questions + mesi_questions)
    shuffle(questions)
    return questions

def main():
    amount = 5
    number_of_questions = 0

    questions = get_energitiki_questions()
    for question in questions:
        if amount != number_of_questions:
            answer = input(f'{question[0]}: ')
            if answer == question[1]:
                print('CORRECT')
            else:
                print('WRONG')
                print(question[1])
            print() #Empty Line
            number_of_questions += 1
        else:
            break

if __name__ == '__main__':
    main()