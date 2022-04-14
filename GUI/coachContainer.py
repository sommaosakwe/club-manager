from tkinter import *

from API.coachStats import coachStats
from API.currentUser import currentUser

from GUI.coachFrames.coachAttendanceFrame import coachAttendanceFrame
from GUI.coachFrames.coachCreateNotificationFrame import coachCreateNotificationFrame
from GUI.coachFrames.coachDeadendFrame import coachDeadendFrame
from GUI.coachFrames.coachMemberListFrame import coachMemberListFrame
from GUI.coachFrames.coachNotificationsFrame import coachNotificationsFrame

class coachContainer(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent.main, name="memberContainer")
        self.config(width=1280, height=720)
        self.parent = parent

        self.childrenFrames = {
            "coachMemberList": coachMemberListFrame,
            "coachAttendance": coachAttendanceFrame,
            "coachNotifications": coachNotificationsFrame,
            "coachCreateNotification": coachCreateNotificationFrame,
            "coachDeadend": coachDeadendFrame
        }

        if coachStats.singleCoachClubPresence(currentUser.getCurrentUser()):
            self.currentFrame = coachAttendanceFrame(self)
        else:
            self.currentFrame = coachDeadendFrame(self)

        self.currentFrame.pack()

    def switchFrame(self, frameName):
        f = self.childrenFrames[frameName]
        if self.currentFrame is not None:
            self.currentFrame.pack_forget()
        self.currentFrame = f(self)
        self.currentFrame.pack()
