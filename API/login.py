class login:

    def memberLogin(self, username, password):
        with open('./data/memberCredentials.txt') as f:
            for line in f.readlines():
                data = line.split(' ')
                if username == data[0]:
                    if password == data[1]:
                        return True
        return False

    def coachLogin(self, username, password):
        with open('./data/coachCredentials.txt') as f:
            for line in f.readlines():
                data = line.split(' ')
                if username == data[0]:
                    if password == data[1]:
                        return True
        return False

    def treasurerLogin(self, username, password):
        pass
