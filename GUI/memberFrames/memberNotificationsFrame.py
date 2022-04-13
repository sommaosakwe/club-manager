from tkinter import *
from tkinter.ttk import Separator

from GUI.scrollableFrame import ScrollableFrame
from API.notificationData import notificationData
from API.week import week

class memberNotificationsFrame(Frame):

    def getNotifications(self):
        return notificationData.getMemberNotifications()

    def createNotification(self, parent, username, message):
        notificationContainer = Frame(parent)

        heading = Label(notificationContainer, text=username,font=("Arial Bold",10))
        heading.pack(anchor='nw',side=TOP)

        body = Label(notificationContainer, text=message)
        body.pack(anchor='nw',side=BOTTOM)

        return notificationContainer

    def notificationBox(self, parent):
        container = LabelFrame(parent, text="Notification Box")

        scrollableFrame = ScrollableFrame(container,width=1280 * 0.8,height=720 * 0.9)
        scrollableFrame.pack_propagate(False)

        for notificationData in self.getNotifications():
            self.createNotification(scrollableFrame.scrollable_frame, notificationData[0], notificationData[1]).pack(anchor='nw',side=TOP)
            Separator(scrollableFrame.scrollable_frame,orient='horizontal').pack(anchor='nw',side=TOP,fill=X)
        
        scrollableFrame.pack()
        return container

    def __init__(self, parent):
        Frame.__init__(self, parent, name="memberNotifications")
        self.config(width=1280, height=720)
        self.pack_propagate(False)

        weekLabel = Label(self, text="Week: " + str(week.getCurrentWeek()))
        weekLabel.pack(anchor='nw',side=LEFT)

        back = Button(self, text="Logout", command=lambda: exit(0))
        back.pack(anchor='ne',side=RIGHT)

        nav = Frame(self)

        pay = Button(nav, text="Payment", command=lambda: parent.switchFrame("memberPay"))
        pay.grid(column=0,row=0)

        attend = Button(nav, text="Attendance", command=lambda: parent.switchFrame("memberAttendance"))
        attend.grid(column=1,row=0)

        notifications = Button(nav, text="Notifications")
        notifications.grid(column=2,row=0)

        nav.pack(anchor='n',side=TOP)

        notificationBox = self.notificationBox(self)
        notificationBox.pack(side=TOP)