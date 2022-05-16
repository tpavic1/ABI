def DPChange(money,coins):
    MinNumCoins=[0]

    for m in range(1,money+1):
        MinNumCoins.append(float("inf"))
        for i in range(1,len(coins)):
            if(m>=coins[i]):
                if MinNumCoins[m-coins[i]]+1 < MinNumCoins[m]:
                    MinNumCoins[m]=MinNumCoins[m-coins[i]]+1
    
    return MinNumCoins[money]

### ispis

sample_=''''''
sample=sample_.splitlines()
money=int(sample[0])
coins=list(map(int,sample[1].split(",")))

DPChange(money,coins)
