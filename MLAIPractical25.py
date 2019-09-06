import pandas as pd
import matplotlib.pyplot as plt

from sklearn import linear_model

import warnings
warnings.filterwarnings(action="ignore")


#Function to get data
def get_data(file_name):
  dataframe = pd.read_csv(file_name)
  print(dataframe)
  x_parameters =[]
  y_parameters =[]
  for single_square_feet , single_price_value in zip(
    dataframe['square_feet'], dataframe['price']):
    x_parameters.append([float(single_square_feet)])
    y_parameters.append(float(single_price_value))

  return x_parameters,y_parameters


def linear_model_main(X_parameters, Y_parameters, predict_value):
    regr = linear_model.LinearRegression()
    print("AREA : ", X_parameters )
    print("PRICE :", Y_parameters)
    regr.fit(X_parameters,Y_parameters) #calc hypothesis variable
    predict_outcome = regr.predict([[predict_value]])
    predictions = {}
    predictions['coefficient'] = regr.coef_
    predictions['intercept'] = regr.intercept_
    predictions['predicted_value'] = predict_outcome

    print("Output from machine = " , predict_outcome)

    plt.scatter(X_parameters, Y_parameters, color="m",
                marker= "o", s=30)

    all_predicted_Y = regr.predict(X_parameters)
    plt.scatter(X_parameters, all_predicted_Y,color="b")
    plt.plot(X_parameters,all_predicted_Y, color="r")
    plt.scatter(predict_value, predict_outcome, color="g")
    plt.show()
    return predictions

if __name__ == "__main__":
    x,y = get_data('LR_House_price.csv')
    predict_value = 700
    result = linear_model_main(x,y,predict_value)
    print("Intercept value " ,result['intercept'])
    print("coefficient ", result['coefficient'])
    print("Predicted House Price value: ", result['predicted_value'])
