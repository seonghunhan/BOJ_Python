
Dongil_said = 50000000
Miran_said = 1100000000

year = 0


while True :
    year += 1
    Dongil_said += (Dongil_said*0.12)
    
    if year == 28 :
        break
    
if Dongil_said > Miran_said :
    winnerPrice = int(Dongil_said - Miran_said)
    print(str(winnerPrice)+"원 차이로 동일 아저씨 말이 맞다")
else :
    winnerPrice = int(Miran_said - Dongil_said)
    print(str(winnerPrice)+"원 차이로 미란 아줌씨 말이 맞다")