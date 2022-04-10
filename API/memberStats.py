class memberStats:

    def getUnpaidSessions(self, username):
        weeksAttended = []
        weeksPaid = []
        with open("./data/members/" + username + ".txt", 'r') as f:
                data = f.read().split('\n')
                if data[0] == 'IN':
                    weeksAttended = [int(n) for n in data[1].split(' ') if n]
                    weeksPaid = [int(n) for n in data[2].split(' ') if n]
        return max(len(weeksAttended) - len(weeksPaid), 0)
