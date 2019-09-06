#KNN

import pandas as pd
import csv

def get_Data(filename):
    fn=open(filename)
    df=csv.DictReader(fn)
    print(df)
    x=[]
    y=[]
    x_ques=[]
    for row in df:
        if row['moviename'] != '?' :
            x.append([float(row['kicks']),float(row['kisses'])])
            y.append((row['movietype']))
        else:
            x_ques.append(float(row['kicks']))
            x_ques.append(float(row['kisses']))
    print(x_ques)
    return x,y,x_ques


def knn(x,y,x_ques=[90.0,20.0]):
    print(y)
    a=pd.Series([x[i][0] for i in range(len(x))])
    b=pd.Series([x[i][1] for i in range(len(x))])
    l1=((a-x_ques[0])**2 + (b-x_ques[1])**2)**0.5
    indexes=l1.argsort()
    print(indexes)
    k=3
    for i in indexes[:k]:
        l2=[]
        l2.append(y[i])

    if l2.count('Romance')>l2.count('Action'):
        print("Romance")
    else:
        print("Action")
if __name__=='__main__':
    x,y,x_ques=get_Data(filename='LgR_Movies_kNN_classifier.csv')
    knn(x,y)
    knn(x,y,x_ques)