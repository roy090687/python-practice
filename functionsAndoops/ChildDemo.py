# Inheritance
# Base Class: OopsDemo , Child Class:ChildClass
from functionsAndoops.OopsDemo import OopsDemo


class ChildClass(OopsDemo):
    var = 200

    def __init__(self):
        OopsDemo.__init__(self, 3, 5)

    def getCompleteData(self):
        return self.var + self.num + self.summation()


objChild = ChildClass()
print("From Child Class:- ", objChild.getCompleteData())
