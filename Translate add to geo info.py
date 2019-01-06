import geocoder
import os
import pandas as pd

# read the excel with the address
address = pd.read_excel('The address.xlsx')

#transfer Address column to a list, list value is string
address_tolist = address['Address'].values.tolist()
city_tolist = address['Ship to City'].values.tolist()
listnum = len(address_tolist)

n = 0
latitude = []
longitude = []
city_trans = []

for i in range (listnum):
    g = geocoder.arcgis(address_tolist[i])
    ans = g.latlng
    latitude.append(ans[0])
    longitude.append(ans[1])
    c = geocoder.google(city_tolist[n])
    city_trans.append(c.address)
    n +=1
    #ans is a list

#build a latitude dataframe
latitude_dict = {"Latitude": latitude}
latitude_df = pd.DataFrame(latitude_dict)

#build a longitude dataframe
longitude_dict = {"Longitude": longitude}
longitude_df = pd.DataFrame(longitude_dict)

#build a city dataframe
city_dict = {"Translate City": city_trans}
city_df = pd.DataFrame(city_dict)

#build a final dataframe    
exfinal_dataframe = pd.concat([address, latitude_df ], axis = 1)
final_dataframe = pd.concat([exfinal_dataframe, longitude_df ], axis = 1)
ffinal_dataframe = pd.concat([final_dataframe, city_df ], axis = 1)

#save the info into a new excel
writer = pd.ExcelWriter('Geo and Translation City.xlsx')
ffinal_dataframe.to_excel(writer,'Sheet1')
writer.save()

