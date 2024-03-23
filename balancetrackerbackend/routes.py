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
        data = {"ownerid":ownerid,"name":name,"currency":currency,"act":[],"balance":0.00}
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

def addExpense(request):
    trackerid = request.GET.get("trackerid")
    et = request.GET.get("et")  # expense type
    em = int(request.GET.get("em"))  # expense money

    query = {"_id": ObjectId(trackerid)}
    data2insert = {"type": "Expense", "et": et, "money": em}  

    try:
        result = trackers.find_one(query)
        if result:
            act = result.get("act", [])  # Retrieve existing "act" list or create a new empty list
            balance = int(result.get("balance", 0))  # Get current balance or default to 0
            balance -= em
            act.append(data2insert)  # Append expense data to the "act" list
            trackers.update_one(query, {"$set": {"act": act, "balance": balance}})
            return JsonResponse({"STATUS": "SUCCESS", "DATA": json_util.dumps(data2insert)})
        else:
            return JsonResponse({"STATUS": "FAILED", "ERROR": "Tracker not found"})
    except Exception as e:
        return JsonResponse({"STATUS": "FAILED", "ERROR": str(e)})

def addIncome(request):
    trackerid = request.GET.get("trackerid")
    it = request.GET.get("it")  # income type
    im = int(request.GET.get("im"))  # income money

    query = {"_id": ObjectId(trackerid)}
    data2insert = {"type": "Income", "it": it, "money": im}  

    try:
        result = trackers.find_one(query)
        if result:
            act = result.get("act", [])  # Retrieve existing "act" list or create a new empty list
            balance = int(result.get("balance", 0))  # Get current balance or default to 0
            balance += im
            act.append(data2insert)  # Append income data to the "act" list
            trackers.update_one(query, {"$set": {"act": act, "balance": balance}})
            return JsonResponse({"STATUS": "SUCCESS", "DATA": json_util.dumps(data2insert)})
        else:
            return JsonResponse({"STATUS": "FAILED", "ERROR": "Tracker not found"})
    except Exception as e:
        return JsonResponse({"STATUS": "FAILED", "ERROR": str(e)})


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
