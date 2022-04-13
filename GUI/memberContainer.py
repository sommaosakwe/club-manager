from tkinter import *

from API.memberStats import memberStats
from API.currentUser import currentUser

from GUI.memberFrames.memberAttendanceFrame import memberAttendanceFrame
from GUI.memberFrames.memberPayFrame import memberPayFrame
from GUI.memberFrames.memberNotificationsFrame import memberNotificationsFrame
from GUI.memberFrames.memberDeadendFrame import memberDeadendFrame

class memberContainer(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent.main, name="memberContainer")
        self.config(width=1280, height=720)
        self.parent = parent

        self.childrenFrames = {
            "memberAttendance": memberAttendanceFrame,
            "memberPay": memberPayFrame,
            "memberNotifications": memberNotificationsFrame,
            "memberDeadend": memberDeadendFrame
        }

        if memberStats.singleMemberClubPresence(currentUser.getCurrentUser()):
            self.currentFrame = memberAttendanceFrame(self)
        else:
            self.currentFrame = memberDeadendFrame(self)

        self.currentFrame.pack()

    def switchFrame(self, frameName):
        f = self.childrenFrames[frameName]
        if self.currentFrame is not None:
            self.currentFrame.pack_forget()
        self.currentFrame = f(self)
        self.currentFrame.pack()
