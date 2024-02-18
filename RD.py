
import requests
#reading input file
list1=[]
list2=[]
#Upload a .txt File here which include all URLs You need to test them 
urls=open("Upload-Your-TXT-File-Here").readlines()
#cleaning data
for i in urls:
    i=i.split("\n")
    list1.append(i[0])
    # new File will be generated , so change the name of the file 
with open("New-File","w") as file1:
    for k in list1:
        r=requests.get(k)
        file1.write(str(k)+str(r.status_code)+" "+"\n")


