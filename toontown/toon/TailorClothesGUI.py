from toontown.makeatoon import ClothesGUI
from . import ToonDNA


class TailorClothesGUI(ClothesGUI.ClothesGUI):
    notify = directNotify.newCategory('MakeClothesGUI')

    def __init__(self, doneEvent, swapEvent, tailorId):
        ClothesGUI.ClothesGUI.__init__(
            self, ClothesGUI.CLOTHES_TAILOR, doneEvent, swapEvent)
        self.tailorId = tailorId

    def setupScrollInterface(self):
        self.dna = self.toon.getStyle()
        if self.swapEvent != None:
            self.tops = ToonDNA.getTops(tailorId=self.tailorId)
            self.bottoms = ToonDNA.getBottoms(tailorId=self.tailorId)
           
            self.topChoice = -1
            self.bottomChoice = -1
        self.setupButtons()
        return
