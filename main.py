import pandas as pd
import matplotlib.pyplot as plt
import csv

#drivers = pd.DataFrame([],[])

F12024 = pd.DataFrame(pd.read_csv('2024.csv'))

drivers = F12024.get("Driver",).drop_duplicates()

