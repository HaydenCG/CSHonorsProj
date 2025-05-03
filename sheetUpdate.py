import requests
import os

SPREADSHEET_ID = '178o8U97P2cpb0RZbZBvGIoX4bPhUm_lPczg6elfIj9s'
sheet_gids = {
    "Greatsword Crafting Recipes": "1472974674",
    "Sword and Shield Crafting Recipes": "1572658771",
    "Dual Blades Crafting Recipes" : "771597674",
    "Long Sword Crafting Recipes": "340864980",
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
    "Armor Crafting Recipes": "1357084566"
}

os.makedirs("MHWildsCSV", exist_ok=True)

for name, gid in sheet_gids.items():
    url = f"https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}/export?format=csv&gid={gid}"
    response = requests.get(url)
    
    
    
    new_content = response.content
    
    filepath = f"MHWildsCSV/{name}.csv" #sets filepath to current sheet name 

    if os.path.exists(filepath): #check existence
        
        with open(filepath, "rb") as f:
            
            existing_content = f.read()
            
        if existing_content == new_content: #if theyre the same
            print(f"[{name}] is currently up to date\n")
            continue #skip the update step
    
    with open(f"MHWildsCSV/{name}.csv", "wb") as f:
        f.write(response.content)
    print(f"Updated: MHWildsCSV/{name}.csv")
    
print("Done Checking Content!")
print("[Starting Application...]")