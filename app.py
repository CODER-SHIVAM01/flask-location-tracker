# -------------------------------------- FLask Using---------------------------------
from flask import Flask,render_template,request
import requests
import datetime
import json
import os
app=Flask(__name__)
@app.route("/")
def home():
    # return "Hello! Flask is Working"
    return render_template("index.html")
# @app.route("/about")
# def about():
@app.route("/data")
def show_data():
    try:
        with open('Location.txt',"r") as f:
            content=f.read()
    except FileNotFoundError:
        content="Not Data Found Yet."
    return"<pre>" + content + "<pre>"
        
@app.route("/collect",methods=["POST"])
def collect():
    data=request.get_json(silent=True)

    if not data:
        return {"error": "No JSON received"}, 400
    
    lat=data["lat"]
    lon=data["lon"]
    name=data["name"]

    if not lat or not lon:
        return {"error": "Missing coordinates"}, 400
    
    # REVERSE GEOCODING API
    url=f"https://nominatim.openstreetmap.org/reverse?format=json&lat={lat}&lon={lon}"
    headers={
        "User-Agent":"FlaskLocationApp"
    }
    try:
        response = requests.get(url, headers=headers)
        address = response.json().get("display_name", "Address not found")
    except Exception as e:
        print("Geocoding error:", e)
        address = "Address lookup failed"

    # response=requests.get(url,headers=headers)
    # address=response.json().get("display_name","Address not found")
    # print('Address :',address)
    # data["time"]=str(datetime.datetime.now().strftime("%d-%m-%Y %I:%M %p")) #02-02-2026 8:56 PM 
    data["time"]=str(datetime.datetime.now().strftime("%d %b %Y , %I:%M %p")) #02 Feb 2026 , 8:56 PM 
    with open('Location.txt',"a")as f:
        f.write(json.dumps(data,name)+ "\n")
        print("Saved ")
    return {
        "Status": "Location Saved",
        'address':address}

if __name__=="__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
    # app.run(debug=True)
    # app.run(host="0.0.0.0", port=5000)

