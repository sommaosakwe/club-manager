class attendance:

    # Adds given week to list of attended weeks for given member
    def memberAttend(self, username, week):
        with open("./data/members/" + username + ".txt", 'r') as f:
            data = f.read().split('\n')
        weeks = [int(n) for n in data[1].split(' ') if n]
        weeks.append(week)
        data[1] = ' '.join(str(n) for n in weeks)
        with open("./data/members/" + username + ".txt", 'w') as f:
            f.writelines('\n'.join(data))

    # Adds given week to list of paid weeks for given member
    def memberPay(self, username, week):
        with open("./data/members/" + username + ".txt", 'r') as f:
            data = f.read().split('\n')
        weeks = [int(n) for n in data[2].split(' ') if n]
        weeks.append(week)
        data[2] = ' '.join(str(n) for n in weeks)
        with open("./data/members/" + username + ".txt", 'w') as f:
            f.writelines('\n'.join(data))

    # Adds given week to list of attended weeks for given coach
    def coachAttend(self, username, week):
        with open("./data/coaches/" + username + ".txt", 'r') as f:
            data = f.read().split('\n')
        weeks = [int(n) for n in data[1].rstrip('\n').split(' ') if n]
        weeks.append(week)
        data[1] = ' '.join(str(n) for n in weeks)
        with open("./data/coaches/" + username + ".txt", 'w') as f:
            f.writelines('\n'.join(data))

    # Returns list of tuples (x, y) where x is a member username and y is the number
    # of weeks that member has attended, sorted by y
    def sortedMembers(self):
        memberUsernames = []
        memberAttendances = []
        with open("./data/memberCredentials.txt", 'r') as f:
            for line in f.read().split('\n'):
                memberUsernames.append(line.split(' ')[0])
        for username in memberUsernames:
            with open("./data/members/" + username + ".txt", 'r') as f:
                data = f.read().split('\n')
                if data[0] == 'IN':
                    weeksAttended = [int(n) for n in data[1].split(' ') if n]
                    memberAttendances.append((username, len(weeksAttended)))
        memberAttendances.sort(key=lambda m: m[1])
        return memberAttendances
