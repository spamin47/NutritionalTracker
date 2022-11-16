import sys
import matplotlib.pyplot as plt
import numpy as np
import json as json
import DBManager
from datetime import datetime
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
    print("Height: " + DBManager.getHeight(database,username))
else:
    #create a new user data
    DBManager.createNewUser(database)
#Ask for user calorie intake
while not DBManager.recordDailyIntake(database,username):
    print()


# # plot given user daily caloric intake
# # define x and y axis points, title of graph
# xAxis = DBManager.getDates(database, username)
# yAxis = DBManager.getDailyCaloricIntake(database, username)
# title = 'Daily Caloric Intake for ' + username.capitalize()

# # plot data as line graph + extra formatting
# plt.plot(xAxis, yAxis, color = 'red', marker = 'o')
# plt.grid(True)
# plt.title(title)
# plt.xlabel('Date')
# plt.ylabel('Calorie Count')
# plt.show()