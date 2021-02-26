import cryptocompare
import json 



key="07adafbb5f028e8d0457c1bbd03faaec503e87df8f8acb417123ac7ca0aaa051"
cryptocompare.cryptocompare._set_api_key_parameter(key)

f = open("crypto.txt", "r")
dict=json.loads(f.read())

synolo=0
for coin in dict:
    print(coin)
    price=cryptocompare.get_price(coin)
    syn=dict[coin]*price[coin]["EUR"]
    print(syn)
    synolo+=syn
print("Synoliko poso: ",synolo)
