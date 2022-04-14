from tkinter import *
from tkinter.ttk import Separator
from tkinter import messagebox

from API.currentUser import currentUser
from API.memberStats import memberStats
from API.notificationData import notificationData
from API.week import week

from GUI.scrollableFrame import ScrollableFrame

class coachMemberListFrame(Frame):

    def giveDiscount(self,username):
        memberStats.giveDiscount(username)
        messagebox.showinfo("Give Discount","You have given a 10% discount to " + username)
    
    def giveReminder(self,username):
        notificationData.addMemberNotification(currentUser.getCurrentUser(), username +", please pay for your unpaid sessions!")
        messagebox.showinfo("Send Reminder","You have sent a reminder to " + username)

    def addMember(self, username):
        memberStats.addMember(username)
        messagebox.showinfo("Member Added", username +" was added to the club")
        self.parentFrame.switchFrame("coachMemberList")

    def removeMember(self, username):
        memberStats.removeMember(username)
        messagebox.showinfo("Member Removed", username +" was removed from the club")
        self.parentFrame.switchFrame("coachMemberList")

    def createMemberEntry(self, parent, username, isInClub, isOverdue, eligibleForDiscount):
        entry = Frame(parent)

        memberUsername = Label(entry, text=username)
        memberUsername.pack(side=LEFT)

        if not isInClub:
            add = Button(entry, text="Add to club", command=lambda: self.addMember(username))
            add.pack(side=LEFT,padx=10)
        else:
            remove = Button(entry, text="Remove from club", command=lambda: self.removeMember(username))
            remove.pack(side=LEFT,padx=10)

            Separator(entry, orient='vertical').pack(side=LEFT,padx=10,fill=Y)
            attendedSessions = Label(entry, text="Sessions: " + str(memberStats.getAttendedSessions(username)))
            attendedSessions.pack(side=LEFT,padx=10)

            if eligibleForDiscount:
                discount = Button(entry, text="Give discount", command=lambda: self.giveDiscount(username))
                discount.pack(side=LEFT,padx=10)

            Separator(entry, orient='vertical').pack(side=LEFT,padx=10,fill=Y)
            unpaidSessions = Label(entry, text="Unpaid Sessions: " + str(memberStats.getUnpaidSessions(username)))
            unpaidSessions.pack(side=LEFT,padx=10)

            if isOverdue:
                remind = Button(entry, text="Remind to pay", command=lambda: self.giveReminder(username))
                remind.pack(side=LEFT,padx=10)
        
        return entry

    def memberListBox(self, parent):
        container = LabelFrame(parent, text="Member List")

        scrollableFrame = ScrollableFrame(container,width=1280 * 0.8,height=720 * 0.8)
        scrollableFrame.pack_propagate(False)

        members = memberStats.sortedMembers()
        for m in range(len(members)):
            self.createMemberEntry(scrollableFrame.scrollable_frame, members[m][0], members[m][1], 
                (memberStats.getUnpaidSessions(members[m][0])) != 0, m < 10).pack(anchor='nw',side=TOP)
            Separator(scrollableFrame.scrollable_frame,orient='horizontal').pack(anchor='nw',side=TOP,fill=X)

        scrollableFrame.pack(side=TOP)
        return container

    def __init__(self, parent):
        Frame.__init__(self, parent, name="coachMemberList")
        self.parentFrame = parent
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