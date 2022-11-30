import matplotlib.pyplot as plt
import numpy as np
import json as json
import DBManager as dbm

# generates graph to visualize progress/trends in weight and caloric intake 
def generateGraph(db, name:str) -> bool:
    # user input prompts 
    print("Graph Options: ")
    print("1. Line Graph")
    print("2. Bar Graph")
    print("3. Line + Bar Graph")
    print("4. Check Progress Towards Calorie Goal")
    option = int(input("Select option 1, 2, 3, or 4: "))
    
    # graph
    xAxis           = dbm.getDates(db, name) # x-Axis of the graph
    yAxis1          = dbm.getDailyCaloricIntake(db, name) # calories
    yAxis2          = dbm.getWeightsRecorded(db, name) # weights
    calorieColor    = "#eb891a" # HEX for calories on graph
    weightColor     = "#1dc4b9" # HEX for weight on graph
    alphaVal        = 0.7 # alpha value for graph transparency(if graphs overlap)
    fig = plt.figure() # graph stuff

    # graph axes: ax1 = calories, ax2 = weight.
    ax1 = plt.subplot(1, 1, 1) 
    ax2 = ax1.twinx() # ax2 shares the same x-axis as ax1

    w = 0.25 # bar width
    x = np.arange(len(xAxis)) # x ticks 
    plt.xticks(x, xAxis) # label x ticks with dates


    # switch statements determines which graph type to generate
    match option:
        case 1:
            # dual axis bar graph: calories = calorie graph, weight = weight graph
            # calories positioned to the left of tick mark, weight positioned to the right
            calories    = ax1.bar(x - w/2, yAxis1, color = calorieColor, width = w, align = 'center', label = "Calories")
            weight      = ax2.bar(x + w/2, yAxis2, color = weightColor, width = w, align = 'center', label = "Weight(lbs)")
            # label bars with values
            ax1.bar_label(calories, padding = 1)
            ax2.bar_label(weight, padding = 1)
        case 2:
            # dual axis line graph
            solid       = (0, (10, 0)) # solid linestyle 
            dashed      = (0, (10, 6)) # dashed linestyle 
            calories    = ax1.plot(x, yAxis1, linestyle = solid, color = calorieColor, marker = 'o', label = "Calories", alpha = alphaVal)
            weight      = ax2.plot(x, yAxis2, linestyle = dashed, color = weightColor, marker = 'v', label = "Weight(lbs)", alpha = alphaVal)
        case 3:
            # dual axis line + bar graph
            calories    = ax1.plot(x, yAxis2, color = calorieColor, marker = 'o', label = "Calorie", alpha = alphaVal)
            weight      = ax2.bar(x, yAxis1, color = weightColor, width = w, align = 'center', label = "Weight(lbs)", alpha = alphaVal)
        case 4:
            # check progress towards calorie goal: graphs recorded daily caloric intake and compares with target caloric intake
            print("not implemented yet")
        case _:
            print("invalid input")
            return False

    # After graphing, setup graph labels
    title = 'Calorie Intake & Weight for ' + name.capitalize() # title
    plt.title(title)
    ax1.set_xlabel("Date") # X axis = date

    ax1.set_ylabel("Recorded Calorie Intake", color = calorieColor)
    ax1.tick_params(axis="y", labelcolor = calorieColor)

    ax2.set_ylabel("Recorded Weights (lbs)", color = weightColor)
    ax2.tick_params(axis="y", labelcolor = weightColor)
    
    # display graph with legend and grid
    fig.legend(loc="upper left", bbox_to_anchor=(0,1), bbox_transform=ax1.transAxes)
    plt.grid(True)
    plt.show()

    # returns true if graph generated sucessfully
    return True