from pymongo import MongoClient as mc


import matplotlib.pyplot as plt

conn = mc("localhost")
db = conn['alvas']
coll = db['tsDemo']
xAxis = [];
yAxis = []

opCur = coll.aggregate([{"$match":{"Symbol":"ASIANPAINT"}},{"$project":{"Close":1, "Date":1, "_id":0}}])

for res in opCur:
    #print(res)
    xAxis.append(res['Date'])
    yAxis.append(res['Close'])


plt.plot(xAxis,yAxis)
plt.show()