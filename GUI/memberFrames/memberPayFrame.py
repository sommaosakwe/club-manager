from tkinter import *
from tkinter import messagebox
from API.notificationData import notificationData

from API.week import week
from API.memberStats import memberStats
from API.currentUser import currentUser

class memberPayFrame(Frame):

    def payWeek(self, parent, weekCount):
        username = currentUser.getCurrentUser()
        weekNum = week.getCurrentWeek()
        for i in range(weekNum, weekNum + weekCount):
            if not memberStats.checkIfMemberPaid(username, i):
                amount = memberStats.getPaymentAmount(username)
                memberStats.memberPay(username, i)
                memberStats.memberPayUpdateRevenue(weekNum, amount)
                notificationData.addTreasurerCoachNotification(username + " paid $" + str(amount) + " for week " + str(i))
                messagebox.showinfo("Payment Information", "You paid $" + str(amount) + " for week " + str(i))
            else:
                messagebox.showwarning("Payment Information", "You have already paid for week " + str(i))
        parent.switchFrame("memberPay")
    
    def payOutstanding(self, parent):
        username = currentUser.getCurrentUser()
        unpaidWeeks = memberStats.getUnpaidSessionList(username)
        thisWeek = week.getCurrentWeek()
        for w in unpaidWeeks:
            memberStats.memberPay(username, w)
            memberStats.memberPayUpdateRevenue(thisWeek, 10.0)
            notificationData.addTreasurerCoachNotification(username + " paid $10.0 for week " + str(w))
            messagebox.showinfo("Payment Information", "You paid $10.0 for week " + str(w))
        parent.switchFrame("memberPay")

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

        payThisWeek = Button(paymentResponses, text="Pay for this week", command=lambda: self.payWeek(parent, 1))
        payThisWeek.pack(side=TOP,fill=X)

        payNext2Weeks = Button(paymentResponses, text="Pay for the next 2 weeks", command=lambda: self.payWeek(parent, 2))
        payNext2Weeks.pack(side=TOP,fill=X)

        payNext3Weeks = Button(paymentResponses, text="Pay for the next 3 weeks", command=lambda: self.payWeek(parent, 3))
        payNext3Weeks.pack(side=TOP,fill=X)

        payNextMonth = Button(paymentResponses, text="Pay for the next month", command=lambda: self.payWeek(parent, 4))
        payNextMonth.pack(side=TOP,fill=X)

        paymentResponses.pack(side=TOP,pady=10)

        if memberStats.getUnpaidSessions(currentUser.getCurrentUser()) != 0:
            paymentOutstanding = Label(self, text="You have outstanding payments!")
            paymentOutstanding.pack(side=TOP)
            payOutstanding = Button(self, text="Pay outstanding payments", command=lambda: self.payOutstanding(parent))
            payOutstanding.pack(side=TOP)
