import json
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
    try:
        caloriesRecorded = float(input("Calories: ")) #Ask for calories consumed
    except:
        print("Invalid input. Please enter a valid value.")
        return False

    dailyCalorieIntake_arr = db[name]["caloriesConsumed"] #array of daily caloric intake
    datesRecorded_arr = db[name]["dates"] #array of dates recorded
    
    #if today's date is still the same as the previous recorded date, then just add to today's calorie count
    #else append a new date and calories element for today's date
    if(datesRecorded_arr[-1] == datetime.today().strftime("%m/%d/%Y")): # Date format: (mm/dd/yyyy)
        dailyCalorieIntake_arr[-1] += caloriesRecorded
    else:
        #add a try method here to check if value is a number or not
        dailyCalorieIntake_arr.append(caloriesRecorded)
        datesRecorded_arr.append(datetime.today().strftime("%m/%d/%Y")) # Date format: (mm/dd/yyyy)
        
    #Push data into database file
    with open("db.json","w") as db_file:
        json.dump(db,db_file)
    print("Calories successfully recorded!")
    return True

def getDailyCaloricIntake(db,name:str) -> list:
    return db[name]["caloriesConsumed"]
        
    

        

    
    
    