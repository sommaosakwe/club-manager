from tkinter import *
from tkinter import messagebox

from API.week import week
from API.memberStats import memberStats
from API.currentUser import currentUser

class memberPayFrame(Frame):

    def payWeek(self, weekNum, weekCount):
        username = currentUser.getCurrentUser()
        amount = memberStats.getPaymentAmount(username)
        for i in range(weekNum, weekNum + weekCount):
            if not memberStats.checkIfMemberPaid(username, i):
                memberStats.memberPay(username, i)
                memberStats.memberPayUpdateRevenue(i, amount)
                messagebox.showinfo("Payment Information", "You paid $" + str(amount) + " for week " + str(i))

    def __init__(self, parent):
        Frame.__init__(self, parent, name="memberPay")
        self.config(width=1280, height=720)
        self.pack_propagate(False)

        weekLabel = Label(self, text="Week: " + str(week.getCurrentWeek()))
        weekLabel.pack(anchor='nw',side=LEFT)

        logout = Button(self, text="Logout", command=lambda: parent.parent.switchFrame("loginChoice"))
        logout.pack(anchor='ne',side=RIGHT)

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

        payThisWeek = Button(paymentResponses, text="Pay for this week (" + str(week.getCurrentWeek()) +  ")\n$"
            + str(memberStats.getPaymentAmount(currentUser.getCurrentUser())), command=lambda: self.payWeek(week.getCurrentWeek(),1))
        payThisWeek.pack(side=TOP,fill=X)

        payNext2Weeks = Button(paymentResponses, text="Pay for the next 2 weeks\n$"
            + str(2 * memberStats.getPaymentAmount(currentUser.getCurrentUser())), command=lambda: self.payWeek(week.getCurrentWeek(),2))
        payNext2Weeks.pack(side=TOP,fill=X)

        payNext3Weeks = Button(paymentResponses, text="Pay for the next 3 weeks\n$"
            + str(3 * memberStats.getPaymentAmount(currentUser.getCurrentUser())), command=lambda: self.payWeek(week.getCurrentWeek(),3))
        payNext3Weeks.pack(side=TOP,fill=X)

        payNextMonth = Button(paymentResponses, text="Pay for the next month\n$"
            + str(4 * memberStats.getPaymentAmount(currentUser.getCurrentUser())), command=lambda: self.payWeek(week.getCurrentWeek(),4))
        payNextMonth.pack(side=TOP,fill=X)

        paymentResponses.pack(side=TOP)