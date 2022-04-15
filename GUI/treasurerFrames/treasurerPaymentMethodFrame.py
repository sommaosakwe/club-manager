from tkinter import *
from tkinter import messagebox

from API.treasurerAccount import treasurerAccount

class treasurerPaymentMethodFrame(Frame):

    def pay(self, parent):
        amount = treasurerAccount.getCurrentCost()
        if treasurerAccount.pay(amount):
            messagebox.showinfo("Payment Success","Amount paid: $" + str(amount) + "\nRemaining Balance: $" + str(treasurerAccount.getAccountBalance()))
        else:
            messagebox.showerror("Payment Failure","There is not enough money in this account")
        parent.switchFrame("treasurerRecentInvoice")

    def __init__(self, parent):
        Frame.__init__(self, parent, name="treasurerPaymentMethod")
        self.config(width=1280, height=720)
        self.pack_propagate(False)

        back = Button(self, text="Back to invoice", command=lambda: parent.switchFrame("treasurerRecentInvoice"))
        back.pack(anchor='nw',side=LEFT)

        logout = Button(self, text="Logout", command=lambda: parent.parent.switchFrame("loginChoice"))
        logout.pack(anchor='ne',side=RIGHT)

        paymentMethodPrompt = Label(self, text="Please select an account to pay the amount of $" + str(treasurerAccount.getCurrentCost()) + ":")
        paymentMethodPrompt.pack(side=TOP)

        treasurerAccountButton = Button(self, text="Club Account\n$" + str(treasurerAccount.getAccountBalance()), command=lambda: self.pay(parent))
        treasurerAccountButton.pack(side=TOP)
