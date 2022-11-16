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
    
    # testData = "data1"
    # testDict = {
    #     "dataset1": [] 
    # }
    # testDict["dataset1"].append(1)
    # print(testDict["dataset1"])
    # # with open("test.json","w") as testFile:
    # #     json.dump(testDict,testFile)

    # with open('test.json','r') as testFile:
    #     data = json.load(testFile)

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
# with open("test2.json","w") as testFile:
#         json.dump(JSON_DATABASE,testFile)
# user = {
#     "name1":"name",
#     "weight":"#lbs",
#     "DOB":"##/##/##",
#     "caloriesConsumed": [], #each element is a different day
#     "Today_date":"##/##/##"    
# }
with open("db.json","r") as db:
    database = json.load(db)

#logging in
username = str(input("Enter your username: "))
if(DBManager.checkForUser(database,username)):
    print("User found!")
else:
    #create a new user data
    DBManager.createNewUser(database)
#Ask for user calorie intake
while not DBManager.recordDailyIntake(database,username):
    print()
