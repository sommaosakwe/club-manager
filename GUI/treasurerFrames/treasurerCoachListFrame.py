from tkinter import *
from tkinter.ttk import Separator
from tkinter import messagebox

from API.coachStats import coachStats
from API.week import week

from GUI.scrollableFrame import ScrollableFrame

class treasurerCoachListFrame(Frame):

    def addCoach(self, username):
        coachStats.addCoach(username)
        messagebox.showinfo("Coach Added", username +" was added to the club")
        self.parentFrame.switchFrame("treasurerCoachList")

    def removeCoach(self, username):
        coachStats.removeCoach(username)
        messagebox.showinfo("Coach Removed", username +" was removed from the club")
        self.parentFrame.switchFrame("treasurerCoachList")

    def createCoachEntry(self, parent, username, isInClub):
        entry = Frame(parent)

        coachUsername = Label(entry, text=username)
        coachUsername.pack(side=LEFT)

        if not isInClub:
            invite = Button(entry, text="Add to club", command=lambda: self.addCoach(username))
            invite.pack(side=RIGHT,padx=10)
        else:
            remove = Button(entry, text="Remove from club", command=lambda: self.removeCoach(username))
            remove.pack(side=RIGHT,padx=10)
        
        return entry

    def coachListBox(self, parent):
        container = LabelFrame(parent, text="Coach List")

        scrollableFrame = ScrollableFrame(container,width=1280 * 0.8,height=720 * 0.8)
        scrollableFrame.pack_propagate(False)

        for coach in coachStats.coachClubPresenceList():
            self.createCoachEntry(scrollableFrame.scrollable_frame, coach[0], coach[1]).pack(anchor='nw',side=TOP)
            Separator(scrollableFrame.scrollable_frame,orient='horizontal').pack(anchor='nw',side=TOP,fill=X)

        scrollableFrame.pack(side=TOP)
        return container

    def __init__(self, parent):
        Frame.__init__(self, parent, name="treasurerCoachList")
        self.parentFrame = parent
        self.config(width=1280, height=720)
        self.pack_propagate(False)

        weekLabel = Label(self, text="Week: " + str(week.getCurrentWeek()))
        weekLabel.pack(anchor='nw',side=LEFT)

        logout = Button(self, text="Logout", command=lambda: parent.parent.switchFrame("loginChoice"))
        logout.pack(anchor='ne',side=RIGHT)

        nav = Frame(self)

        coach = Button(nav, text="Coach List")
        coach.grid(column=0,row=0)

        recentInvoice = Button(nav, text="Recent Invoice", command=lambda: parent.switchFrame("treasurerRecentInvoice"))
        recentInvoice.grid(column=1,row=0)

        globalInvoice = Button(nav, text="Global Invoice", command=lambda: parent.switchFrame("treasurerGlobalInvoice"))
        globalInvoice.grid(column=2,row=0)

        notifications = Button(nav, text="Notifications", command=lambda: parent.switchFrame("treasurerNotifications"))
        notifications.grid(column=3,row=0)

        nav.pack(anchor='n',side=TOP)

        coachList = self.coachListBox(self)
        coachList.pack(side=TOP)