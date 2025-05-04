#what to look up:
    #Monster given a material
    
import pandas as pd

def monsterDropLookup(item): #returns rows where item matches
    
    dropDF = pd.read_csv("MHWildsCSV//Large Monster Drops.csv")
    #print(df.iloc[0])  # Access first row
            

    #perform lookup on that object
    dropColumnName = "Item"

    matching_rows = dropDF[dropDF[dropColumnName] == item] #try here, if not found, call nonDrop
    
    if matching_rows.empty:
        matching_rows = nonMonsterDropLookup(item) #if not in monsterDrops -> sends to nonMonster LU
    
    return matching_rows
    #print(matching_rows["Monster"] + " | " + matching_rows["Monster ID"]) #returns name and ID


def nonMonsterDropLookup(item):#returns non monster part in case of monster drop failure
    
    itemDF = pd.read_csv("MHWildsCSV/Gatherable Items.csv")
    itemColumnName = "Name"
    
    matching_rows = itemDF[itemDF[itemColumnName] == item] #if item in Name == item
    if matching_rows.empty:
        matching_rows = None

    return matching_rows


        