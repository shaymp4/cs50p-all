def convert(sentence):
    sentence = sentence.replace(':)','🙂')
    new_sentence = sentence.replace(':(','🙁')
    return new_sentence

def main():
    user_sentence = input("Enter text for conversion: ")
    final_sentence = convert(user_sentence)
    print(final_sentence)

main()