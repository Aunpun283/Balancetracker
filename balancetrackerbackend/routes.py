import pymongo
from bson import ObjectId, json_util
from django.http import JsonResponse
mongoClient = pymongo.MongoClient("mongodb+srv://aunpun:goodpassword@cluster0.a8gk28i.mongodb.net/?retryWrites=true&w=majority")

balancetracker = mongoClient["balancetracker"]
trackers = balancetracker["trackers"]

def createtracker(request):
    ownerid = request.GET.get("ownerid")
    name = request.GET.get("name")
    currency = request.GET.get("currency")
    try:
        data = {"ownerid":ownerid,"name":name,"currency":currency,"incomes":[],"expenses":[],"balance":0}
        result = trackers.insert_one(data)
        data["_id"] = str(result.inserted_id)
    except Exception as e:
        return JsonResponse({"STATUS":"FAILED","ERROR":str(e)})
    return JsonResponse({"STATUS":"SUCCESS","DATA_INSERTED":data})
def getTrackerInfo(request):
    id = request.GET.get("id")
    query = {"_id":ObjectId(id)}
    try:
        result = trackers.find(query)
    except Exception as e:
        return JsonResponse({"STATUS":"FAILED","ERROR":str(e)})
    return JsonResponse({"STATUS":"SUCCESS","DATA":json_util.dumps(result)})
def getTrackerFromOwnerId(request):
    ownerid = request.GET.get("ownerid")
    query = {"ownerid":ownerid}
    try:
        result = trackers.find(query)
    except Exception as e:
        return JsonResponse({"STATUS":"FAILED","ERROR":str(e)})
    return JsonResponse({"STATUS":"SUCCESS","DATA":json_util.dumps(result)})

def addExpense(request) :
    trackerid = request.GET.get("trackerid")
    et = request.GET.get("et")
    em = request.GET.get("em")
    en = request.GET.get("en")
    nw = request.GET.get("nw")
    i = request.GET.get("i")
    query = {"_id":ObjectId(trackerid)}
    data2insert = {"type":et,"money":em,"notes":en,"needwant":nw,"item":i}
    try:
        result = trackers.find_one(query)
        expenses = list(result["expenses"])
        balance = int(result["balance"])
        balance -= int(em)
        expenses.append(data2insert)
        trackers.update_one(query,{"$set":{"expenses":expenses,'balance':balance}})
    except Exception as e:
        return JsonResponse({"STATUS":"FAILED","ERROR":str(e)})
    return JsonResponse({"STATUS":"SUCCESS","DATA":json_util.dumps(data2insert)})
def addIncome(request) :
    trackerid = request.GET.get("trackerid")
    et = request.GET.get("it")
    em = request.GET.get("im")
    en = request.GET.get("in")
    i = request.GET.get("i")
    query = {"_id":ObjectId(trackerid)}
    data2insert = {"type":et,"money":em,"notes":en,"item":i}
    try:
        result = trackers.find_one(query)
        expenses = list(result["incomes"])
        balance = int(result["balance"])
        balance += int(em)
        expenses.append(data2insert)
        trackers.update_one(query,{"$set":{"incomes":expenses,'balance':balance}})
    except Exception as e:
        return JsonResponse({"STATUS":"FAILED","ERROR":str(e)})
    return JsonResponse({"STATUS":"SUCCESS","DATA":json_util.dumps(data2insert)})

def changeBalance(request):
    trackerid = request.GET.get("trackerid")
    money = request.GET.get("money")
    q = {"_id":ObjectId(trackerid)}
    newvalues = {"$set":{"balance":int(money)}}
    try:
        data = trackers.update_one(q,newvalues)
    
    except Exception as e:
        return JsonResponse({"STATUS":"FAILED","ERROR":str(e)})
    return JsonResponse({"STATUS":"SUCCESS"})
def deletetracker(request):
    trackerid = request.GET.get("trackerid")
    query = {"_id":ObjectId(trackerid)}

    try:
        trackers.delete_one(query)
    except Exception as e:
        return JsonResponse({"STATUS":"FAILED","ERROR":str(e)})
    return JsonResponse({"STATUS":"SUCCESS"})
