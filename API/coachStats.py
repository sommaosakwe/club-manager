class coachStats:
    # Returns list of tuples (x, y) where x is a coach username
    # and y is a boolean representing their presence in the club
    def coachClubPresence(self):
        coachUsernames = []
        coachPresences = []
        with open("./data/memberCredentials.txt", 'r') as f:
            for line in f.read().split('\n'):
                coachUsernames.append(line.split(' ')[0])
        for username in coachUsernames:
            with open("./data/members/" + username + ".txt", 'r') as f:
                data = f.read().split('\n')
                if data[0] == 'IN':
                    coachPresences.append((username, True))
                elif data[0] == 'OUT':
                    coachPresences.append((username, False))
        return coachPresences
    
    def addCoach(self, username):
        with open("./data/coaches/" + username + ".txt", 'r') as f:
            data = f.read().split('\n')
        data[0] = 'IN'
        with open("./data/coaches/" + username + ".txt", 'w') as f:
            f.writelines('\n'.join(data))
    
    def removeCoach(self, username):
        with open("./data/coaches/" + username + ".txt", 'r') as f:
            data = f.read().split('\n')
        data[0] = 'OUT'
        with open("./data/coaches/" + username + ".txt", 'w') as f:
            f.writelines('\n'.join(data))