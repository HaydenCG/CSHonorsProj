import pandas as pd

armorDF = pd.read_csv("MHWildsCSV\Monster Hunter WildsDataSetCopy - Armour.csv")

def armorSkillLookup(skill, piece):
    skill_columns = ["Skill 1", "Skill 2", "Skill 3"]

    if piece == "": 
        matching_rows = armorDF[   
    armorDF.apply(lambda row: skill in row[skill_columns].values, axis=1)
]
    else:

        matching_rows = armorDF[   
        armorDF.apply(lambda row: skill in row[skill_columns].values and piece == row["Type"], axis=1)
    ]

    selected_columns = ["Index", "Name", "Type", "Skill 1", "Skill 2", "Skill 3", 
                        "Slot 1", "Slot 2", "Slot 3"]
    
    print(matching_rows[selected_columns])
     
    return matching_rows[selected_columns] 


skill = input("[[WHAT ARMOR SKILL?]]")
piece = input("[[WHAT ARMOR PIECE?]]")

armorSkillLookup(skill, piece)
