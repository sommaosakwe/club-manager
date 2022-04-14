class attendance:

    # Adds given week to list of attended weeks for given member
    def memberAttend(username, week):
        with open("./data/members/" + username + ".txt", 'r') as f:
            data = f.read().split('\n')
        weeks = [int(n) for n in data[1].split(' ') if n]
        weeks.append(week)
        data[1] = ' '.join(str(n) for n in weeks)
        with open("./data/members/" + username + ".txt", 'w') as f:
            f.writelines('\n'.join(data))

    # Adds given week to list of attended weeks for given coach
    def coachAttend(username, week):
        with open("./data/coaches/" + username + ".txt", 'r') as f:
            data = f.read().split('\n')
        weeks = [int(n) for n in data[1].rstrip('\n').split(' ') if n]
        weeks.append(week)
        data[1] = ' '.join(str(n) for n in weeks)
        with open("./data/coaches/" + username + ".txt", 'w') as f:
            f.writelines('\n'.join(data))
