import requests
import json
import pandas as pd

random_cocktail="https://www.thecocktaildb.com/api/json/v1/1/random.php"

data=requests.get(random_cocktail)

dict_random_cocktail=json.loads(data.text)

df=pd.DataFrame(dict_random_cocktail)
print(f"Number of random cocktails: {len(df)}")
list1=[]
for x in range(0,len(df),1):
    list1.append(df["drinks"][x])
df2=pd.DataFrame(list1)
for x in range(0,len(df2),1):
    print(f"Drink name: {df2['strDrink'][x]}")
    print(f"Recipe: {df2['strIngredient1'][x]} {df2['strMeasure1'][x]}, {df2['strIngredient2'][x]}{df2['strMeasure2'][x]}")
    print(f"Recipe Instructions: {df2['strInstructions'][x]}")
   


#cocktail_url = f"www.thecocktaildb.com/api/json/v1/{api_key}/search.php?s={name}"
#cocktail_url = f"https://www.thecocktaildb.com/api/json/v1/1/random.php"

#response = requests.get(cocktail_url)
#print(type(response))
#print(response.status_code)
#
#print(response.text)
#print(type(response.text))
#data = json.loads(response.text)
#print(type(data))
#print(data)

#print(len(data))
#for drink in data:
    #print(drink["strDrink"])


#Welcome message and user inpput cocktail name

#If error, print please try again

#If no error, print recipe and image

