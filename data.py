import json
import datetime


#get all json stored int json bin [no param]
def get():
  f = open('data.json')
  return json.load(f)

#find index of json object in json bin through json parameter
def index(data):
  count = 0
  list = []
  jsonData = get()
  for item in jsonData:
    if item == data:
      list.append(count)
    count += 1
  if list == []:
    return -1
  else:
    return list

#replace all json in bin with new json parameter
def post(data):
  with open('data.json', 'r+') as f:
    dataset = json.load(f)
    if json.dumps(data) == "[]":
      data = json.loads("[{}]")
    dataset = data
    f.seek(0)
    json.dump(data, f, indent=4)
    f.truncate()

#add new json to existing json in bin through json parameter
def add(data):
  if not get().__contains__(data):
    if(json.dumps(get()) != "[{}]"):
      jsonData = json.loads(json.dumps(get())[0:len(json.dumps(get()))-1] + "," + json.dumps(data) + "]")
      post(jsonData)
    else:
      post(json.loads("[" + json.dumps(data) + "]"))

#provide amount of items in json bin
def length():
  x = 0
  for i in get():
    if i is not {"name":"test","date":"1"}:
      x += 1
  return x