import pandas as pd
import numpy as np


index = ["Berlin", "Madrid", "Rom"]
bevölkerung  = pd.Series(data = [3.6, 3.3, 2.8], index = index)
fläche = pd.Series(data = [892, 604, 1285], index = index)
land = pd.Series(data = ["Deutschland", "Spanien", "Italien"], index = index)
sprache = pd.Series(data = ["deutsch", "spanisch", None], index = index)

my_dict = {
    'Bevölkerung': bevölkerung,
    'Fläche': fläche,
    'Land': land,
    'Sprache': sprache
}





df = pd.DataFrame(my_dict)
print(df)
print()
print()

df.iloc[2,3] = "italienisch"
df.loc["Rom", "Sprache"] = "Lol"
print(df)

index_ny = ["New York"]
bevölkerung_ny  = pd.Series(data = [8.5], index = index_ny)
fläche_ny = pd.Series(data = [784], index = index_ny)
land_ny = pd.Series(data = ["Usa"], index = index_ny)
sprache_ny = pd.Series(data = ["english"], index = index_ny)
                              
my_dict_ny = {
    'Bevölkerung': bevölkerung_ny,
    'Fläche': fläche_ny,
    'Land': land_ny,
    'Sprache': sprache_ny
}

df_ny = pd.DataFrame(my_dict_ny)
print()
print()
print(df_ny)


df_final = pd.concat([df, df_ny])
print()
print()
print(df_final)

#neue spalte
df_final["EU"] = df_final["Land"] != "Usa"
print()
print()
print(df_final)

df_final["Region"] = np.where(df_final["EU"] == True, "Europa", "Americas")
print()
print(df_final)



 

