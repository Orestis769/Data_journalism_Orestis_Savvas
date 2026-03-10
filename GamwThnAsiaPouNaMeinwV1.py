#1 thelw na minw se mia xvra tis asias poy exei panw apo to meso oro life exectensi . pia einai ayth h xwra
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/datajour-gr/Data_journalism/master/week3/countries.csv")
# fitaxe asia_list_xwres
asia_list_xwres = df[df['continent'] == 'Asia'] 

#1 thelw na minw se mia xvra tis asias poy exei panw apo to meso oro life exectensi . pia einai ayth h xwra

asia_list_xwres_new = asia_list_xwres[asia_list_xwres['gdp_per_capita'] > asia_list_xwres['gdp_per_capita'].mean()] 
#apo tis asialistnew the ba minw se auth me to megalitero prosdokimo 

print(asia_list_xwres_new.sort_values(by='life_expectancy', ascending=False).head(3))

#Askisi poies xwres se kafe ypiro einai panw apo to meso ployto tis ypiroy poy anikoyn 
#xeres se kathe ypiro fitaxnw pente listes me kathe ipiro

