import json
import re
from datetime import datetime

#check if user exist in database
def checkForUser(db, name:str) -> bool:
    if name in db.keys():
        print("Data retrieved.")
        return True
    else:
        print("Username not found.")
        return False

#create a new user data in database 
def createNewUser(db):
    #Ask for user info for creating a new user data
    username = input("Creating new user data. Enter your username: ")
    weight:float = float(input("Enter your weight (lbs): "))
    DOB = input("Enter your date of birth (mm-dd-yyyy): ")
    DOB_stripped = datetime.strptime(DOB,'%m-%d-%Y') 
    #User's info
    db[str(username)] = {
        "weight": weight,
        "DOB": str(DOB_stripped),
        "caloriesConsumed": [0],
        "dates": [0]
    }
    #Push data into database file
    with open("db.json","w") as db_file:
        json.dump(db,db_file)
    
def recordDailyIntake(db,name:str) -> bool:
    dailyCalorieIntake_arr = db[name]["caloriesConsumed"] #array of daily caloric intake

        

    
    
    