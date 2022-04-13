from tkinter import *
from GUI.memberFrames.memberAttendanceFrame import memberAttendanceFrame
from GUI.memberFrames.memberPayFrame import memberPayFrame
from GUI.memberFrames.memberNotificationsFrame import memberNotificationsFrame

class memberContainer(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent.main, name="memberContainer")
        self.config(width=1280, height=720)

        self.childrenFrames = {
            "memberAttendance": memberAttendanceFrame,
            "memberPay": memberPayFrame,
            "memberNotifications": memberNotificationsFrame
        }
        self.currentFrame = memberNotificationsFrame(self)
        self.currentFrame.pack()

    def switchFrame(self, frameName):
        f = self.childrenFrames[frameName]
        if self.currentFrame is not None:
            self.currentFrame.pack_forget()
        self.currentFrame = f(self)
        self.currentFrame.pack()
