from tkinter import *
from tkinter import messagebox

from API.treasurerAccount import treasurerAccount

class treasurerDepositMethodFrame(Frame):

    def deposit(self, parent):
        amount = treasurerAccount.getCurrentAmount()
        treasurerAccount.pay(amount)
        messagebox.showinfo("Deposit Success","Amount paid: $" + str(amount) + "\nUpdated Balance: $" + str(treasurerAccount.getAccountBalance))
        parent.switchFrame("treasurerRecentInvoice")

    def __init__(self, parent):
        Frame.__init__(self, parent, name="treasurerDepositMethod")
        self.config(width=1280, height=720)
        self.pack_propagate(False)

        back = Button(self, text="Back to invoice", command=lambda: parent.switchFrame("treasurerRecentInvoice"))
        back.pack(anchor='nw',side=LEFT)

        logout = Button(self, text="Logout", command=lambda: parent.parent.switchFrame("loginChoice"))
        logout.pack(anchor='ne',side=RIGHT)

        paymentMethodPrompt = Label(self, text="Please select an account to deposit into:")
        paymentMethodPrompt.pack(side=TOP)

        treasurerAccountButton = Button(self, text="Club Account\n$" + str(treasurerAccount.getAccountBalance()), command=lambda: self.deposit(parent))
        treasurerAccountButton.pack(side=TOP)
