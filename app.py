from flask import Flask, jsonify, render_template,request
from sheetUpdate import *
app = Flask(__name__)

@app.route('/')
def hello_world():
    #update_raw_sheets()
    #update_stat_sheets()
    
    return render_template('base.html')


@app.route('/weapon/<weapon_type>') #gets weapon type input from frontend - searches filepath with that type

def get_weapon_data(weapon_type):
    
    
    filepath = f"MHWildsCSV/weaponStats/{weapon_type} Stats.csv"
    


    with open(filepath, newline='', encoding='utf-8') as csvfile:
        rawData = csv.DictReader(csvfile)
        data = list(rawData)
        print(data[0]) #example data for debug, first element in list of weapon dicts
        return jsonify(data)
    
    
@app.route('/weaponSkills/<currentWeapon>')
def get_weapon_skills(currentWeapon):
    skillsList = [] #populate with each unique skill in currentWeapon
    
    

if __name__ == '__main__':
    app.run()