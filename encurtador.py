import requests as r
import json as j
import APIkeys as k

def code(url):
    headers = {"Content-Type": "application/json"}
    return j.loads(r.post("https://www.googleapis.com/urlshortener/v1/url?key="+k.GoogleKey,data=j.dumps({"longUrl":url}),headers=headers).text)