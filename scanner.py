import random

randomDS1 = random.randint(0,5)
randomDS2 = random.randint(0,3)
randomDS3 = random.randint(0,6)
randomDS4 = random.randint(0,3)
randomDS5 = random.randint(0,5)


ds1 = ['hii there!! ', 'hello ', 'hii ', 'how are you? ', 'whats going on? ', 'what are you doing these days? ']
ds2 = ["you know, I kind of like you... ", "I just don't like your face too much... ", "I wanted to tell you ", "that "]
ds3 = ['so','I was kind of wondering... ','and ','you know, ','which ','is ','exactly ']
ds4 = ["I just wanted to tell you that ", "I am done now! ", "thanks for hearing me! ",
      "you are a great person, thanks for giving me a chance! "]
ds5 = ["bye! ", "see you later! ", "will see you again! ", "send my regards! ", "good bye! ", "Tanay... "]


print("Welcome to the random message generator!!\nPlease note, that these messages may not have any semantic meaning on them, but if you get a message with a meaning, consider yourself lucky!!")

message = ds1[randomDS1]+ds2[randomDS2]+ds3[randomDS3]+ds4[randomDS4]+ds5[randomDS5]
print(message)

