import pandas as pd

#%matplotlib inline
import matplotlib.pyplot as plt
#https://github.com/Orestis769/Data_journalism_Orestis_Savvas/blob/main/mathenwwww/countries.csv
df = pd.read_csv('https://raw.githubusercontent.com/Orestis769/Data_journalism_Orestis_Savvas/main/mathenwwww/countries.csv')
#na tis tiposei oles tis grames olh thn lista
df.info()
print(df)
df.columns
df.dtypes
print("The population of the world is: ", df['population'].sum())
print(df.sort_values(by='population', ascending = False).head())

print("apo katv h lista me ta 10 pio poluplithismena xwra: ")
print(df.sort_values(by='population', ascending = False).head(10))
print(df["population"].describe()) 

#df['continent'].value_counts().plot()
print("diagramma apo edw kai katw")
print(df['continent'].value_counts())

print(f" edw einai toyto {df["population"].std()}")
#na ftiaxei png me df['continent'].value_counts().plot()
df['continent'].value_counts().plot(kind='bar')
print(f"edw einai {df['continent'].value_counts().head()}")
plt.title('Number of countries per continent')
plt.xlabel('Continent')
plt.ylabel('Number of countries')
plt.savefig('countries_per_continent.png')