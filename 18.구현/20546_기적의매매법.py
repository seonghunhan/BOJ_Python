import sys
import copy
input = sys.stdin.readline

holdings = int(input())
stock = list(map(int, input().split()))
stock2 = copy.deepcopy(stock)
stock2.append(-1)
junHoldings = holdings
seongHoldings = holdings
finalValue = stock[-1]
jun = 0
seong = 0
compareValue = 0

def BNP(cash, stock) :
    purchaseQuantity = 0
    
    if cash >= stock :
        purchaseQuantity = cash // stock 
        cash -= purchaseQuantity * stock
        
    return cash, purchaseQuantity
    
    
for i in stock :
    junHoldings, junPurchaseQuantity = BNP(junHoldings, i)
    jun += junPurchaseQuantity
    
temp = -1
temp2 = 0
temp3 = 0


for i in range(14) :
    
    if stock[i] > stock[i-1] :
        temp += 1
        temp2 = 0
        #print("temp : " + str(temp))
    elif stock[i] < stock[i-1] :
        temp2 += 1
        temp = 0
        #print("temp2 : " + str(temp2))
    if temp >= 3 :
        seongHoldings += temp3 * stock[i]
        temp3 = 0
        #print("매도하는날 : " +str(i)+ "일    주가 : "+ str(stock[i]))   
    if temp2 >= 3 :
        seong = seongHoldings // stock[i]
        seongHoldings -= seong * stock[i]
        # print("매수하는날 : " +str(i)+ "일    주가 : "+ str(stock[i]))
        # print("남은자산 : " + str(seongHoldings) + "  보유주식량 :" + str(seong))  
    temp3 += seong
    seong = 0
result1 = seongHoldings + (temp3 * finalValue)
result2 = junHoldings + (jun * finalValue)

#print(result1)
#print(result2)

if result1 > result2 :
    print("TIMING")
elif result1 < result2 :
    print("BNP")
else :
    print("SAMESAME")
