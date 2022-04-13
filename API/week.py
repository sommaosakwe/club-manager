class week:
    def getCurrentWeek():
        with open("./data/weeks.txt", 'r') as f:
            data = f.read().split('\n')
        return int(data[0])
