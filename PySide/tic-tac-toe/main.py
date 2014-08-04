#__|__|__
#__|__|__
#  |  | 



class play(object):
    def __init__(self):
        self._place1=""
        self._place2=""
        self._place3=""
        self._place4=""
        self._place5=""
        self._place6=""
        self._place7=""
        self._place8=""
        self._place9=""
    
    def setPlace1(self, value):
        self._place1=value
    def setPlace2(self, value):
        self._place2=value
    def setPlace3(self, value):
        self._place3=value
    def setPlace4(self, value):
        self._place4=value
    def setPlace5(self, value):
        self._place5=value
    def setPlace6(self, value):
        self._place6=value
    def setPlace7(self, value):
        self._place7=value
    def setPlace8(self, value):
        self._place8=value
    def setPlace9(self, value):
        self._place9=value
        
    def getPlace1(self):
        return self._place1
    def getPlace2(self):
        return self._place2
    def getPlace3(self):
        return self._place3
    def getPlace4(self):
        return self._place4
    def getPlace5(self):
        return self._place5
    def getPlace6(self):
        return self._place6
    def getPlace7(self):
        return self._place7
    def getPlace8(self):
        return self._place8
    def getPlace9(self):
        return self._place9
    
    def Print(self):
        print self._place1, "|", self._place2, "|", self._place3
        print self._place4, "|", self._place5, "|", self._place6
        print self._place7, "|", self._place8, "|", self._place9
    
    