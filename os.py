import os 
print("pree 1 to open notepad")
print("pree 2 to open   C1alculator")
print("pree 3 to open paint")
print("pree 4 to open word")
print("pree 5 to open excel")
print("pree 6 to open chrome")
print("pree 7 to open VLC")
print("pree 8 to open powerpoint")
x=int(input("enter your number"))
if x==1:
    os.system("notepad")
elif x==2:
    os.system("calc")
elif x==3:
    os.system("mspaint")
elif x==4:
    os.system("start winword")
elif x==5:
    os.system("start excel")
elif x==6:
    
    os.system("start chrome")
elif x==7:
    os.system("start VLC")  
elif x==8:
    os.system("start powerpnt.exe")
