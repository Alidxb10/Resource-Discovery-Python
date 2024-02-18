
import requests
#reading input file
list1=[]
list2=[]
urls=open("recourses_G2.txt").readlines()
#cleaning data
for i in urls:
    i=i.split("\n")
    list1.append(i[0])
#print(list1)
#for c in list1:
 #   r=requests.get(urls,auth=c)
  #  list2.append(str(r.status_code))
with open("Group2_recourse_discovery.txt","w") as file1:
    for k in list1:
        r=requests.get(k)
        file1.write(str(k)+str(r.status_code)+" "+"\n")


