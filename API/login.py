class login:

    # Checks if a given username and password exist within
    # the list of member credentials
    def memberLogin(self, username, password):
        with open('./data/memberCredentials.txt','r') as f:
            for line in f.readlines():
                data = line.rstrip('\n').split(' ')
                if username == data[0]:
                    if password == data[1]:
                        return True
        return False

    # Checks if a given username and password exist within
    # the list of coach credentials
    def coachLogin(self, username, password):
        with open('./data/coachCredentials.txt','r') as f:
            for line in f.readlines():
                data = line.rstrip('\n').split(' ')
                if username == data[0]:
                    if password == data[1]:
                        return True
        return False

    def treasurerLogin(self, username, password):
        if username == 'clubtreasurer' and password == '12345':
            return True
        return False
