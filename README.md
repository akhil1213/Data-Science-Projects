# Natural-Language-Processing
https://www.youtube.com/watch?v=p-XCC0y8eeY
SOFTMAX VID ABOVE

Feature Selection:
Backward elimination : you’re evaluating the model with all of the features and then you pick each feature and remove it once and evaluate how accurate the model is without that feature and keep looping through. 
Forward selection: you start with one feature and then you add every other feature as your 2nd and see which feature leads to a better and accurate model.
Stepwise selection is a combination of above

K-fold cross validation:
Your folding your dataset into k folds  and you use k-1 folds to train and 1 fold to test and you do this k times. each time your fiting your model and then your taking the mean accuracy of all of the combinations. This will be your average accuracy and this helps avoiding overfitting. 
	So now when you test a data, you have k models that your dataset goes into and gets predicted by?

GridSearchCV: 
	hyper parameter tuning, you’re figuring out what parameters to use when training your model. Depending on the classifier/model, each model takes different parameters for example, for Decision Trees you have max depth and for Support vector machines you either have a linear kernel (Straight line)  or a rbf kernel (squiggly line). Grid Search CV also does cross validation with CV = 5 or 10. Grid search returns you ‘best_params” and best accuracy. so it can tell you what your maximum depth should be to fit your model in order to obtain the highest accuracy.

Linear Regression:
	-predicts a continuos number such as the weather or the cost of a house.
	-single linear regression is when you have one independent variable and one dependent variable so one feature and one label. An example of this is calculating the maxtemp given the minimum temperature. 
		-these points of data when training are plotted on the graph so (mintemp,maxtemp) and then linear regression computes the mean of the x values and y values as a starting 	point for the line. this line is computed by minimizing the distance of each point. the line is a straight line in the middle of the data with the minimum distance to all of the training 	points.
		-linear regression returns the coefficient which is the slope and y intercept which is b so you have an equation y = mx+b and now you can plug in ur minimum temp to get a 		predicted maxtemp
		-to evaluate the performance metric you can use mean absolute error, mean squared error or root mean squared error which is just the sum of [(predicted-actual)^2]/n
	Multiple linear regression is when you have multiple independent variables so many features and one label (y).
		-the main difference between single and multiple is that now you have multiple features and each feature has a different slope/weight on how important it is in determining the label. the linear regression algorithm after training returns you the coefficients for each feature and which direction the feature is leaning towards so negative or positive. if its a negative coefficient that means more of that feature will lean toward a smaller y.
	-you can plot your line and scatter plot your training data to see how well your line fitted.

Logistic Regression:
	Similar to linear however it classifies the input(feature vector) into a discrete/finite value e.g [0,1] which would be a binary classifier or even more values such as [0,1,2,3,4..] but the values for y aren’t continuous. We can predict if a passenger in the titanic ship survived or not so y=[survived,died].
	Similar to linear regression as it uses weights for each feature and a bias ( y intercept) and sums it up however this value will not be discrete so logistic regression uses a sigmoid function to convert the value into a probability.
		-we then have a decision boundary which is a threshold and if the y value we receive is 0.7 which is greater then the threshold of 0.5 then the input can be classified in the direction of > 0.5, etc.
	-similar to linear regression we have a cost function(how far your line is from data points that are included in the training set) which we minimize to get the best line when training such that the line is closest to every point in the training set, however, with logistic regression we have discrete values between 0 and 1 which makes it difficult to minimize the cost value. You use gradient descent in logistic regression.

Decision Tree Classifier:
	Has a tree where each root node is a question and this question’s goal is to split the training set such that each child node has the most information gain. 
	-Information gain is calculated using entropy.
		-entropy is how diverse the data is, so if all the data points the same type in that node then the entropy will be 0. entropy is between 0 and 1. The root node so the beginning of the tree the entropy is 1 because your data is the most diverse possible. 
	
After the textual values are encoded to numerical values, we will see some values which will be greater than the other values. Higher values imply they have higher importance. This can lead to our models treating features differently. As an instance, Fashion news type might get a value of 1 and Economical news type might get a value of 10. This makes the machine learning model assume that Economical news type has more importance than Fashion news type.
Solution: We can solve this by using One-Hot Encoding
One Hot Encoding
To prevent some categorical values getting higher importance than the others, we could use the one hot encoding technique before we feed encoded data into our machine learning model.
One hot encoding technique essentially creates a replica (dummy) feature for each distinct value in our target categorical feature. Once the dummy values are created, a boolean (0 or 1) is populated to indicate whether the value is true or false for the feature. As a consequence, we end up get a wide sparse matrix which has 0/1 values populated.
As an instance, if your feature has values “A”, “B” and “C” then three new features (columns) will be created: Feature A, Feature B and Feature C. If first row’s feature value was A then for feature A, you will see 1 and for feature B and C, it will be 0 and so on.


Neural Networks:
	1) pass data to the network using forward propagation. Starting from the input layer, each neuron in the input layer is connected to each neuron in the first hidden layer. Each connection has a weight. The weights are multiplied by the actual inputs and then are summed up and passed to an activation function either relu(max(x,0)), tanh or sigmoid. 
	2) the output layer consists of probabilities for each prediction, so if the model is a multinomial classifier then the output layer contains a neuron. for each class. 
		i.e if it is a hard classification task, then only one class if the correct one and in this case we use a one hot encoded vector. 
	3)We then calculate loss on the output
	4) use Stochastic gradient descent to minimimze the loss by calculating the gradient of the loss function and update weights accordingly using back-propogation.
	5) backpropation uses the derivative of the loss with respect to each weight.

