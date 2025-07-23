from data_loader2 import data_loader
import pandas as pd

df = data_loader("Titanic.csv")

df.to_csv("Cleaned Titanic data")