class coachStats:
    # Returns list of tuples (x, y) where x is a coach username
    # and y is a boolean representing their presence in the club
    def coachClubPresenceList():
        coachUsernames = []
        coachPresences = []
        with open("./data/coachCredentials.txt", 'r') as f:
            for line in f.read().split('\n'):
                line and coachUsernames.append(line.split(' ')[0])
        for username in coachUsernames:
            with open("./data/coaches/" + username + ".txt", 'r') as f:
                data = f.read().split('\n')
                if data[0] == 'IN':
                    coachPresences.append((username, True))
                elif data[0] == 'OUT':
                    coachPresences.append((username, False))
        return coachPresences

    def singleCoachClubPresence(username):
        with open("./data/coaches/" + username + ".txt", 'r') as f:
            data = f.read().split('\n')
        return data[0] == 'IN'

    def addCoach(username):
        with open("./data/coaches/" + username + ".txt", 'r') as f:
            data = f.read().split('\n')
        data[0] = 'IN'
        with open("./data/coaches/" + username + ".txt", 'w') as f:
            f.writelines('\n'.join(data))
    
    def removeCoach(username):
        with open("./data/coaches/" + username + ".txt", 'w') as f:
            f.writelines('OUT\n')