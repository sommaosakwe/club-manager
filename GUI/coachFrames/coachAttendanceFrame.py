from glob import escape
from tkinter import *
from tkinter import messagebox

from API.attendance import attendance
from API.currentUser import currentUser
from API.week import week

class coachAttendanceFrame(Frame):

    def checkIn(self, username, week):
        if not attendance.weekIsFree(week) and not attendance.coachHasAttended(username,week):
            messagebox.showerror("Check In Error","There is already a coach checked in for this week")
        elif not attendance.coachHasAttended(username, week):
            attendance.coachAttend(username, week)
            messagebox.showinfo("Check In","You have successfully checked in as the coach for this week")

    def __init__(self, parent):
        Frame.__init__(self, parent, name="coachAttendance")
        self.config(width=1280, height=720)
        self.pack_propagate(False)

        weekLabel = Label(self, text="Week: " + str(week.getCurrentWeek()))
        weekLabel.pack(anchor='nw',side=LEFT)

        logout = Button(self, text="Logout", command=lambda: parent.parent.switchFrame("loginChoice"))
        logout.pack(anchor='ne',side=RIGHT)

        nav = Frame(self)

        memberAttendance = Button(nav, text="Member Attendance List",command=lambda:parent.switchFrame("coachMemberAttendanceList"))
        memberAttendance.grid(column=0,row=0)

        memberUnpaid = Button(nav, text="Member Unpaid Session List",command=lambda:parent.switchFrame("coachMemberUnpaidList"))
        memberUnpaid.grid(column=1,row=0)

        attend = Button(nav, text="Attendance")
        attend.grid(column=2,row=0)

        notifications = Button(nav, text="Notifications", command=lambda: parent.switchFrame("coachNotifications"))
        notifications.grid(column=3,row=0)

        nav.pack(anchor='n',side=TOP)

        attendanceQuestion = Label(self, text="Are you attending this week? (" + str(week.getCurrentWeek()) + ")")
        attendanceQuestion.pack(side=TOP)

        checkIn = Button(self, text="Check in", command=lambda: self.checkIn(currentUser.getCurrentUser(), week.getCurrentWeek()))
        checkIn.pack(side=TOP)