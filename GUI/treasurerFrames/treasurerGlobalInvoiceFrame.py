from tkinter import *
from tkinter.ttk import Separator

from API.week import week

from GUI.scrollableFrame import ScrollableFrame

class treasurerGlobalInvoiceFrame(Frame):

    def createInvoiceRow(self, parent, weekData, oldProfit, deltaFlag):
        rowContainer = Frame(parent)

        weekInfo = Label(rowContainer, text="Week: " + str(weekData[0]))
        weekInfo.pack(side=LEFT)

        Separator(rowContainer, orient='vertical').pack(side=LEFT,padx=10,fill=Y)
        memberRevenue = Label(rowContainer, text="Member revenue: $" + str(weekData[1]))
        memberRevenue.pack(side=LEFT,padx=10)

        Separator(rowContainer, orient='vertical').pack(side=LEFT,padx=10,fill=Y)
        coachFee = Label(rowContainer, text="Coach fee: $" + str((weekData[2] != "absent") * 50.0) + " (" + weekData[2] + ")")
        coachFee.pack(side=LEFT,padx=10)

        Separator(rowContainer, orient='vertical').pack(side=LEFT,padx=10,fill=Y)
        rentFee = Label(rowContainer, text="Rent fee: $100.0")
        rentFee.pack(side=LEFT,padx=10)

        Separator(rowContainer, orient='vertical').pack(side=LEFT,padx=10,fill=Y)
        localProfit = weekData[1] - (weekData[2] != "absent") * 50.0 - weekData[3]
        profit = Label(rowContainer, text="Profit: $" + str(localProfit))
        profit.pack(side=LEFT,padx=10)

        if deltaFlag:
            Separator(rowContainer, orient='vertical').pack(side=LEFT,padx=10,fill=Y)
            delta = Label(rowContainer, text="Delta: $" + str(localProfit - oldProfit))
            delta.pack(side=LEFT,padx=10)

        return rowContainer

    def createRevenueCostProfitRow(self, parent, revenueCostProfit):
        rowContainer = Frame(parent)

        revenue = Label(rowContainer, text="Total revenue: $" + str(revenueCostProfit[0]))
        revenue.pack(side=LEFT)

        Separator(rowContainer, orient='vertical').pack(side=LEFT,padx=10,fill=Y)
        cost = Label(rowContainer, text="Total cost: $" + str(revenueCostProfit[1]))
        cost.pack(side=LEFT,padx=10)

        Separator(rowContainer, orient='vertical').pack(side=LEFT,padx=10,fill=Y)
        profit = Label(rowContainer, text="Total profit: $" + str(revenueCostProfit[2]))
        profit.pack(side=LEFT,padx=10)

        return rowContainer
    
    def invoiceBox(self, parent):
        container = LabelFrame(parent, text="Invoice for weeks 1 - " + str(week.getCurrentWeek()))

        scrollableFrame = ScrollableFrame(container,width=1280 * 0.8,height=720 * 0.8)
        scrollableFrame.pack_propagate(False)

        invoice = week.parseAllWeeks()
        self.createInvoiceRow(scrollableFrame.scrollable_frame, invoice[0], 0.0, False).pack(anchor='nw',side=TOP)
        Separator(scrollableFrame.scrollable_frame,orient='horizontal').pack(anchor='nw',side=TOP,fill=X)
        oldProfit = invoice[0][1] - (invoice[0][2] != "absent") * 50.0 - invoice[0][3] 
        for weekData in invoice[1:]:
            self.createInvoiceRow(scrollableFrame.scrollable_frame, weekData, oldProfit, True).pack(anchor='nw',side=TOP)
            Separator(scrollableFrame.scrollable_frame,orient='horizontal').pack(anchor='nw',side=TOP,fill=X)
            oldProfit = weekData[1] - (weekData[2] != "absent") * 50.0 - weekData[3]
        if not invoice:
            Label(scrollableFrame.scrollable_frame, text="No invoice information at this time").pack(side=TOP)
        else:
            self.createRevenueCostProfitRow(scrollableFrame.scrollable_frame, week.getTotalRevenueCostProfit(invoice)).pack(anchor='nw',side=TOP)
            Separator(scrollableFrame.scrollable_frame,orient='horizontal').pack(anchor='nw',side=TOP,fill=X)
        
        scrollableFrame.pack()
        return container

    def __init__(self, parent):
        Frame.__init__(self, parent, name="treasurerGlobalInvoice")
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

        globalInvoice = Button(nav, text="Global Invoice")
        globalInvoice.grid(column=2,row=0)

        notifications = Button(nav, text="Notifications", command=lambda: parent.switchFrame("treasurerNotifications"))
        notifications.grid(column=3,row=0)

        weekChange = Button(nav, text="Week Change", command=lambda: parent.switchFrame("treasurerWeekChange"))
        weekChange.grid(column=4,row=0)

        nav.pack(anchor='n',side=TOP)

        invoice = self.invoiceBox(self)
        invoice.pack(side=TOP)