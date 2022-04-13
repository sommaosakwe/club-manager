from tkinter import *

from API.week import week

class coachAttendanceFrame(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent, name="coachAttendance")
        self.config(width=1280, height=720)
        self.pack_propagate(False)

        weekLabel = Label(self, text="Week: " + str(week.getCurrentWeek()))
        weekLabel.pack(anchor='nw',side=LEFT)

        back = Button(self, text="Logout", command=lambda: exit(0))
        back.pack(anchor='ne',side=RIGHT)

        nav = Frame(self)

        pay = Button(nav, text="Member List", command=lambda: parent.switchFrame("coachMemberList"))
        pay.grid(column=0,row=0)

        attend = Button(nav, text="Attendance")
        attend.grid(column=1,row=0)

        notifications = Button(nav, text="Notifications",command=lambda: parent.switchFrame("coachNotifications"))
        notifications.grid(column=2,row=0)

        nav.pack(anchor='n',side=TOP)

        attendanceQuestion = Label(self, text="Are you attending this week? (" + str(week.getCurrentWeek()) + ")")
        attendanceQuestion.pack(side=TOP)

        attendanceResponses = Frame(self)

        isAttending = Button(attendanceResponses, text="Yes",command=lambda: self.is_attending())
        isAttending.grid(row=0,column=0)
        isNotAttending = Button(attendanceResponses, text="No",command=lambda: self.is_not_attending())
        isNotAttending.grid(row=0,column=1)

        attendanceResponses.pack(side=TOP)