class createAccount:

    def memberExists(self, username):
        with open('./data/memberCredentials.txt') as f:
            for line in f.readlines():
                data = line.split(' ')
                if username == data[0]:
                    return True
        return False
    
    def coachExists(self, username):
        with open('./data/coachCredentials.txt') as f:
            for line in f.readlines():
                data = line.split(' ')
                if username == data[0]:
                    return True
        return False

    def createMember(self, username, password):
        if not self.memberExists(username):
            with open('./data/memberCredentials.txt', 'a') as f:
                f.write(username + " " + password + "\n")
                with open("./data/members/" + username + ".txt", 'x') as m:
                    m.write('OUT\n\n\n')
                return True
        return False
    
    def createCoach(self, username, password):
        if not self.coachExists(username):
            with open('./data/coachCredentials.txt', 'a') as f:
                f.write(username + " " + password + "\n")
                with open("./data/coaches/" + username + ".txt", 'x') as c:
                    c.write('OUT\n')
                return True
        return False

