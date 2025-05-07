import requests
import os
import csv

def update_raw_sheets():

    SPREADSHEET_ID = '178o8U97P2cpb0RZbZBvGIoX4bPhUm_lPczg6elfIj9s' #monster hunter community database
    raw_sheet_gids = {
        "Greatsword Crafting Recipes": "1472974674",
        "Sword and Shield Crafting Recipes": "1572658771",
        "Dual Blades Crafting Recipes" : "771597674",
        "Longsword Crafting Recipes": "340864980",
        "Hammer Crafting Recipes": "2010213182",
        "Hunting Horn Crafting Recipes": "1359327010",
        "Lance Crafting Recipes": "321604244",
        "Gunlance Crafting Recipes": "1909151771",
        "Switch Axe Crafting Recipes": "342578461",
        "Charge Blade Crafting Recipes": "99012255",
        "Insect Glaive Crafting Recipes": "2085009326",
        "Bow Crafting Recipes": "795181790",
        "Heavy Bowgun Crafting Recipes": "1342559614",
        "Light Bowgun Crafting Recipes": "904336956",
        "Armor Crafting Recipes": "1357084566",
        "Large Monster Drops": "1288744951",
        "Gatherable Items": "1401660839",
        "Weapon Series": "1118732449",
        "Talisman Crafting Recipes": "1189567904",
        "Talisman Skills": "179350341"
    }


    for name, gid in raw_sheet_gids.items(): #for each item adn key in sheets
        url = f"https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}/export?format=csv&gid={gid}"
        response = requests.get(url)
        
        new_content = response.content #retrieving all content, probably a better way to do this
        
        rawPath = f"MHWildsCSV/rawCSV/{name}.csv" #sets filepath to current sheet name 

            
            
        if os.path.exists(rawPath):
            with open(rawPath, "rb") as f:
                    
                existing_content = f.read() #explicit content check
                    
            if existing_content == new_content: #if theyre the same
                print(f"[{name}] is currently up to date\n")
                
                continue #skip the update step
        else:
            
            with open(f"MHWildsCSV/rawCSV/{name}.csv", "wb") as f:
                f.write(response.content)
                
            
        print(f"Updated: MHWildsCSV/rawCSV/ {name}.csv\n")
    
def update_stat_sheets():
    SPREADSHEET_ID = '178o8U97P2cpb0RZbZBvGIoX4bPhUm_lPczg6elfIj9s' #monster hunter community database


    weapon_stat_gids = {
        "Greatsword Stats" : "431701753",
        "Sword and Shield Stats" : "929045942",
        "Dual Blades Stats" : "1584251007",
        "Longsword Stats" : "1146108654",
        "Hammer Stats" : "594720478",
        "Hunting Horn Stats": "733904683",
        "Lance Stats" : "79978835",
        "Gunlance Stats" : "874092719",
        "Switch Axe Stats" : "337678051",
        "Charge Blade Stats" : "1927088976",
        "Insect Glaive Stats"  :"689340841",
        "Bow Stats" : "2105092355",
        "Heavy Bowgun Stats" : "55061877",
        "Light Bowgun Stats": "103129807"
    }
    for name, gid in weapon_stat_gids.items(): #for each item adn key in sheets
        url = f"https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}/export?format=csv&gid={gid}"
        response = requests.get(url)
        
        new_content = response.content #retrieving all content, still probably a better way to do this
        
        statsPath = f"MHWildsCSV/weaponStats/{name}.csv"
        if os.path.exists(statsPath):
            
            with open(statsPath, "rb") as f:
                    
                existing_content = f.read() #explicit content check
                
            if existing_content == new_content: #if theyre the same
                print(f"[{name}] is currently up to date\n")
                
            continue #skip the update step
        else:
        
            with open(f"MHWildsCSV/weaponStats/{name}.csv", "wb") as f:
                f.write(response.content)
            
            
        print(f"Updated: MHWildsCSV/weaponStats/ {name}.csv\n")

    
print("[Done Checking Content...]\n")
print("[Starting Application...]\n")