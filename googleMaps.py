import json as j
import requests as r
import APIkeys as k

def validate(address):
    digestAddress = ""
    for word in address.split():
        digestAddress += word+'+'
    response = r.get("https://maps.googleapis.com/maps/api/geocode/json?address="+digestAddress[:-1]+"&key="+k.GoogleKey)
    auxDic = j.loads(response.text)
    if auxDic["status"] == "OK":
        return auxDic["results"][0]["formatted_address"]
    return "DeuRuim"

def kComplete(addressList):
    allAddress = ""
    retunedDic = {}
    retunedDic.update({'code':{}})
    retunedDic.update({'route':{}})
    for i in range(len(addressList)):
        retunedDic['code'].update({chr(ord('a')+i):addressList[i]})
        allAddress += addressList[i].replace(' ','+')+'|'
    allAddress= allAddress[:-1]
    response = r.get("https://maps.googleapis.com/maps/api/distancematrix/json?origins="+allAddress+"&destinations="+allAddress+"&key="+k.GoogleKey)
    auxDic = j.loads(response.text)
    for i in range(0,len(addressList)):
        retunedDic['route'].update({chr(ord('a')+i):{}})
        for s in range(0,len(addressList)):
            wheight = int(auxDic['rows'][i]["elements"][s]['distance']['value'])
            retunedDic['route'][chr(ord('a')+i)].update({chr(ord('a')+s):wheight})
        retunedDic['route'][chr(ord('a')+i)].update({"color":"white"})
    return retunedDic
