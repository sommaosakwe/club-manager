class login:

    # Checks if a given username and password exist within
    # the list of member credentials
    def memberLogin(username, password):
        with open('./data/memberCredentials.txt','r') as f:
            for line in f.readlines():
                data = line.rstrip('\n').split(' ')
                if username == data[0]:
                    if password == data[1]:
                        return True
        return False

    # Checks if a given username and password exist within
    # the list of coach credentials
    def coachLogin(username, password):
        with open('./data/coachCredentials.txt','r') as f:
            for line in f.readlines():
                data = line.rstrip('\n').split(' ')
                if username == data[0]:
                    if password == data[1]:
                        return True
        return False

    def treasurerLogin(username, password):
        if username == 'clubtreasurer' and password == '12345':
            return True
        return False
