from tkinter import *

from API.week import week

class memberPayFrame(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent, name="memberPay")
        self.config(width=1280, height=720)
        self.pack_propagate(False)

        weekLabel = Label(self, text="Week: " + str(week.getCurrentWeek()))
        weekLabel.pack(anchor='nw',side=LEFT)

        back = Button(self, text="Logout", command=lambda: exit(0))
        back.pack(anchor='ne',side=RIGHT)

        nav = Frame(self)

        pay = Button(nav, text="Payment")
        pay.grid(column=0,row=0)

        attend = Button(nav, text="Attendance", command=lambda: parent.switchFrame("memberAttendance"))
        attend.grid(column=1,row=0)

        notifications = Button(nav, text="Notifications",command=lambda: parent.switchFrame("memberNotifications"))
        notifications.grid(column=2,row=0)

        nav.pack(anchor='n',side=TOP)

        paymentQuestion = Label(self, text="Please select a payment option:")
        paymentQuestion.pack(side=TOP)

        paymentResponses = Frame(self)

        payThisWeek = Button(paymentResponses, text="Pay for this week (" + str(week.getCurrentWeek()) +  ")")
        payThisWeek.pack(side=TOP,fill=X)
        payNext2Weeks = Button(paymentResponses, text="Pay for the next 2 weeks")
        payNext2Weeks.pack(side=TOP,fill=X)
        payNext3Weeks = Button(paymentResponses, text="Pay for the next 3 weeks")
        payNext3Weeks.pack(side=TOP,fill=X)
        payNextMonth = Button(paymentResponses, text="Pay for the next month")
        payNextMonth.pack(side=TOP,fill=X)

        paymentResponses.pack(side=TOP)