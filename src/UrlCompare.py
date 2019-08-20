"""
Utility script to compare two json files response using request module
@author : Ganesh Kumar
"""
import json
import requests
import sys

#print the console out in 
#sys.stdout=open("mismatch.txt","w")

BASE_URL = "https://reqres.in"
params = {'page':2}
params1 = {'page':3}
response = requests.get(BASE_URL+"/api/users",params=params)
response2 = requests.get(BASE_URL+"/api/users",params=params1)
resp1 = response.json()
resp2 = response2.json() 


# oldurl_resp = { "firstName":"alex", "age":31, "dob":"10-12-1988" }
# newurl_resp = { "firstName":"**alx**", "**ag**":31, "dob":"10-12-1988"}

class UrlComapre():
          
 def validate_resp(self,old_resp,new_resp):
    for old_k,old_v in resp1.items():
  
        try:
            if old_k in new_resp:
                new_val = resp2[old_k]
               
            else:
                raise KeyError('newurl_response doesn\'t have key: '+old_k)
  
            try:
                if old_v != new_val:
                    raise ValueError('new value = '+str(new_val)+' doesn\'t match with orignal value = '+str(old_v)+' of key: '+str(old_k))
                #else:
                 # print('new value = '+str(new_val)+'  match with orignal value = '+str(old_v)+' of key: '+str(old_k))     
                    #raise ValueError('new value = {} doesn\'t match with orignal value = {} of key: {}'.format(new_val,old_v,old_k))
  
            except ValueError as v_err:
                print(v_err.args)
  
        except KeyError as k_err:
            print(k_err.args)
  
url = UrlComapre()
url.validate_resp(resp1,resp2)