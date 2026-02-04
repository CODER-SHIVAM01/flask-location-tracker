# -------------------------------------- FLask Using---------------------------------
from flask import Flask,render_template,request
import requests
import datetime
import json
app=Flask(__name__)
@app.route("/")
def home():
    return "Hello! Flask is Working"
@app.route("/about")
def about():
    return render_template("index.html")
@app.route("/collect",methods=["POST"])
def collect():
    data=request.get_json(silent=True)
    lat=data["lat"]
    lon=data["lon"]
    # REVERSE GEOCODING API
    url=f"https://nominatim.openstreetmap.org/reverse?format=json&lat={lat}&lon={lon}"
    headers={
        "User-Agent":"FlaskLocationApp"
    }
    response=requests.get(url,headers=headers)
    address=response.json().get("display_name","Address not found")
    print('Address :',address)
    # data["time"]=str(datetime.datetime.now().strftime("%d-%m-%Y %I:%M %p")) #02-02-2026 8:56 PM 
    data["time"]=str(datetime.datetime.now().strftime("%d %b %Y , %I:%M %p")) #02 Feb 2026 , 8:56 PM 
    with open('Location.txt',"a")as f:
        f.write(json.dumps(data)+ "\n")
        print("Saved ")
    return {
        "Status": "Location Saved",
        'address':address}
if __name__=="__main__":
    # app.run(debug=True)
     app.run(host="0.0.0.0", port=5000)

