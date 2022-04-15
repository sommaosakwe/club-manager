from tkinter import *
from tkinter import messagebox

from API.notificationData import notificationData
from API.currentUser import currentUser


class coachCreateNotificationFrame(Frame):

    def sendNotification(self, messageBox):
        notificationData.addMemberNotification(currentUser.getCurrentUser(), messageBox.get('1.0', 'end-1c'))
        messageBox.delete('1.0', END)
        messagebox.showinfo("Confirmation","Notification Sent")

    def __init__(self, parent):
        Frame.__init__(self, parent, name="coachCreateNotification")
        self.config(width=1280, height=720)
        self.pack_propagate(False)

        back = Button(self, text="Back to notifications", command=lambda: parent.switchFrame("coachNotifications"))
        back.pack(anchor='nw',side=LEFT)

        logout = Button(self, text="Logout", command=lambda: parent.parent.switchFrame("loginChoice"))
        logout.pack(anchor='ne',side=RIGHT)

        notificationLabelFrame = LabelFrame(self, text="Create Notification")
        
        messageBox = Text(notificationLabelFrame, width = 100, height=1)
        messageBox.pack(side=TOP)

        notificationLabelFrame.pack(side=TOP)

        submit = Button(self, text="Send Notification", command=lambda: self.sendNotification(messageBox))
        submit.pack(side=TOP)
