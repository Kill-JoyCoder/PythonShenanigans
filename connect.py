"""using (import) to treat another .py file as a MODULE
   .py extension not required to mention anywhere
   Works in SAME DIRECTORY"""
import Zprntd
count=0
for i in range(7,1,-2):
    for j in range(3):
        print(i,j)
        count+=1
Zprntd.func()