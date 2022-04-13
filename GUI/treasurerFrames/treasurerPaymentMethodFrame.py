from tkinter import *

class treasurerPaymentMethodFrame(Frame):

    def getAccountBalance(self):
        return 100

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

        treasurerAccountButton = Button(self, text="Club Account\n$" + str(self.getAccountBalance()), command=lambda:print("Paid $"+ str(amount)))
        treasurerAccountButton.pack(side=TOP)
