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

    def singleMemberClubPresence(username):
        with open("./data/members/" + username + ".txt", 'r') as f:
            data = f.read().split('\n')
        return data[0] == 'IN'

    def addMember(username):
        with open("./data/members/" + username + ".txt", 'r') as f:
            data = f.read().split('\n')
        data[0] = 'IN'
        with open("./data/members/" + username + ".txt", 'w') as f:
            f.writelines('\n'.join(data))
    
    def removeMember(username):
        with open("./data/members/" + username + ".txt", 'w') as f:
            f.writelines('OUT\n\n')
