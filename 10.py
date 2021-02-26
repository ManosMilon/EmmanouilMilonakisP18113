import json 

def depth(x):

    # AN EINAI  LEKSIKO KAI OXI NULL TOTE EPESTREPSE TO MEGISTO
    # TIS SINARTISIS DEPTH  GIA KATHE STOIXEIO TOU LEKSIKOU KAI PROSTHESE ENA GIA AYTO POY IDI PROSPELASES
    if type(x) is dict and x:
        return 1 + max(depth(x[a]) for a in x)
    # AN EINAI LISTA KAI OXI NULL
    if type(x) is list and x:
        return 1 + max(depth(a) for a in x)
    return 0
          
    
f = open("demo.txt", "r")
dictio=json.loads(f.read()) 


print(depth(dictio)) 


