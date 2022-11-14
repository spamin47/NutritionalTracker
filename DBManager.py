import json
import re
from datetime import datetime

    
def checkForUser(db, name:str) -> bool:
    if name in db.keys():
        print("Data retrieved.")
        return True
    else:
        print("Username not found.")
        return False
    
def createNewUser(db):
    username = input("Creating new user data. Enter your username: ")
    weight:float = float(input("Enter your weight (lbs): "))
    
    
    
    DOB = input("Enter your date of birth (mm-dd-yyyy): ")
    datestripped = datetime.strptime(DOB,'%m-%d-%Y')
    db[str(username)] = {
        "weight": weight,
        "DOB": datestripped,
        "caloriesConsumed": [],
        "dates": []
    }
    with open("db.json","w") as db_file:
        json.dump(db,db_file)
    
# def recordCalorie():
    