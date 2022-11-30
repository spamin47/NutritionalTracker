import json
from datetime import datetime
from dateutil.relativedelta import relativedelta

#check if user exist in database
def checkForUser(db, name:str) -> bool:
    if name in db.keys():
        # print("Data retrieved.")
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
     
    sexValid:bool = True 
    while sexValid:
        sex = str(input("What is your sex (male|female)? ")).lower()
        if(sex == "m" or sex == "male" or sex == "girl"):
            sex = "male"
            sexValid = False
        elif(sex == "f" or sex == "female" or sex == "boy"):
            sex = "female"
            sexValid = False   
    height_ft = int(input("Height (ft) "))
    height_in = int(input("Height (in) "))
    
    #User's info
    db[str(username)] = {
        "weight": weight,
        "weightsRecorded": [0],
        "DOB": str(DOB_stripped),
        "sex": sex,
        "height": [height_ft,height_in],
        "caloriesConsumed": [0],
        "dates": [0]
    }
    #Push data into database file
    with open("db.json","w") as db_file:
        json.dump(db,db_file)

#Record daily calorie intake into an array and save it into database
def recordDailyIntake(db,name:str) -> bool:
    try:
        caloriesRecorded = float(input("Calories: ")) #Ask for calories consumed
    except:
        print("Invalid input. Please enter a valid value.")
        
        #Ask if user wants to retry entering in calories
        retry = str(input("Re enter input? ")).lower()
        if (retry == "yes" or retry == "y" or retry == 1):
            return False
        
        return True

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

# record current weight into weight records
def recordCurrentWeight(db, name:str):
    currentWeight       = db[name]["weight"] # current recorded weight value
    datesRecorded_arr   = db[name]["dates"] # array of dates recorded
    weightsRecorded     = db[name]["weightsRecorded"] # array of weights recorded

    if(datesRecorded_arr[-1] == datetime.today().strftime("%m/%d/%Y")): # Date format: (mm/dd/yyyy)
        weightsRecorded[-1] = currentWeight
    else:
        #add a try method here to check if value is a number or not
        weightsRecorded.append(currentWeight)

#SETTER METHODS
def setWeight(db:dict,name:str,new_weight:float):
    db[name]["weight"] = new_weight
    #Push data into database file
    with open("db.json","w") as db_file:
        json.dump(db,db_file)
    

#GETTER METHODS
# returns list of daily caloric intake
def getDailyCaloricIntake(db,name:str) -> list:
    return db[name]["caloriesConsumed"]

# returns list of dates
def getDates(db, name:str) -> list:
    return db[name]["dates"]

#return sex
def getSex(db,name:str) -> str:
    return db[name]["sex"]

#return string of height _ft _in
def getHeight(db,name:str)-> str:
    return str(db[name]["height"][0]) + "ft " + str(db[name]["height"][1]) + "in"

#return DOB
def getDOB(db,name:str) -> list:
    dateOfBirth = db[name]["DOB"].split(' ')
    dateOfBirth = dateOfBirth[0].split('-')
    return dateOfBirth

def getWeight(db,name:str)->float:
    return db[name]["weight"]

#calculate age using DOB and today's date
def getAge(db,name:str) -> int:
    dob = getDOB(db,name) #['year','month','day']
    dob = datetime(int(dob[0]),int(dob[1]),int(dob[2]),0,0,0,0)
    now = datetime.now()
    return int(relativedelta(now,dob).years)

def getWeightsRecorded(db, name:str) -> list:
    return db[name]["weightsRecorded"]