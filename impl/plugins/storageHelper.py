import urllib2

def storageGet(key):
    res = urllib2.urlopen("http://127.0.0.1:9000/storage?a=getk=" + key)
    if res.startswith("ERR"):
        return None
    val = res[4:]
    if val.startswith("UKNOWN"):
        return None
    return val

def storageSet(key, val):
    res = urllib2.urlopen("http://127.0.0.1:9000/storage?a=set&k=" + key + "&v=" + val)
    if not res.startswith("OK"):
        return False
    return True

def storageGetAll():
    # Work around bug in storage plugin
    res = urllib2.urlopen("http://127.0.0.1:9000/storage?a=getall&k=dummy")
    pairs = res.split('|')
    dict = {}
    for p in pairs:
        pp = p.split(':')
        dict[pp[0]] = pp[1]
    return dict