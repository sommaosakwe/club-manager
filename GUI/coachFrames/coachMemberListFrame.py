from tkinter import *
from tkinter.ttk import Separator
from tkinter import messagebox

from API.memberStats import memberStats
from API.week import week

from GUI.scrollableFrame import ScrollableFrame

class coachMemberListFrame(Frame):

    def addMember(self, username):
        memberStats.addMember(username)
        messagebox.showinfo("Member Added", username +" was added to the club")

    def removeMember(self, username):
        memberStats.removeMember(username)
        messagebox.showinfo("Member Removed", username +" was removed from the club")

    def createMemberEntry(self, parent, username, isInClub, isOverdue):
        entry = Frame(parent)

        memberUsername = Label(entry, text=username)
        memberUsername.pack(side=LEFT)

        if not isInClub:
            add = Button(entry, text="Add to club", command=lambda: self.addMember(username))
            add.pack(side=RIGHT,padx=10)
        else:
            remove = Button(entry, text="Remove from club", command=lambda: self.removeMember(username))
            remove.pack(side=RIGHT,padx=10)

        if isOverdue:
            remind = Button(entry, text="Remind to pay")
            remind.pack(side=RIGHT,padx=10)
        
        return entry

    def memberListBox(self, parent):
        container = LabelFrame(parent, text="Member List")

        scrollableFrame = ScrollableFrame(container,width=1280 * 0.8,height=720 * 0.8)
        scrollableFrame.pack_propagate(False)

        for member in memberStats.memberClubPresence():
            self.createMemberEntry(scrollableFrame.scrollable_frame, member[0], member[1], False).pack(anchor='nw',side=TOP)
            Separator(scrollableFrame.scrollable_frame,orient='horizontal').pack(anchor='nw',side=TOP,fill=X)

        scrollableFrame.pack(side=TOP)
        return container

    def __init__(self, parent):
        Frame.__init__(self, parent, name="coachMemberList")
        self.config(width=1280, height=720)
        self.pack_propagate(False)

        weekLabel = Label(self, text="Week: " + str(week.getCurrentWeek()))
        weekLabel.pack(anchor='nw',side=LEFT)

        logout = Button(self, text="Logout", command=lambda: parent.parent.switchFrame("loginChoice"))
        logout.pack(anchor='ne',side=RIGHT)

        nav = Frame(self)

        member = Button(nav, text="Member List")
        member.grid(column=0,row=0)

        attend = Button(nav, text="Attendance", command=lambda: parent.switchFrame("coachAttendance"))
        attend.grid(column=1,row=0)

        notifications = Button(nav, text="Notifications", command=lambda: parent.switchFrame("coachNotifications"))
        notifications.grid(column=2,row=0)

        nav.pack(anchor='n',side=TOP)

        memberList = self.memberListBox(self)
        memberList.pack(side=TOP)