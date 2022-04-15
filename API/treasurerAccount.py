from API.week import week

class treasurerAccount:
    def getAccountBalance():
        with open("./data/treasurer.txt",'r') as f:
            data = f.read().split('\n')
        balance = round(float(data[1]), 2)
        return balance
    
    def pay(amount):
        with open("./data/treasurer.txt",'r') as f:
            data = f.read().split('\n')

        newBalance = round(float(data[1]), 2) + amount
        if newBalance < 0.00:
            return False

        data[0] = str(week.getCurrentWeek())
        data[1] = str(newBalance)
        with open("./data/treasurer.txt",'w') as f:
            f.writelines('\n'.join(data))
        return True

    def deposit(amount):
        with open("./data/treasurer.txt",'r') as f:
            data = f.read().split('\n')
        newBalance = round(float(data[1]), 2) + amount
        data[1] = str(newBalance)
        with open("./data/treasurer.txt",'w') as f:
            f.writelines('\n'.join(data))
        return True
    
    def setCurrentCost(amount):
        with open("./data/currentAmount.txt", 'w') as f:
            f.writelines(str(amount))
    
    def getCurrentCost():
        with open("./data/currentAmount.txt", 'r') as f:
            data = f.read().split('\n')
        return float(data[0])
    
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