import sys
import mysql.connector
import matplotlib.pyplot as plt
import numpy as np

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
    print(mysql.connector.connect())
    print("test")
    # x = np.linspace(0, 2 * np.pi, 200)
    # y = np.sin(x)

    # fig, ax = plt.subplots()
    # ax.plot(x, y)
    # plt.show()
    xpoints = np.array([0,6])
    ypoints = np.array([0,250])
    plt.plot(xpoints,ypoints)
    plt.show()
    
    mydb = mysql.connector.connect(
        host ="localhost",
        user = "myUser",
        password = "myPassword",
        database = "myDatabase"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SHOW TABLES")
    for x in mycursor:
        print(x)
    