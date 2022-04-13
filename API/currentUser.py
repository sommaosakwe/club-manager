class currentUser:
    def getCurrentUser():
        with open("./data/currentUser.txt", 'r') as f:
            data = f.read().split('\n')
        return data[0]

    def setCurrentUser(username):
        with open("./data/currentUser.txt", 'w') as f:
            f.write(username)
