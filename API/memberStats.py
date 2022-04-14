class memberStats:

    # Returns the number of sessions a given member has not paid for
    def getUnpaidSessions(username):
        weeksAttended = []
        weeksPaid = []
        with open("./data/members/" + username + ".txt", 'r') as f:
                data = f.read().split('\n')
                if data[0] == 'IN':
                    weeksAttended = [int(n) for n in data[1].split(' ') if n]
                    weeksPaid = [int(n) for n in data[2].split(' ') if n]
        return max(len(weeksAttended) - len(weeksPaid), 0)

    def getAttendedSessions(username):
        weeksAttended = []
        with open("./data/members/" + username + ".txt", 'r') as f:
                data = f.read().split('\n')
                if data[0] == 'IN':
                    weeksAttended = [int(n) for n in data[1].split(' ') if n]
        return len(weeksAttended)

    # Returns list of tuples (x, y) where x is a member username
    # and y is a boolean representing their presence in the club
    def memberClubPresence():
        memberUsernames = []
        memberPresences = []
        with open("./data/memberCredentials.txt", 'r') as f:
            for line in f.read().split('\n'):
                line and memberUsernames.append(line.split(' ')[0])
        for username in memberUsernames:
            with open("./data/members/" + username + ".txt", 'r') as f:
                data = f.read().split('\n')
                if data[0] == 'IN':
                    memberPresences.append((username, True))
                elif data[0] == 'OUT':
                    memberPresences.append((username, False))
        return memberPresences

    # Returns list of tuples (x, y, z) where x is a member username,
    # y indicates that member's presence in the club, and z is the number
    # of weeks that member has attended, sorted by z
    def sortedMembers():
        memberUsernames = []
        memberAttendances = []
        with open("./data/memberCredentials.txt", 'r') as f:
            for line in f.read().split('\n'):
                line and memberUsernames.append(line.split(' ')[0])
        for username in memberUsernames:
            with open("./data/members/" + username + ".txt", 'r') as f:
                data = f.read().split('\n')
                if data[0] == 'IN':
                    weeksAttended = [int(n) for n in data[1].split(' ') if n]
                    memberAttendances.append((username, True, len(weeksAttended)))
                elif data[0] == 'OUT':
                    memberAttendances.append((username, False, 0))
        memberAttendances.sort(key=lambda m: m[2])
        memberAttendances.reverse()
        return memberAttendances

    def singleMemberClubPresence(username):
        with open("./data/members/" + username + ".txt", 'r') as f:
            data = f.read().split('\n')
        return data[0] == 'IN'

    def addMember(username):
        data = ["IN","","","1.00"]
        with open("./data/members/" + username + ".txt", 'w') as f:
            f.writelines('\n'.join(data))
    
    def removeMember(username):
        with open("./data/members/" + username + ".txt", 'w') as f:
            f.writelines('OUT\n\n')
    
    def memberPayUpdateRevenue(week, amount):
        with open("./data/weeks.txt", 'r') as f:
            data = f.read().split('\n')
        if len(data) <= week:
            data.append(str(week) + " " + str(amount) + " absent")
        else:
            elems = data[week].split(" ")
            newData = str(week) + " " + str(round(float(elems[1])) + amount) + " " + elems[2]
            data[week] = newData
        with open("./data/weeks.txt", 'w') as f:
            f.writelines('\n'.join(data))
    
    # Adds given week to list of paid weeks for given member
    def memberPay(username, week):
        with open("./data/members/" + username + ".txt", 'r') as f:
            data = f.read().split('\n')
        weeks = [int(n) for n in data[2].split(' ') if n]
        (week not in weeks) and weeks.append(week)
        data[2] = ' '.join(str(n) for n in weeks)
        with open("./data/members/" + username + ".txt", 'w') as f:
            f.writelines('\n'.join(data))
    
    def checkIfMemberPaid(username, week):
        with open("./data/members/" + username + ".txt", 'r') as f:
            data = f.read().split('\n')
        weeks = [int(n) for n in data[2].split(' ') if n]
        return (week in weeks)

    def getPaymentAmount(username):
        with open("./data/members/" + username + ".txt", 'r') as f:
            data = f.read().split('\n')
        discount = round(float(data[3]),2)
        return 10.00 * discount 

    def giveDiscount(username):
        with open("./data/members/" + username + ".txt", 'r') as f:
            data = f.read().split('\n')
        data[3] = "0.75"
        with open("./data/members/" + username + ".txt", 'w') as f:
            f.writelines('\n'.join(data))
