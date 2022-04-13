class treasurerAccount:
    def getAccountBalance():
        with open("./data/treasurer.txt",'r') as f:
            data = f.read().split('\n')
        balance = round(float(data[1]), 2)
        return balance
    
    def pay(amount):
        with open("./data/treasurer.txt",'r') as f:
            data = f.read().split('\n')

        newBalance = round(float(data[1]), 2) - amount
        if newBalance < 0.00:
            return False

        data[1] = str(newBalance)
        with open("./data/treasurer.txt",'w') as f:
            f.writelines('\n'.join(data))
        return True
    
    def getLastWeekPaid():
        with open("./data/treasurer.txt",'r') as f:
            data = f.read().split('\n')
        return int(data[0])

    def setLastWeekPaid(week):
        with open("./data/treasurer.txt",'r') as f:
            data = f.read().split('\n')
        data[0] = str(week)
        with open("./data/treasurer.txt",'w') as f:
            f.writelines('\n'.join(data))
        return True