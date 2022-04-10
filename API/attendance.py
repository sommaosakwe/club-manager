class attendance:

    # Adds given week to list of attended weeks for given member
    def memberAttend(self, username, week):
        with open("./data/members/" + username + ".txt", 'r') as f:
            data = f.readlines()
        weeks = [int(n) for n in data[1].rstrip('\n').split(' ') if n]
        weeks.append(week)
        data[1] = ' '.join(str(n) for n in weeks) + '\n'
        with open("./data/members/" + username + ".txt", 'x') as f:
            f.writelines(data)

    # Adds given week to list of paid weeks for given member
    def memberPay(self, username, week):
        with open("./data/members/" + username + ".txt", 'r') as f:
            data = f.readlines()
        weeks = [int(n) for n in data[2].rstrip('\n').split(' ') if n]
        weeks.append(week)
        data[2] = ' '.join(str(n) for n in weeks) + '\n'
        with open("./data/members/" + username + ".txt", 'x') as f:
            f.writelines(data)

    # Adds given week to list of attended weeks for given coach
    def coachAttend(self, username, week):
        with open("./data/coaches/" + username + ".txt", 'r') as f:
            data = f.readlines()
        weeks = [int(n) for n in data[1].rstrip('\n').split(' ') if n]
        weeks.append(week)
        data[1] = ' '.join(str(n) for n in weeks) + '\n'
        with open("./data/coaches/" + username + ".txt", 'x') as f:
            f.writelines(data)

    # Returns list of tuples (x, y) where x is a member username and y is the number
    # of weeks that member has attended, sorted by y
    def sortedMembers(self):
        memberUsernames = []
        memberAttendances = []
        with open("./data/memberCredentials.txt", 'r') as f:
            for line in f.readlines():
                memberUsernames.append(line.rstrip('\n').split(' ')[0])
        for username in memberUsernames:
            with open("./data/members/" + username + ".txt", 'r') as f:
                data = f.readlines()
                if data[0] == 'IN\n':
                    weeksAttended = [int(n) for n in data[1].rstrip('\n').split(' ') if n]
                    memberAttendances.append((username, len(weeksAttended)))
        memberAttendances.sort(key=lambda m: m[1])
        return memberAttendances
