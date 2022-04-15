from tkinter import *
from tkinter import messagebox

from API.week import week

class treasurerWeekChangeFrame(Frame):

    def updateWeek(self, parent):
        week.updateWeek(week.getCurrentWeek() + 1)
        messagebox.showinfo("Update Week","You have successfully updated the club to week " + str(week.getCurrentWeek()))
        parent.switchFrame("treasurerWeekChange")

    def __init__(self, parent):
        Frame.__init__(self, parent, name="treasurerWeekChange")
        self.parentFrame = parent
        self.config(width=1280, height=720)
        self.pack_propagate(False)

        weekLabel = Label(self, text="Week: " + str(week.getCurrentWeek()))
        weekLabel.pack(anchor='nw',side=LEFT)

        logout = Button(self, text="Logout", command=lambda: parent.parent.switchFrame("loginChoice"))
        logout.pack(anchor='ne',side=RIGHT)

        nav = Frame(self)

        coach = Button(nav, text="Coach List", command=lambda: parent.switchFrame("treasurerCoachList"))
        coach.grid(column=0,row=0)

        recentInvoice = Button(nav, text="Recent Invoice", command=lambda: parent.switchFrame("treasurerRecentInvoice"))
        recentInvoice.grid(column=1,row=0)

        globalInvoice = Button(nav, text="Global Invoice", command=lambda: parent.switchFrame("treasurerGlobalInvoice"))
        globalInvoice.grid(column=2,row=0)

        notifications = Button(nav, text="Notifications", command=lambda: parent.switchFrame("treasurerNotifications"))
        notifications.grid(column=3,row=0)

        weekChange = Button(nav, text="Week Change")
        weekChange.grid(column=4,row=0)

        nav.pack(anchor='n',side=TOP)

        updateWeek = Button(self, text="Update to week " + str(week.getCurrentWeek() + 1), command=lambda: self.updateWeek(parent))
        updateWeek.pack(side=TOP)