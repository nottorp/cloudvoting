import urllib2
import requests

def storageGet(key):
    res = requests.get("http://127.0.0.1:9000/storage?a=getk=" + key)
    txt = res.text
    if txt.startswith("ERR"):
        return None
    val = res[4:]
    if val.startswith("UKNOWN"):
        return None
    return val

def storageSet(key, val):
    res = requests.get("http://127.0.0.1:9000/storage?a=set&k=" + key + "&v=" + val)
    txt = res.text
    print txt
    if not txt.startswith("OK"):
        return False
    return True

def storageGetAll():
    # Work around bug in storage plugin
    res = requests.get("http://127.0.0.1:9000/storage?a=getall&k=dummy")
    txt = res.text
    pairs = txt.split('|')
    dict = {}
    for p in pairs:
        pp = p.split(':')
        # One dummy at the end, due to generation
        if len(pp) >= 2:
            dict[pp[0]] = pp[1]
    return dict