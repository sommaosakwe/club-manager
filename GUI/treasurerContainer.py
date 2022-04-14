from tkinter import *

from GUI.treasurerFrames.treasurerCoachListFrame import treasurerCoachListFrame
from GUI.treasurerFrames.treasurerPaymentMethodFrame import treasurerPaymentMethodFrame

class treasurerContainer(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent.main, name="memberContainer")
        self.config(width=1280, height=720)
        self.parent = parent

        self.childrenFrames = {
            "treasurerCoachListFrame": treasurerCoachListFrame
        }

        self.currentFrame = treasurerCoachListFrame(self)
        self.currentFrame.pack()

    def switchFrame(self, frameName):
        f = self.childrenFrames[frameName]
        if self.currentFrame is not None:
            self.currentFrame.pack_forget()
        self.currentFrame = f(self)
        self.currentFrame.pack()