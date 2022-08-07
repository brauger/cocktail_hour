import requests
import json
import pandas as pd
import PySimpleGUI as sg

#GUI using PsImpleGUI. Credit to: https://www.geeksforgeeks.org/introduction-to-pysimplegui/

sg.theme('BluePurple')

layout = [[sg.Text('Hello! Welcome to Cocktail Hour What is your name?:'),
		sg.Text(size=(15,1), key='-OUTPUT-')],
		[sg.Input(key='-IN-')],
		[sg.Button('Display'), sg.Button('Exit')]]

window = sg.Window('Introduction', layout)

while True:
	event, values = window.read()
	print(event, values)
	
	if event in (None, 'Exit'):
		break
	
	if event == 'Display':
		# Update the "output" text element
		# to be the value of "input" element
		window['-OUTPUT-'].update(values['-IN-'])

window.close()

#Fetching data. Adapted code from professor's non-alcoholic class example.

random_cocktail="https://www.thecocktaildb.com/api/json/v1/1/random.php"

data=requests.get(random_cocktail)

dict_random_cocktail=json.loads(data.text)

df=pd.DataFrame(dict_random_cocktail)
#print(f"Number of random cocktails: {len(df)}")

#Welcome message and user input

print(f"Hello {values['-IN-']} and welcome to the Cocktail Hour! Would you like to live on the edge and see what new recipe we have in store for you? ")

user = input("Yes or no?")
user = user.lower()


if user in ["no"]:
    print("That's ok. Come back for new cocktail recipes whenever you like!") 
else:
    
    

    #print(f"Number of random cocktails: {len(df)}")
    list1=[]
    for x in range(0,len(df),1):
        list1.append(df["drinks"][x])
    df2=pd.DataFrame(list1)
    for x in range(0,len(df2),1):
    
        print(f"Drink name: {df2['strDrink'][x]}")

        if df2['strIngredient1'][x] is None:
            pass
        elif df2['strMeasure1'][x] is None:
            print(f"{df2['strIngredient1'][x]}")
        else:
            print(f"{df2['strIngredient1'][x]} {df2['strMeasure1'][x]}")
        if df2['strIngredient2'][x] is None:
            pass
        elif df2['strMeasure2'][x] is None:
            print(f"{df2['strIngredient2'][x]}")
        else:  
            print(f"{df2['strIngredient2'][x]} {df2['strMeasure2'][x]}")
        if df2['strIngredient3'][x] is None:
            pass
        elif df2['strMeasure3'][x] is None:
            print(f"{df2['strIngredient3'][x]}")
        else:    
            print(f"{df2['strIngredient3'][x]} {df2['strMeasure3'][x]}")
        if df2['strIngredient4'][x] is None:
            pass
        elif df2['strMeasure4'][x] is None:
            print(f"{df2['strIngredient4'][x]}")
        else:    
            print(f"{df2['strIngredient4'][x]} {df2['strMeasure4'][x]}")
        if df2['strIngredient5'][x] is None:
            pass
        elif df2['strMeasure5'][x] is None:
            print(f"{df2['strIngredient5'][x]}")
        else:     
            print(f"{df2['strIngredient5'][x]} {df2['strMeasure5'][x]}")
        if df2['strIngredient6'][x] is None:
            pass
        elif df2['strMeasure6'][x] is None:
            print(f"{df2['strIngredient6'][x]}")
        else:     
            print(f"{df2['strIngredient6'][x]} {df2['strMeasure6'][x]}")
        if df2['strIngredient7'][x] is None:
            pass
        elif df2['strMeasure7'][x] is None:
            print(f"{df2['strIngredient7'][x]}")
        else:  
            print(f"{df2['strIngredient7'][x]} {df2['strMeasure7'][x]}")
        if df2['strIngredient8'][x] is None:
            pass
        elif df2['strMeasure8'][x] is None:
            print(f"{df2['strIngredient8'][x]}")
        else:   
            print(f"{df2['strIngredient8'][x]} {df2['strMeasure8'][x]}")
        if df2['strIngredient9'][x] is None:
            pass
        elif df2['strMeasure9'][x] is None:
            print(f"{df2['strIngredient9'][x]}")
        else:   
            print(f"{df2['strIngredient9'][x]} {df2['strMeasure9'][x]}")
        if df2['strIngredient10'][x] is None: 
            pass
        elif df2['strMeasure10'][x] is None:
            print(f"{df2['strIngredient10'][x]}")
        else:  
            print(f"{df2['strIngredient10'][x]} {df2['strMeasure10'][x]}")
        if df2['strIngredient11'][x] is None:  
            pass
        elif df2['strMeasure11'][x] is None:
            print(f"{df2['strIngredient11'][x]}")
        else:  
            print(f"{df2['strIngredient11'][x]} {df2['strMeasure11'][x]}")
        if df2['strIngredient12'][x] is None: 
            pass
        elif df2['strMeasure12'][x] is None:
            print(f"{df2['strIngredient12'][x]}")
        else: 
            print(f"{df2['strIngredient12'][x]} {df2['strMeasure12'][x]}")
        if df2['strIngredient13'][x] is None:
            pass
        elif df2['strMeasure13'][x] is None:
            print(f"{df2['strIngredient13'][x]}")
        else:     
            print(f"{df2['strIngredient13'][x]} {df2['strMeasure13'][x]}")
        if df2['strIngredient14'][x] is None:
            pass
        elif df2['strMeasure14'][x] is None:
            print(f"{df2['strIngredient14'][x]}")
        else:
            print(f"{df2['strIngredient14'][x]} {df2['strMeasure14'][x]}")
        if df2['strIngredient15'][x] is None:   
            pass
        elif df2['strMeasure15'][x] is None:
            print(f"{df2['strIngredient15'][x]}")
        else:  
            print(f"{df2['strIngredient15'][x]} {df2['strMeasure15'][x]}")     
    
        print(f"Recipe Instructions: {df2['strInstructions'][x]}")


