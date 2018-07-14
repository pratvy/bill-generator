import json
s2=open("/home/prateek/codeasylum/billgenerator/Nike.json",'r').read()
s1=open("/home/prateek/codeasylum/billgenerator/bill_temp.html",'r').read()
jsodic = json.loads(s2)
#print(jsodic)
#print(len(jsodic['data']))
#print(jsodic['name'])
s1 = s1.replace("xxx",jsodic['name'])
re=""
net=0
for i in range(0,len(jsodic['data'])):
    re+= "<tr><td>"+str(jsodic['data'][i]['qty'])+"</td><td>"+str(jsodic['data'][i]['p/p'])+"</td><td>"+str(jsodic['data'][i]['qty']*jsodic['data'][i]['p/p'])+"</t2></tr>"
    net+=jsodic['data'][i]['qty']*jsodic['data'][i]['p/p']
s1 = s1.replace("data",re)
s1 = s1.replace("ttt",str(net))
s3 =open("/home/prateek/codeasylum/billgenerator/bill.html",'w')
s3.write(s1)
s3.close()








