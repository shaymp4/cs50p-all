def playback(user_sentence):
    return user_sentence.replace(' ', '...')

sentence = input("Enter your phrase: ")
new_sentence = playback(sentence)
print(new_sentence)
