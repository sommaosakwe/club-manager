class week:
    def getCurrentWeek():
        with open("./data/weeks.txt", 'r') as f:
            data = f.read().split('\n')
        return int(data[0])
    
    def parseWeeks(startpoint):
        data = open("data/weeks.txt","r")
        relevantWeeks = data.readlines()
        data.close()
        relevantWeeks = relevantWeeks[(startpoint + 2):]
        print(relevantWeeks)
        ProcessedListOfData = []
        for week in relevantWeeks:
            currentWeek = week.strip().split(" ")
            print(currentWeek)
            ProcessedListOfData.append([ int(currentWeek[0]), int(currentWeek[1]), currentWeek[2], 100 ])
        return ProcessedListOfData
