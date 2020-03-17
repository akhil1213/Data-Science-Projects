import math
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
total_number_of_unique_words_in_training = len(count_of_words)
print("total number of unique words in the training set is including <s> and </s> is" + str(total_number_of_unique_words_in_training))

tokenized_training_unk = ""#this is the training set with unk
count_of_words['<unk>'] = 0
for word in tokenized_training:
    if count_of_words[word] == 1:
        tokenized_training_unk += ' <unk> '
        count_of_words[word] = 0
        count_of_words['<unk>'] = count_of_words['<unk>']+1
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
        unk_replaced_test += ' <unk> '
        total_number_of_unks+=1
        continue
    unk_replaced_test += word + " "
# print(unk_replaced_test)
print("total number of words in test set is: " + str(total_number_of_words))
print("total number of unks in test set is: " + str(total_number_of_unks))
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
counts_of_bigram = {}
total_number_of_bigrams = 0
tokenized_training_unk_splitted = tokenized_training_unk.split()
sum_of_all_counts_with_a_word_before_it = {}
###############code to count each unique bigram and how many times it appeared in the dataset
for i in range(len(tokenized_training_unk_splitted)-1):
    bigram_key = tokenized_training_unk_splitted[i] + "," + tokenized_training_unk_splitted[i+1]

    #count num of bigrams
    if counts_of_bigram.get(bigram_key) == None:
        counts_of_bigram[bigram_key] = 1
    else:
        counts_of_bigram[bigram_key] = counts_of_bigram[bigram_key] + 1
    total_number_of_bigrams+=1

# count = 0
# for key in counts_of_bigram:
#     print (key + str(counts_of_bigram[key]))
#     count+=1
#     if count == 20:
#         break

########################## implementing this formula
# count(prevword,currentword)/sum(count(prevword,ANYWORDAFTERIT))
bigram_model_maximum = {}
for i in range(len(tokenized_training_unk_splitted)-1):
    bigram_key = tokenized_training_unk_splitted[i] + "," + tokenized_training_unk_splitted[i+1]
    numerator = counts_of_bigram[bigram_key]
    denom = count_of_words[tokenized_training_unk_splitted[i]]
    bigram_model_maximum[bigram_key] = numerator/denom
    # sumOfAllCountsWithPreviousWordAndAnyWordAfterIt=0
    # for j in range(len(tokenized_training_unk_splitted)-1):
    #     key = tokenized_training_unk_splitted[j]
    #     if key.find(',',1) != -1:
    #         if key[0:key.find(',',1)] == tokenized_training_unk_splitted[i]:
    #         sumOfAllCountsWithPreviousWordAndAnyWordAfterIt+=1
    # if sumOfAllCountsWithPreviousWordAndAnyWordAfterIt!=0:
    #     bigram_model_maximum[bigram_key] = numerator/sumOfAllCountsWithPreviousWordAndAnyWordAfterIt

bigram_model_maximum_smoothing = {}
for i in range(len(tokenized_training_unk_splitted)-1):
    bigram_key = tokenized_training_unk_splitted[i] + "," + tokenized_training_unk_splitted[i+1]
    numerator = counts_of_bigram[bigram_key]
    denom = count_of_words[tokenized_training_unk_splitted[i]]
    numerator+=1
    denom += total_number_of_unique_words_in_training#which is the number of unique words in the training set 
    bigram_model_maximum_smoothing[bigram_key] = numerator/denom



# count = 0
# for key in bigram_model_maximum:
#     print ('bigram model without smoothing:' + key + ' ' + str(bigram_model_maximum[key]))
#     count+=1
#     if count == 20:
#         break

# count = 0
# for key in bigram_model_maximum_smoothing:
#     print ('with smoothing' + key + ' ' + str(bigram_model_maximum_smoothing[key]))
#     count+=1
#     if count == 20:
#         break


#What percentage of bigrams (bigram types and bigram tokens) in the test corpus did not occur in
# training (treat <unk> as a regular token that has been observed).
test_text_splitted = unk_replaced_test.split()
bigram_types_test = {}
number_of_bigram_tokens_not_in_training = 0
total_bigrams_in_test = 0
for i in range(len(test_text_splitted)-1):
    bigram_test_key = test_text_splitted[i] + "," + test_text_splitted[i+1]
    # print(bigram_test_key)
    if bigram_types_test.get(bigram_test_key) == None:
        bigram_types_test[bigram_test_key] = 1
    else:
        bigram_types_test[bigram_test_key]+=1
    if counts_of_bigram.get(bigram_test_key) == None:
        number_of_bigram_tokens_not_in_training+=1
    total_bigrams_in_test+=1
print(number_of_bigram_tokens_not_in_training)
print(total_bigrams_in_test)
print("the percentage of bigram tokens that appeared in the test but didn't appear in the training are" + \
    str(number_of_bigram_tokens_not_in_training/total_bigrams_in_test))
