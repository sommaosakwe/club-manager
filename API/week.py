class week:
    def getCurrentWeek():
        with open("./data/weeks.txt", 'r') as f:
            data = f.read().split('\n')
        return int(data[0])
    
    def getLastWeekPaid():
        with open("./data/treasurer.txt", 'r') as f:
            data = f.read().split('\n')
        return int(data[0])

    def parseWeeksFromLastPayment():
        invoice = []
        with open("./data/weeks.txt",'r') as f:
            data = f.read().split('\n')
        for line in data[week.getLastWeekPaid() + 1: week.getCurrentWeek() + 1]:
            elems = line.split(' ')
            invoice.append((int(elems[0]), float(elems[1]), elems[2], 100.0))
        return invoice

    def parseAllWeeks():
        invoice = []
        with open("./data/weeks.txt",'r') as f:
            data = f.read().split('\n')
        for line in data[1:]:
            elems = line.split(' ')
            invoice.append((int(elems[0]), float(elems[1]), elems[2], 100.0))
        return invoice
    
    def getTotalRevenueCostProfit(invoice):
        revenue = 0.0
        cost = 0.0
        for week in invoice:
            revenue += week[1]
            cost += (week[2] != 'absent') * 50.0 + week[3]
        return (revenue, cost, revenue - cost)

    def updateWeek(weekNum):
        with open("./data/weeks.txt",'r') as f:
            data = f.read().split('\n')
        data[0] = str(weekNum)
        if len(data) <= weekNum:
            data.append(str(weekNum) + " 0.0 absent")
        with open("./data/weeks.txt",'w') as f:
            f.writelines('\n'.join(data))
