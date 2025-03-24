import pandas as pd
from relationalLookup import *
#Prompt UI for weapon by name
#Find method to efficiently look up weapon type first

def weaponMaterialLookup(weapon):
    weaponDF = pd.read_csv("MHWildsCSV\Monster Hunter WildsDataSetCopy - Great Sword Recipes.csv")

    column_name = "Name"

    matching_rows = weaponDF[weaponDF[column_name] == weapon] #finds matching columns where item occurs
    

    #turn into formatted for loop
    print(monsterDropLookup(matching_rows["Item 1"].iloc[0])) #returns name and ID
    print(monsterDropLookup(matching_rows["Item 2"].iloc[0])) #returns name and ID
    print(monsterDropLookup(matching_rows["Item 3"].iloc[0])) #returns name and ID
    print(monsterDropLookup(matching_rows["Item 4"].iloc[0])) #returns name and ID

    
    
    #find items for weapon
    #run monsterDropLookup on items
    #for testing, return names of all monsters required
desiredWeapon = input("[[INPUT DESIRED GREATSWORD]]\n")

weaponMaterialLookup(desiredWeapon)