#### for the bigram types so im using the bigram types test dictionary since it has all the unique types
bigram_test_types_that_didnt_occur_in_training=0
for k,v in bigram_types_test.items():
    if k not in counts_of_bigram:#counts of bigram is for the training set.
        bigram_test_types_that_didnt_occur_in_training+=1
total_unique_bigrams_in_test = len(bigram_types_test)
print("the percentage of bigram types that appeared in the test but didn't appear in the training are" + \
    str(bigram_test_types_that_didnt_occur_in_training/total_unique_bigrams_in_test))
print(bigram_test_types_that_didnt_occur_in_training)
print(total_unique_bigrams_in_test)
    
#####for unigram maximum likelihood estimation:
#parameters needed: unigram_model are each word so i, look, forward, to, hearing, your , reply , and . 
print("The parameters needed for unigram model predication are each word so i, look, forward, to, hearing, your , reply , and . " )


sentence_to_predict = "I look forward to hearing your reply ."
sentence_to_predict = sentence_to_predict.lower()
sentence_tokenized = sentence_to_predict.split()
uni_probability=1
calculations=""
parameters_0 = []
##log probability for unigram model

for word in sentence_tokenized:
    if unigram_model.get(word) != None:
        uni_probability*=unigram_model[word]
        calculations+=str(unigram_model[word]) + ' * '
    else:
        parameters_0.append(word)
print(calculations + ' = log(' +str(uni_probability) + ")")
print("the log probabilty based on the unigram model is: " + str(math.log(uni_probability,2)))
print("the parameters with 0 probability are below:")
print(parameters_0)


###log probability for bigram model
print("The parameters needed for bigram model predication are each bigram so i look, look forward, forward to, to hearing, hearing your , your reply , reply and, and . " )
parameters_1=[]
bigram_probability=1
for i in range(len(sentence_tokenized)-1):
    bigram = sentence_tokenized[i] + "," + sentence_tokenized[i+1]
    if bigram_model_maximum.get(bigram) != None:
        bigram_probability*=bigram_model_maximum[bigram]
        calculations+=str(bigram_model_maximum[bigram]) + ' * '
    else:
        parameters_1.append(bigram)
print(calculations + ' = log(' +str(bigram_probability) + ")")
print("the log probabilty based on the bigram model is: " + str(math.log(bigram_probability,2)))
print("the parameters for bigram with 0 probability are below:")
print(parameters_0)


###log probability for bigram smoothing model
parameters_2=[]
bigram_smoothing_probability=1
for i in range(len(sentence_tokenized)-1):
    bigram = sentence_tokenized[i] + "," + sentence_tokenized[i+1]
    if bigram_model_maximum_smoothing.get(bigram) != None:
        bigram_smoothing_probability*=bigram_model_maximum_smoothing[bigram]
        calculations+=str(bigram_model_maximum_smoothing[bigram]) + ' * '
    else:
        parameters_1.append(bigram)
print(calculations + ' = log(' +str(bigram_smoothing_probability) + ")")
print("the log probabilty based on the bigram add one smoothing model is: " + str(math.log(bigram_smoothing_probability,2)))
print("the parameters for bigram with add one smoothing with 0 probability are below:")
print(parameters_0)

#lower perplexity corresponds to a better fit of the model
perplexity_sentence_uni = 0
for word in sentence_tokenized:
    if unigram_model.get(word) != None:
        perplexity_sentence_uni += math.log(unigram_model[word],2)
perplexity_sentence_uni/=len(sentence_tokenized)
print(perplexity_sentence_uni)

perplexity_sentence_bigram = 0
for i in range(len(sentence_tokenized)-1):
    bigram = sentence_tokenized[i] + "," + sentence_tokenized[i+1]
    if bigram_model_maximum.get(bigram) != None:
        perplexity_sentence_bigram+=bigram_model_maximum[bigram]
perplexity_sentence_bigram/=(len(sentence_tokenized)-1)
print(perplexity_sentence_bigram)

print("I notice that the perplexity of the sentence under the bigram model is significantly smaller then the perplexity of the sentence under the unigram model")



# print(total_number_of_bigrams)
# total_sum=0
# count=0
# for key in counts_of_bigram:
#     value = counts_of_bigram[key]
#     total_sum += value/total_number_of_bigrams
#     counts_of_bigram[key] = value/total_number_of_bigrams
#     if count == 15:
#         break
#     count+=1
#     print(str(key) + str(counts_of_bigram[key]))
# print(total_sum)#should equal 1
# print(counts_of_bigram)


# #add one smoothing
# counts_of_bigram_add1_smoothing = {}
# # total_number_of_bigrams = total_number_of_bigrams*2
# total_sum = 0
# count = 0
# for key in counts_of_bigram:
#     # count +=1
#     # if count == 50: 
#     #     break
#     value = counts_of_bigram[key]
#     print(key)
#     counts_of_bigram_add1_smoothing[key] = ((value*total_number_of_bigrams) + 1)/(2*total_number_of_bigrams)
#     print(value*total_number_of_bigrams)
#     print(2*total_number_of_bigrams)
#     total_sum += counts_of_bigram_add1_smoothing[key]
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