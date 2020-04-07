
#you don't need both female and male columns and u can have a gender column

# tf.enable_eager_execution()#whenever your prototyping a new model into tensorflow, you need to enable eager execution
#this allows you to write your model in eager while your iterating but you still get the full benefit of tensorflow execution when you train

#load the data in and process the data 
#convert pandas dataframe into a tensorflow dataset

#tensorflow doesn't accept float column values so i convert to int.
X["Fare"] = X["Fare"].astype(int)
X["Age"] = X["Age"].astype(int)
print(X)    

# print(tf.constant(X))
X=tf.convert_to_tensor(
    X, dtype=None, dtype_hint=None, name=None
)
print(X)
# dataset = tf.data.Dataset.from_tensor_slices((X.values, Y.values))
# for feat, targ in dataset.take(5):
#   print ('Features: {}, Target: {}'.format(feat, targ))

# learning_rate = 0.1
# epochs = 50
# batch_size = 100
# batches = 897