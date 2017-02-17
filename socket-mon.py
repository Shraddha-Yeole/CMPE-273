import psutil
from collections import defaultdict

p=psutil.net_connections(kind='tcp')
kv=defaultdict(list)
count1=defaultdict(int)

for i in p:
    kv[i.pid].append(i)
    count1[i.pid]+=1

list1=[(v,k) for k,v in count1.items()]
list1.sort()
list1.reverse()
list1=[(k,v) for v,k in list1]


spaces1 = "%-5s %-5s %-5s %-5s"
print(spaces1 % (
    '"'+"pid"+'",', '"'+"laddr"+'",', '"'+"raddr"+'",', '"'+"status"+'"'))


for i in range(len(list1)):
    l=list1[i][0]
    pid=l
    sconn=kv[pid]

    for m in sconn:
        if m.laddr:
            laddr="%s@%s" % (m.laddr)
        if m.raddr:
            raddr="%s@%s" % (m.raddr)

        print "%s,%s, %s, %s " % ('"'+ str(pid)+'"'  , '"'+str(laddr)+'"'  , '"'+str(raddr)+'"'  ,'"'+str(m.status)+'"')
