import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/datajour-gr/Data_journalism/master/week3/countries.csv")

#Askisi poies xwres se kafe ypiro einai panw apo to meso ployto tis ypiroy poy anikoyn 
#pame Asia, Europe, Africa, Oceania, S. America, N. America xwres['gdp_per_capita'] 

#tha kanoyme ena keniourgio column pou tha legetai 'continent_mean' kai tha exei to meso ployto tis kathe ypiroy
df['continent_mean'] = df.groupby('continent')['gdp_per_capita'].transform('mean')
#twra tiponoyme xwres se kafe ypiro einai panw apo to meso ployto tis ypiroy poy anikoyn 
df['above_mean'] = df['gdp_per_capita'] > df['continent_mean']  
#sort to dataframe me vasi to continent kai to gdp_per_capita se katametrisi
df = df.sort_values(by=['continent', 'gdp_per_capita'], ascending=[True, False])
#print to dataframe gia kathe ipiro tis poio ploysies xwres
for continent in df['continent'].unique():
    print(f"Continent: {continent}")
    continent_df = df[df['continent'] == continent]
    above_mean_countries = continent_df[continent_df['above_mean']]
    print(above_mean_countries[['country', 'gdp_per_capita']])
    print("\n")
