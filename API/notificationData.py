class notificationData:
    def getMemberNotifications():
        notifications = []
        with open("./data/notifications/memberNotifications.txt", 'r') as f:
            data = f.read().split('\n')
        for line in data:
            if line:
                n = line.split(':')
                notifications.append((n[0],n[1]))
        notifications.reverse()
        if len(notifications) == 0:
            notifications.append("No notifications at this time")
        return notifications

    def addMemberNotification(coachUsername, message):
        notification = coachUsername + ":" + message + "\n"
        with open("./data/notifications/memberNotifications.txt", 'a') as f:
            f.write(notification)
    
    def getTreasurerCoachNotifications():
        notifications = []
        with open("./data/notifications/tcNotifications.txt", 'r') as f:
            data = f.read().split('\n')
        for line in data:
            line and notifications.append(line)
        if len(notifications) == 0:
            notifications.append("No notifications at this time")
        return notifications
    
    def addTreasurerCoachNotification(message):
        with open("./data/notifications/memberNotifications.txt", 'a') as f:
            f.write(message)
