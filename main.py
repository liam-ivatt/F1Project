import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv

def driver_list(data):
    drivers = data.get("Driver").drop_duplicates()
    print(drivers.to_string(index = False))
    print("Driver count: ", drivers.count())

def average_placement(name, data):

    if name not in data["Driver"].values:
        print("Average Placement Error: Driver not found")
    else:
        driver = data[data["Driver"].str.contains(name)]
        driver = pd.to_numeric(driver["Position"], errors='coerce').mean().round()
        print("Average driver placement is:", driver)

    prompt = input("Average Placement Plot? (y/n): ")

    if prompt == "y":

        driver = data[data["Driver"].str.contains(name)]
        trackpos = driver[["Track", "Position"]]

        plt.xlabel("Track Position")
        plt.ylabel("Race Placement")
        plt.title("Driver's Positions on Different Tracks", fontsize=14)
        fig, ax = plt.subplots()
        plt.xticks(rotation=45, ha="right")
        ax.plot(trackpos["Track"], trackpos["Position"].sort_values())
        plt.show()


def main():
    data = pd.DataFrame(pd.read_csv('2024.csv'))
    driver_list(data)
    average_placement("Max Verstappen", data)

if __name__ == "__main__":
    main()