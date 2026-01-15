import pandas as pd
from models import Terrorist


def choosing_5_terrorists(file):
    df = pd.read_csv(file)
    df.sort_values(by="danger_rate", ascending=False)
    df_danger = df.head()
    df_danger = df_danger[["name", "location","danger_rate"]]
    return df_danger






