import sys
import matplotlib.pyplot as plt
import numpy as np
import json as json
import DBManager
from datetime import datetime
import NutritionCalculator
import math
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print("Num of arguments: " + str(len(sys.argv)))
    print("print argument list",str(sys.argv))
    print(sys.executable)
    print("test")
    
    # xpoints = np.array([0,6])
    # ypoints = np.array([0,250])
    # plt.plot(xpoints,ypoints)
    # plt.show()
    
    # # Testing for graphing from Json file with given format(name will change depending on what the user inputs), place after user intake for the day

    # # define x and y axis plot points, turn on grid
    # xAxis = data["john4"]["dates"]
    # yAxis = data["john4"]["caloriesConsumed"]
    # plt.grid(True)

    # # plots dates and calories
    # plt.plot(xAxis, yAxis, color = 'blue', marker = 'o')
    # plt.xlabel('date')
    # plt.ylabel('calories')

    # fig = plt.figure()
    # plt.bar(xAxis, yAxis, color = 'maroon')
    # plt.xlabel('day')
    # plt.ylabel('calories')

    # plt.show()



# # Uncomment to reset database. Make sure to delete database file before hand
# JSON_DATABASE = {
#     "test_user":{ #each element is a different user
#         "weight":"#lbs",
#         "DOB":"##/##/##",
#         "caloriesConsumed": [0], #each element is a different day
#         "dates":[0]    
        
#     } 
# }
# with open("db.json","w") as testFile:
#         json.dump(JSON_DATABASE,testFile)
# user = {
#     "name1":"name",
#     "weight":"#lbs",
#     "DOB":"##/##/##",
#     "caloriesConsumed": [], #each element is a different day
#     "Today_date":"##/##/##"    
# }
with open("db.json","r") as db:
    database:dict = json.load(db)

#logging in
username = str(input("Enter your username: "))
if(DBManager.checkForUser(database,username)):
    print("---Info---")
    print("Sex: "+DBManager.getSex(database,username))
    print("Age: "+ str(DBManager.getAge(database,username)))
    print("Weight: " + str(DBManager.getWeight(database,username)) +"lbs")
    print("Height: " + DBManager.getHeightStr(database,username))
    sex:str = DBManager.getSex(database,username)
    weight:float = DBManager.getWeight(database,username)
    age:int = DBManager.getAge(database,username)
    height_ft = DBManager.getHeight(database,username)[0]
    height_in = DBManager.getHeight(database,username)[1]
    height_ft_in = [height_ft,height_in]
else:
    #create a new user data
    DBManager.createNewUser(database)
    
print("1. Display profile information.")
print("2. Record calories for today.")
print("3. Update weight.")
print("4. My BMR")
option = int(input(""))
match option:
    case 1:
        #Display info
        print("---Info---")
        print("Sex: "+sex)
        print("Age: "+ str(age))
        print("Weight: " + str(weight) +"lbs")
        height_cm:float = NutritionCalculator.HeightToCm(height_ft,height_in)
        print("Height: " + DBManager.getHeightStr(database,username) + " (" +str(height_cm)+ "cm)")
        
    case 2:
        #Ask for user calorie intake
        while not DBManager.recordDailyIntake(database,username):
            print()
    case 3:
        newWeight:float = float(input("New Weight: "))
        DBManager.setWeight(database,username,newWeight)
    case 4:
        if sex == "male":
            print("BMR: " + str(NutritionCalculator.Male_BMR(weight,height_ft_in,age)))
        else:
            print("BMR: " + str(NutritionCalculator.Female_BMR(weight,height_ft_in,age)))  
    case _:
        print("Invalid input")
    


# # plot given user daily caloric intake
# define x and y axis points, title of graph
xAxis = DBManager.getDates(database, username)
yAxis = DBManager.getDailyCaloricIntake(database, username)
title = 'Daily Caloric Intake for ' + username.capitalize()

# plot data as line graph + extra formatting
plt.plot(xAxis, yAxis, color = 'red', marker = 'o')
plt.grid(True)
plt.title(title)
plt.xlabel('Date')
plt.ylabel('Calorie Count')
plt.show()