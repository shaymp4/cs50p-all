def indoor_voice(user_sentence):
    indoor_sentence = user_sentence.lower()
    return indoor_sentence

sentence = input("Enter your phrase: ")
new_sentence = indoor_voice(sentence)
print(new_sentence)
