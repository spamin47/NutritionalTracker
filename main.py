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
        
    # with open("test.json","r") as testFile:
    #     data = json.load(testFile)
    # print(data["dataset1"])

## Uncomment to reset database. Make sure to delete database file before hand
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
    database = json.load(db)

username = str(input("Enter your username: "))
if(DBManager.checkForUser(database,username)):
    print("User found!")
else:
    DBManager.createNewUser(database)
    
while not DBManager.recordDailyIntake(database,username):
    print()
