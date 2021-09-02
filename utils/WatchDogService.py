

class WatchDogService():

    def __init__(self):
        self.serviceInfo = None

    def setServiceInfo(self, serviceInfo):
        self.serviceInfo = serviceInfo
        return self

    def getRunningStatusMsg(self):
        pass
