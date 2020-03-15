file = open('train.txt','r')
trained_text_without_padding = file.read()
file = open('test.txt','r')
test_text_without_padding = file.read()

#padding for training text
training_file = 'train.txt'
trained_text_padded = ""
with open(training_file) as fp:
   line = fp.readline()
   while line:
    #    line = line[0:len(line)-2]
       trained_text_padded+='<s> ' + line + ' </s> '
       line = fp.readline()
#padding for testing text
testing_file = 'test.txt'
test_text_padded=""
with open(testing_file) as fp:
   line = fp.readline()
   while line: 
    #    line = line[0:len(line)-2]
       test_text_padded +='<s> ' + line + ' </s> '
       line = fp.readline()
# print(trained_text_padded[0:2000])
#lowercasing all words
trained_text_without_padding = trained_text_without_padding.lower()
test_text_without_padding = test_text_without_padding.lower()
trained_text_padded = trained_text_padded.lower()
test_text_padded = test_text_padded.lower()

trained_text_without_padding_splitted = trained_text_without_padding.split()
print("total number of words excluding <s> and </s> is " + str(len(trained_text_without_padding_splitted)))
# trained_text_padded = "<s>"
# for character in trained_text:
#     if character == '.':
#         trained_text_padded += ".</s><s>"
#     else:
#         trained_text_padded += character
# print(trained_text_padded[0:1000])

# file = open('test.txt','r')
# test_text = file.read()
# test_text = test_text.lower()


# test_text_padded = "<s>"
# for character in test_text:
#     if character == '.':
#         test_text_padded += ".</s><s>"
#     else:
#         test_text_padded += character
# print(test_text_padded[0:1000])

tokenized_training = trained_text_padded.split()
count_of_words = {}
# print(trained_text_padded)
#all words in tokenized text with padding! and map of how many times each word appeared
total_words_in_training_corpus = 0
print("The total words in the training corpus including <s> and </s> is " + str(len(tokenized_training)))
for word in tokenized_training:
    total_words_in_training_corpus += 1
    if count_of_words.get(word) == None:
        count_of_words[word] = 1
    else:
        count_of_words[word] +=1
print("The total words in the training corpus including <s> and </s> is " + str(total_words_in_training_corpus))
print("total number of unique words in the training set is including <s> and </s> is" + str(len(count_of_words)))

tokenized_training_unk = ""#this is the training set with unk
for word in tokenized_training:
    if count_of_words[word] == 1:
        tokenized_training_unk += '<unk> '
        count_of_words[word] = 0
    else:
        tokenized_training_unk += word + " "

# print(tokenized_training_unk[0:6000])


#replace all words in test set never seen in training set with unk
test_text_splitted = test_text_padded.split()
trained_text_splitted = trained_text_padded.split()
unk_replaced_test = ""#testing set with unk
total_number_of_words = 0
total_number_of_unks = 0
for word in test_text_splitted:
    total_number_of_words+=1
    # if word[0:3] == '<s>':
    #     word = word[3:]
    # elif word[len(word)-4:] == '</s>':
    #     word = word[0:len(word)-4]
    # if word != ',' and word != '\"':
    if word not in trained_text_splitted:
        unk_replaced_test += '<unk>'
        total_number_of_unks+=1
        continue
    unk_replaced_test += word + " "
print('yick')
# print(unk_replaced_test[0:500])
print(total_number_of_words)
print(total_number_of_unks)
print("the percentage of word tokens and word types in the test corpus that did not occur in training is" + 
      str((total_number_of_unks/total_number_of_words)*100) + '%')

      ################ unigram omdels

unigram_model = {}
sum_of_all_unigram_prob = 0
for word in count_of_words:
    unigram_model[word] = count_of_words[word]/total_words_in_training_corpus
    sum_of_all_unigram_prob+=unigram_model[word]
print("the sum of all the unigram prob is close to 1 so its working it is" + str(sum_of_all_unigram_prob))


##########bigram models
bigram_model = {}
total_number_of_bigrams = 0
tokenized_training_unk_splitted = tokenized_training_unk.split()
for i in range(len(tokenized_training_unk_splitted)-1):
    bigram_key = tokenized_training_unk_splitted[i] + "," + tokenized_training_unk_splitted[i+1]
    if bigram_model.get(bigram_key) == None:
        bigram_model[bigram_key] = 1
    else:
        bigram_model[bigram_key] = bigram_model[bigram_key] + 1
    total_number_of_bigrams+=1





# print(total_number_of_bigrams)
total_sum=0
count=0
for key in bigram_model:
    value = bigram_model[key]
    total_sum += value/total_number_of_bigrams
    bigram_model[key] = value/total_number_of_bigrams
    if count == 15:
        break
    count+=1
    print(str(key) + str(bigram_model[key]))
print(total_sum)#should equal 1
# print(bigram_model)


# #add one smoothing
# bigram_model_add1_smoothing = {}
# # total_number_of_bigrams = total_number_of_bigrams*2
# total_sum = 0
# count = 0
# for key in bigram_model:
#     # count +=1
#     # if count == 50: 
#     #     break
#     value = bigram_model[key]
#     print(key)
#     bigram_model_add1_smoothing[key] = ((value*total_number_of_bigrams) + 1)/(2*total_number_of_bigrams)
#     print(value*total_number_of_bigrams)
#     print(2*total_number_of_bigrams)
#     total_sum += bigram_model_add1_smoothing[key]
# print(total_sum)





######## no need for this trigram model.
# trigram_model = {}
# tokenized_training_unk_splitted = tokenized_training_unk.split()
# for i in range(len(tokenized_training_unk_splitted)-2):
#     trigram_key = tokenized_training_unk_splitted[i] + "," + tokenized_training_unk_splitted[i+1] + "," + tokenized_training_unk_splitted[i+2]
#     if trigram_model.get(trigram_key) == None:
#         trigram_model[trigram_key] = 1
#     else:
#         trigram_model[trigram_key] = trigram_model[trigram_key] + 1

# print(trigram_model)