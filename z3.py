y=int(input())
m=int(input())
d=int(input())
sum_d=0
for i to y:
    if y%4==0:
        sum_d+=366
    else:
        sum_d+=365
if m==2:
    dy=31
if m==3:
    dy=60
if m==4: 
    dy=91
if m==5: 
    dy=121
if m==6: 
    dy=152
if m==7: 
    dy=182
if m==8: 
    dy=213
if m==9: 
    dy=243
if m==10: 
    dy=274
if m==11: 
    dy=304
if m==12: 
    dy=335
if y%4==0 and 3<m<=12:
        dy+=1
 dn=(sum_d+dy+d)%7
print(dn)   
        
        
    