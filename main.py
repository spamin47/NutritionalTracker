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
    # x = np.linspace(0, 2 * np.pi, 200)
    # y = np.sin(x)

    # fig, ax = plt.subplots()
    # ax.plot(x, y)
    # plt.show()
    
    # xpoints = np.array([0,6])
    # ypoints = np.array([0,250])
    # plt.plot(xpoints,ypoints)
    # plt.show()
    
    testData = "data1"
    testDict = {
        "dataset1": [] 
    }
    testDict["dataset1"].append(1)
    print(testDict["dataset1"])
    # with open("test.json","w") as testFile:
    #     json.dump(testDict,testFile)
        
    with open("test.json","r") as testFile:
        data = json.load(testFile)
    print(data["dataset1"])


JSON_DATABASE = {
    "users":{ #each element is a different user
        "weight":"#lbs",
        "DOB":"##/##/##",
        "caloriesConsumed": [], #each element is a different day
        "dates":[]    
        
    } 
}
user2 = { #each element is a different user
        "weight":"#lbs",
        "DOB":"##/##/##",
        "caloriesConsumed": [], #each element is a different day
        "dates":[]       
    } 
# print(str(JSON_DATABASE["users"][0]["name"]) == str(name))
with open("db.json","w") as testFile:
        json.dump(JSON_DATABASE,testFile)
# user = {
#     "name1":"name",
#     "weight":"#lbs",
#     "DOB":"##/##/##",
#     "caloriesConsumed": [], #each element is a different day
#     "Today_date":"##/##/##"    
# }
with open("db.json","r") as db:
    database = json.load(db)


testDOB = str(input("Type in Date: "))
test = datetime.strptime(testDOB,'%m-%d-%Y')
testDOB2 = str(input("Type in Date: "))
test2 = datetime.strptime(testDOB,'%m-%d-%Y')
print(test == test2)

# username = input("Enter your username: ")
# if(DBManager.checkForUser(database,str(username))):
#     print("User found!")
# else:
#     DBManager.createNewUser(database)
