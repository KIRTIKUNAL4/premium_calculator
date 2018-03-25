file=open('q.csv','r+')
for count,i in enumerate(file.readlines()):
    if(count<2):
        continue
    (fname,lname,email,age,gender,coverage,tenure)=i.split(',')
i=0.1
v=1/1+float(i)
cal=open('lifecohort.csv','r')
dic={}
for count,i in enumerate(cal.readlines()):
    if count==0:
        continue
    (x,lx,qx,dx)=i.split(',')
    dic[int(x)]=(float(lx),float(qx),float(dx))
su=0
for count,i in enumerate(range(int(age),(int(tenure))-1),1):
    su+=(v**count)*dic[i][2]
su/=dic[int(age)][0]
su*=int(coverage)
file.close()
cal.close()
file=open('s.txt','w')
file.write(str(su))
file.close()
