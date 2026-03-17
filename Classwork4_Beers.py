import pandas as pd
import matplotlib.pyplot as plt

df= pd.read_csv("https://raw.githubusercontent.com/datajour-gr/Data_journalism/refs/heads/master/week4/craftcans.csv", na_values = ["???", "Unknown", "UNKNOWN"])

"""3 βήματα:

Επιλέξτε την στήλη ABV
Αφαιρέστε το σύμβολο % (βοήθεια μετατρέψτε το σε κενό)
Μετατρέψτε την στήλη τώρα σε float
Μπορείτε να την σώσετε με ένα νέο column ή στο ίδι"""


#me mia grami auto upologizei to meso oro twn IBUs gia ta 24 oz
filtered_df = df[df['Size'] == '24 oz'] 
#mesos oros ana perioxi 
filtered_df = df[df['Size'] == '24 oz.']
#mean_ibu = filtered_df.groupby("Location")['IBUs'].mean() ascending = False
mean_ibu = filtered_df.groupby("Location")['IBUs'].mean().sort_values(ascending=False)

print(mean_ibu)

#tiposa ta vall gia Supper Club Lager
supper_club_lager = df[df['Beer'] == 'Supper Club Lager']
print(f"supper club lager: {supper_club_lager}")

#poses grames exoyn misin vuales apo oli tin lista na_values = ["???", "Unknown", "UNKNOWN"])
#otan xrisimopoioume to na_values, to pandas tha metatrepsei ta values pou exoyn auto to string se NaN, opote mporoume na ypologisoume posa NaN yparxoun se kathe stili me tin methodo isin kai sum
missing_values_count = df.isin(["NaN"]).sum()
print(f"Missing values count:\n{missing_values_count}")

#me to in null
missing_values_count = df.isnull().sum()
print(f"Missing values count:\n{missing_values_count}")
#sort tin list me to ABV se ayxousa seira

#tria idoi biras StyleNew = df[df['Style'] me sinthiki == anagastika me == (beers)] kai meta sort ana xwra 
# Witbier", "Hefeweizen", "American Pale Wheat Ale
#filtered_df = df[df['Style'] == "Witbier"] or df[df['Style'] == "Hefeweizen"] or df[df['Style'] == "American Pale Wheat Ale"]
