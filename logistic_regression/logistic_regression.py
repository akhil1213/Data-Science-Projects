import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as pyplot
import math
import tensorflow as tf
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

class Learn_Titanic_Data:
    def __init__(self):
        titanic_data = pd.read_csv("train.csv")
        titanic_data.head(10)
        print(titanic_data.shape)
        # #analyze the data
        # sns.countplot(x="Survived", data=titanic_data)
        # pyplot.savefig("survivedplot")
        # #there are 350 passengers who survived and 869-350 passengers that died.
        # #there are less surviivals then non-survivals

        # sns.countplot(x="Survived",hue = "Sex",data=titanic_data)
        # pyplot.savefig("survived_females_vs_males")
        # #mostly females survived, and males died. 

        # sns.countplot(x="Survived",hue = "Pclass",data=titanic_data)
        # pyplot.savefig("class_surival_rate")
        # #the most deaths occured for passengers who travelled in class 3
        # #more passengers who survived belong to class 1 and 2 then class 3

        # sns.countplot(x="Age", data = titanic_data)
        # pyplot.savefig("age_distribution")

        # titanic_data["Age"].plot.hist(bins=10)
        # pyplot.savefig("age_distribution")
        #more young passengers then older

        # titanic_data["Fare"].plot.hist(bins=20)
        # pyplot.savefig("faresize")

        #more passengers paid a cheap price for the fare.
        print(titanic_data.info())

        # sns.countplot(x="Survived",hue = "SibSp",data=titanic_data)
        # pyplot.savefig("survived_with_siblings_or_spouses")

        #no point on analyzing survived with siblings or not because most passengers had no spouses or siblings boarding the ship

        #you use a histogram when you want to count between a range of x values.
        # sns.countplot(x="SibSp",data=titanic_data)
        # pyplot.savefig("sibling-spousecounts")

        # sns.countplot(x="Parch",data=titanic_data)
        # pyplot.savefig("parents-children_counts")
        #no point on analyzing parent-children-counts because most people on board had no parent or children with them
        self.clean_data(titanic_data)

    ####clean the data
    def clean_data(self,titanic_data):
        # print(titanic_data.isnull())
        #cabin columns have a lot of null values
        # print(titanic_data.isnull().sum())
        #177 missing values for age, and 687 missing values for the cabin column

        # sns.boxplot(x="Pclass", y="Age",data=titanic_data)
        # pyplot.savefig("age_in_each_class")
        #age is older in class 1 and in class 2 then class 3
        #older people can afford to pay more money and like travelling in higher classes.

        titanic_data.drop('Cabin',axis=1, inplace=True)
        print(titanic_data.head(5))
        #The dropna() function is used to remove missing values. Determine if rows or columns which contain missing values are removed. 0, or 'index' : Drop rows which contain missing values.
        titanic_data.dropna(inplace=True)
        #you can also replace na values 
        print(titanic_data.isnull().sum())

        print(pd.get_dummies(titanic_data["Embarked"]))
        embarked = pd.get_dummies(titanic_data["Embarked"],drop_first = True)

        sex = pd.get_dummies(titanic_data["Sex"],drop_first = True)
        print(sex)
        #sex has two columns, 0 for male and 1 for female but we only need one column, so if we have male and thats 0 then obviously its a female.
        pcl = pd.get_dummies(titanic_data["Pclass"],drop_first=True)
        print(pcl)
        #pclass has three values 1,2,3 but if 2 is 0 and 3 is 0 then we know the person embarked in class 1 so we dont need the first column.
        titanic_data = pd.concat([titanic_data,sex,pcl,embarked],axis=1)
        #when your adding columns you use axis = 1


        titanic_data.drop(['PassengerId', 'SibSp', 'Parch', 'Ticket', 'Name','Pclass','Embarked','Sex'],axis=1, inplace=True)


        X = titanic_data.drop("Survived",axis=1)
        Y = titanic_data["Survived"]

        self.train_model(X,Y)
    def train_model(self,X,Y):
        print(X.shape)
        print(Y.shape)
        x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=0)
        print(x_train.shape)
        print(y_train.shape)

        logisticRegr = LogisticRegression()
        logisticRegr.fit(x_train,y_train)

        predictions = logisticRegr.predict(x_test)

        # False positives are cases the model incorrectly labels as positive that are actually negative, or in our example, individuals the model classifies
        #  as terrorists that are not. While recall expresses the ability to find all relevant instances in a dataset, precision expresses the proportion of the data
        #   points our model says was relevant actually were relevant.

        from sklearn.metrics import classification_report
        print(classification_report(y_test, predictions))

        from sklearn.metrics import confusion_matrix
        cm = confusion_matrix(y_test,predictions)
        #confusion matrix is a 2x2 matrix showing how accurate your model was trained
        #its a 2x2 matrix like this
        #     models predictions: survived died
        # actual           
        # survived                108      17
        # died                     26     63

        #to compute the accuracy its simple
        true_negative = cm[0][0]
        true_positive = cm[1][1]
        false_negative = cm[0][1]#died but actually survived
        false_positive = cm[1][0]

        accuracy = (true_positive + true_negative)/(true_positive + true_negative + false_positive + false_negative)

        from sklearn.metrics import accuracy_score
        print(accuracy_score(y_test,predictions))

        print(accuracy)
Learn_Titanic_Data()