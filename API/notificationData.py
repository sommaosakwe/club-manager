class notificationData:
    def getMemberNotifications():
        notifications = []
        with open("./data/notifications/memberNotifications.txt", 'r') as f:
            data = f.read().split('\n')
        for line in data:
            n = line.split(':')
            notifications.append((n[0],n[1]))
        return notifications
