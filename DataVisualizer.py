import matplotlib.pyplot as plt
import numpy as np
import json as json
import DBManager as dbm

def generateGraph(db, name:str) -> bool:
    print("Graph Options: ")
    print("1. Line Graph")
    print("2. Bar Graph")
    print("3. Line + Bar Graph")
    option = int(input("Select option 1, 2, or 3: "))

    # graph data
    xAxis           = dbm.getDates(db, name) # X-Axis of the graph
    yAxis1          = dbm.getWeightsRecorded(db, name)
    yAxis2          = dbm.getDailyCaloricIntake(db, name)

    # graph axis
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()

    # graph colors
    calorieColor = "#eb891a"
    weightColor = "#1dc4b9"

    # graph labels
    title = 'Daily Caloric Intake for ' + name.capitalize()
    fig.suptitle(title)

    ax1.set_xlabel("Date")

    ax1.set_ylabel("Recorded Calorie Intake", color = calorieColor)
    ax1.tick_params(axis="y", labelcolor = calorieColor)

    ax2.set_ylabel("Recorded Weight (lbs)", color = weightColor)
    ax2.tick_params(axis="y", labelcolor = weightColor)

    # other settings
    ax1.grid(True)

    line1 = 0
    line2 = 0
    match option:
        case 1:
            line1 = ax1.plot(xAxis, yAxis1, color = weightColor, marker = 'o', label = "Weight")
            line2 = ax2.plot(xAxis, yAxis2, color = calorieColor, marker = 'o', label = "Calories")
        case 2:
            ax1.bar(xAxis, yAxis1, color = weightColor, width = 1.0)
            ax2.bar(xAxis, yAxis2, color = calorieColor, width = 1.0)
        case 3:
            print()
        case default:
            return False
    
    # combine separate legends
    lns = line1 + line2

    if (lns != 0):
        labs = [l.get_label() for l in lns]
        ax1.legend(lns, labs, loc='upper left')

    plt.show()

    return True