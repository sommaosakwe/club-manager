from tkinter import *

from GUI.treasurerFrames.treasurerCoachListFrame import treasurerCoachListFrame
from GUI.treasurerFrames.treasurerNotificationsFrame import treasurerNotificationsFrame
from GUI.treasurerFrames.treasurerGlobalInvoiceFrame import treasurerGlobalInvoiceFrame
from GUI.treasurerFrames.treasurerRecentInvoiceFrame import treasurerRecentInvoiceFrame
from GUI.treasurerFrames.treasurerPaymentMethodFrame import treasurerPaymentMethodFrame
from GUI.treasurerFrames.treasurerWeekChangeFrame import treasurerWeekChangeFrame

class treasurerContainer(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent.main, name="treasurerContainer")
        self.config(width=1280, height=720)
        self.parent = parent

        self.childrenFrames = {
            "treasurerCoachList": treasurerCoachListFrame,
            "treasurerRecentInvoice": treasurerRecentInvoiceFrame,
            "treasurerGlobalInvoice": treasurerGlobalInvoiceFrame,
            "treasurerNotifications": treasurerNotificationsFrame,
            "treasurerWeekChange": treasurerWeekChangeFrame,
            "treasurerPaymentMethod": treasurerPaymentMethodFrame
        }

        self.currentFrame = treasurerCoachListFrame(self)
        self.currentFrame.pack()

    def switchFrame(self, frameName):
        f = self.childrenFrames[frameName]
        if self.currentFrame is not None:
            self.currentFrame.pack_forget()
        self.currentFrame = f(self)
        self.currentFrame.pack()