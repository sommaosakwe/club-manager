from tkinter import *
from tkinter import messagebox

from API.treasurerAccount import treasurerAccount

class treasurerPaymentMethodFrame(Frame):

    def pay(self, parent, amount):
        treasurerAccount.pay(amount)
        messagebox.showinfo("Payment Success","Amount paid: $" + str(amount) + "\nRemaining Balance: $" + str(treasurerAccount.getAccountBalance))
        parent.switchFrame("treasurerInvoice")

    def __init__(self, parent, amount):
        Frame.__init__(self, parent, name="treasurerPaymentMethod")
        self.config(width=1280, height=720)
        self.pack_propagate(False)

        back = Button(self, text="Back to invoice", command=lambda: parent.switchFrame("treasurerInvoice"))
        back.pack(anchor='nw',side=LEFT)

        logout = Button(self, text="Logout", command=lambda: parent.parent.switchFrame("loginChoice"))
        logout.pack(anchor='ne',side=RIGHT)

        paymentMethodPrompt = Label(self, text="Please select an account to pay:")
        paymentMethodPrompt.pack(side=TOP)

        treasurerAccountButton = Button(self, text="Club Account\n$" + str(treasurerAccount.getAccountBalance()), command=lambda: self.pay(parent, amount))
        treasurerAccountButton.pack(side=TOP)
