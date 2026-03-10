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
#xwres se kathe ypiro fitaxnw pente listes me kathe ipiro 
#Askisi poies xwres se kafe ypiro einai panw apo to meso ployto tis ypiroy poy anikoyn , kai to arhisma ton xwron ana ipiro se grafima
asia_list_xwres = df[df['continent'] == 'Asia'] 
eyropi_list_xwres = df[df['continent'] == 'Europe']
afriki_list_xwres = df[df['continent'] == 'Africa'] 
australia_list_xwres = df[df['continent'] == 'Oceania']
ameriki_S_America = df[df['continent'] == 'S. America']	
ameriki_N_America = df[df['continent'] == 'N. America']

#se ena data frame ta asia ktlp tis xwres se kathe ypiro
#na enosw kai ta 6 mazi ta onomata ton ypirwn 
#OlesOiXwres_data_frame = df[df['continent'].isin(['Asia', 'Europe', 'Africa', 'Oceania', 'S. America', 'N. America'])] 



asia_list_xwres_new = asia_list_xwres[asia_list_xwres['gdp_per_capita'] > asia_list_xwres['gdp_per_capita'].mean()]
eyropi_list_xwres_new = eyropi_list_xwres[eyropi_list_xwres['gdp_per_capita'] > eyropi_list_xwres['gdp_per_capita'].mean()]
afriki_list_xwres_new = afriki_list_xwres[afriki_list_xwres['gdp_per_capita'] > afriki_list_xwres['gdp_per_capita'].mean()]
australia_list_xwres_new = australia_list_xwres[australia_list_xwres['gdp_per_capita'] > australia_list_xwres['gdp_per_capita'].mean()]
ameriki_S_America_new = ameriki_S_America[ameriki_S_America['gdp_per_capita'] > ameriki_S_America['gdp_per_capita'].mean()]
ameriki_N_America_new = ameriki_N_America[ameriki_N_America['gdp_per_capita'] > ameriki_N_America['gdp_per_capita'].mean()]

sorted_asia = asia_list_xwres_new.sort_values(by='gdp_per_capita', ascending=False)    
sorted_eyropi = eyropi_list_xwres_new.sort_values(by='gdp_per_capita', ascending=False)    
sorted_afriki = afriki_list_xwres_new.sort_values(by='gdp_per_capita', ascending=False)
sorted_australia = australia_list_xwres_new.sort_values(by='gdp_per_capita', ascending=False)
sorted_amerika_S_America = ameriki_S_America_new.sort_values(by='gdp_per_capita', ascending=False)
sorted_amerika_N_America = ameriki_N_America_new.sort_values(by='gdp_per_capita', ascending=False)

#twra me groupby na kanw ameriki_N_America['gdp_per_capita'] > ameriki_N_America['gdp_per_capita'].mean()] se kathe xwra


print(f"asia xwres: {asia_list_xwres_new['country'].tolist()[:3]} \n eyropi xwres: {eyropi_list_xwres_new['country'].tolist()[:3]} \n afriki xwres: {afriki_list_xwres_new['country'].tolist()[:3]} \n amerika S. America xwres: {ameriki_S_America_new['country'].tolist()[:3]} \n amerika N. America xwres: {ameriki_N_America_new['country'].tolist()[:3]} \n australia xwres: {australia_list_xwres_new['country'].tolist()[:3]}")
#print(f"oi xwres se kathe ypiro pou exoun panw apo to meso ployto tous einai: {asia_list_xwres_new['country'].tolist()} se Asia, {eyropi_list_xwres_new['country'].tolist()} se Europe, {afriki_list_xwres_new['country'].tolist()} se Africa, {amerika_list_xwres_new['country'].tolist()} se Americas, {australia_list_xwres_new['country'].tolist()} se Oceania  ")
print(f"sorted oi ypiri kai i xwres {sorted_asia['country'].tolist()[:3]} se Asia, {sorted_eyropi['country'].tolist()[:3]} se Europe, {sorted_afriki['country'].tolist()[:3]} se Africa, {sorted_amerika_S_America['country'].tolist()[:3]} se S. America, {sorted_amerika_N_America['country'].tolist()[:3]} se N. America, {sorted_australia['country'].tolist()[:3]} se Oceania  ")
#na bgalei to parapano se lista  .head(3) amkeriki N. America	S. America	
#print(f"asia xwres: {asia_list_xwres_new['country'].tolist()[:3]} \n eyropi xwres: {eyropi_list_xwres_new['country'].tolist()[:3]} \n afriki xwres: {afriki_list_xwres_new['country'].tolist()[:3]} \n amerika xwres: {amerika_list_xwres_new['country'].tolist()[:3]} \n australia xwres: {australia_list_xwres_new['country'].tolist()[:3]}")


print("Asia: ", len(asia_list_xwres_new))
print("Europe: ", len(eyropi_list_xwres_new))
print("Africa: ", len(afriki_list_xwres_new))
print("Oceania: ", len(australia_list_xwres_new))
print("S. America: ", len(ameriki_S_America_new))


