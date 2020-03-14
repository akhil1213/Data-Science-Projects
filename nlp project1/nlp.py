file = open('train.txt','r')


trained_text = file.read()

trained_text = trained_text.lower()
for line in file:
    print(line)


trained_text_padded = "<s>"
for character in trained_text:
    if character == '.':
        trained_text_padded += ".</s><s>"
    else:
        trained_text_padded += character
print(trained_text_padded[0:1000])

file = open('test.txt','r')
test_text = file.read()
test_text = test_text.lower()


test_text_padded = "<s>"
for character in test_text:
    if character == '.':
        test_text_padded += ".</s><s>"
    else:
        test_text_padded += character
print(test_text_padded[0:1000])

tokenized_training = trained_text_padded.split()
count_of_words = {}

#all words in tokenized text with padding!
total_words_in_training_corpus = 0
for word in tokenized_training:
    total_words_in_training_corpus += 1
    
    if count_of_words.get(word) == None:
        count_of_words[word] = 1
    else:
        count_of_words[word] +=1
print("The total words in the training corpus including <s> and </s> is " + str(total_words_in_training_corpus))

#all words in tokenized text without padding!
tokenized_training = trained_text.split()
total_words_in_training_corpus = 0
for word in tokenized_training:
    total_words_in_training_corpus += 1
    
    if count_of_words.get(word) == None:
        count_of_words[word] = 1
    else:
        count_of_words[word] +=1
print("The total words in the training corpus not including <s> and </s> is " + str(total_words_in_training_corpus))

tokenized_training_unk = ""
for word in tokenized_training:
    if count_of_words[word] == 1:
        tokenized_training_unk += '<unk> '
        count_of_words[word] = 0
    else:
        tokenized_training_unk += word + " "

count = 0
for item in count_of_words:
    count = count + 1
print(count)
print(tokenized_training_unk[0:6000])

tokenized_test = test_text_padded.split()
unk_replaced_test = ""
total_number_of_words = 0
total_number_of_unks = 0
for word in tokenized_test:
    total_number_of_words+=1
    if word[0:3] == '<s>':
        word = word[3:]
    elif word[len(word)-4:] == '</s>':
        word = word[0:len(word)-4]
    if word != ',' and word != '\"':
        if word not in trained_text_padded:
            unk_replaced_test += '<unk>'
            total_number_of_unks+=1
            continue
    unk_replaced_test += word + " "
print(unk_replaced_test[0:500])
print(total_number_of_words)
print(total_number_of_unks)
print("the percentage of word tokens and word types in the test corpus that did not occur in training is" + 
      str(total_number_of_unks/total_number_of_words))