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

    def memberHasAttended(username, week):
        with open("./data/members/" + username + ".txt", 'r') as f:
            data = f.read().split('\n')
        weeks = [int(n) for n in data[1].rstrip('\n').split(' ') if n]
        if week in weeks:
            return True
        return False

    # Adds given week to list of attended weeks for given coach
    def coachAttend(username, week):
        with open("./data/coaches/" + username + ".txt", 'r') as f:
            data = f.read().split('\n')
        weeks = [int(n) for n in data[1].rstrip('\n').split(' ') if n]
        weeks.append(week)
        data[1] = ' '.join(str(n) for n in weeks)
        with open("./data/coaches/" + username + ".txt", 'w') as f:
            f.writelines('\n'.join(data))

        with open("./data/weeks.txt", 'r') as f:
            data = f.read().split('\n')
        elems = data[week].split(' ')
        elems[2] = username
        data[week] = ' '.join(elems)
        with open("./data/weeks.txt", 'w') as f:
            f.writelines('\n'.join(data))
    
    def coachHasAttended(username, week):
        with open("./data/coaches/" + username + ".txt", 'r') as f:
            data = f.read().split('\n')
        weeks = [int(n) for n in data[1].rstrip('\n').split(' ') if n]
        if week in weeks:
            return True
        return False

    def weekIsFree(week):
        with open("./data/weeks.txt", 'r') as f:
            data = f.read().split('\n')
        elems = data[week].split(' ')
        return elems[2] == "absent"
