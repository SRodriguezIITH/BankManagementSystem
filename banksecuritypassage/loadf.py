import time
import emoji

def loadbar(ch):
 if ch==3 or ch==7:
 s1="\":dollar_banknote:\""
 s2 ="\":money_bag:\""
 if ch==4:
 s1="\":money_bag:\""
 s2 ="\":dollar_banknote:\""
 if ch==5:
 s1="\":money_bag:\""
 s2 ="\":money_bag:\""
 for i in range(20): #To simulate a load screen bar
 if i<6 or (i>7 and i<14)or(i>17):
 print('.',end="")
 time.sleep(0.2)
 if (i>5 and i<8):
 print("",emoji.emojize(s1),end="")
 time.sleep(0.2)
 if (i>13 and i<16):
 print("-->",end="")
 time.sleep(0.2)
 if (i>15 and i<18):
 print("",emoji.emojize(s2),end="")
 time.sleep(0.2)
