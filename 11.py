import json 

def mostUsual(x,keys):
    
    # EDO GIA KAPOIO LOGO DEN EPIANE TO TYPE = DICT OPOTE XRISIMOPOISA
    # AFTITI SINTHIKI
    if str(x)[0]=="{" and len(str(x))>2:
     
        for key in x:
            keys.append(key)
            mostUsual(x[key],keys)


    if type(x) is list and x:
        for element in x:
            # print(type(element))
            mostUsual(element,keys)
    return keys

f = open("demofile.txt", "r")
dict=json.loads(f.read())

keys=[]
for x in dict:
    keys.append(x)
    # MAZEVO OLA TA KLEIDIA STI LISTA KEYS
    mostUsual(dict[x],keys)




res = max(set(keys), key = keys.count)
print(res)