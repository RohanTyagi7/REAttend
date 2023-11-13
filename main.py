from flask import Flask
from flask import request
import pyqrcode 
import png 
from pyqrcode import QRCode 
import base64
import socket
import geocoder
import datetime
import random
import data
import json

app = Flask(__name__)

@app.route('/')
def index():
  return('400')

@app.route('/create-new-qr/')
def qr():
  text = request.args.get('key')
  if text == "JhbukJGYuukbhj":
      hostname = socket.gethostname()
      IPAddr = socket.gethostbyname(hostname)
      rand = round(random.random()*2000+1)
      d = str(datetime.datetime.now())
      url = pyqrcode.create("https://reattend-real.rt123.repl.co/attend/?date=" + str(d[0:d.index(" ")]) + "&key1=" + str(rand) + "&key2=" + "new" + str(rand%2) + "&key3=" + str(rand%57))
      x = url.png('qrcode.png', scale = 6)
      z = "data:image/png;base64," + base64.b64encode(open("qrcode.png", "rb").read()).decode()
      g = geocoder.ip('me')
      print(g.latlng)
      return ('<script>alert("YOUR PERSONAL DATA HAS BEEN SHARED WITH THE SITE OWNER: Your IP Address \'' + IPAddr + '\', hostname \'' + hostname + '\', and physical location \'(' + str(g.latlng[0]) + ', ' + str(g.latlng[1]) + ')\' along with other device information have been collected and submitted. Stop snooping :)")</script><center><h1>Attendance QR Code</h1><br></br><img src="' + z + '" alt="QR Code" width="400vw" height="400vh"/></center>')
  else:
    return('stop snooping')

@app.route('/attend/')
def attend():
  date = request.args.get('date')
  key1 = request.args.get('key1')
  key2 = request.args.get('key2')
  key3 = request.args.get('key3')
  d = str(datetime.datetime.now())
  if(str(d[0:d.index(" ")]) == date):
    if(int(key1) % 2 == int(key2.replace("new", "")) and int(key1) % 57 == int(key3)):
      return('<center><h1>Hello<span id="name">!</span></h1><br></br><span id="attended"></span><div id="nameField"><input type="text" id="nameIn" placeholder="First Name"></input><button onclick="sub()">Submit</button></div></center><script>function sub(){localStorage.setItem("name", document.getElementById("nameIn").value); location.reload()} if(localStorage.getItem("name") != null){var response = fetch("https://reattend-real.rt123.repl.co/add/?name="+localStorage.getItem("name") + "&date=" + "' + str(d[0:d.index(" ")]) + '"); console.log(response); document.getElementById("name").innerHTML = " " + localStorage.getItem("name"); document.getElementById("name").style.display = "block"; document.getElementById("nameField").style.display = "none"; document.getElementById("attended").style.display = "block";  document.getElementById("attended").innerHTML = "You have been logged, you may now close the tab!";} else{document.getElementById("name").style.display = "none"; document.getElementById("nameField").style.display = "block";}</script>')
  return('<p>Wrong Address</p>')

@app.route('/add/')
def add():
  date = request.args.get('date')
  name = request.args.get('name')
  if(not json.dumps(data.get()).__contains__(json.dumps({"name":name, "date":date}))):
    data.add({"name":name, "date":date})
  return "400"

app.run(host='0.0.0.0', port=81)
