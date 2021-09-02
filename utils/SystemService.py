import os, sys
import subprocess
import ctypes
from utils import Logger

from utils.Exception import ServiceNotFound


class CMDService():
    def __init__(self):
        pass

    def is_admin(self):
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    def isAdmin(self):
        result = subprocess.run("net session", stderr=subprocess.PIPE)
        if result.stderr:
            return False
        return True



    def isNSSMInstalled(self):
        try:
            result = subprocess.run("nssm")
        except FileNotFoundError as e:
            print(str(e))
            return False
        return True


    def getServiceStatusDict(self, serviceName):
        statusDict = {}

        result = ""
        if not self.isAdmin():
            raise PermissionError("Please run as administrator")
        try:
            result = subprocess.run("sc queryex {}".format(serviceName), stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            if "FAILED" in str(result.stdout):
                raise ServiceNotFound("Service {} is not installed yet".format(serviceName))

            resultLines = str(result.stdout).split("\\r\\n")
            for line in resultLines:
                if ":" not in line:
                    continue
                line = line.strip()
                lineSplited = line.split(":")
                key = lineSplited[0]
                key = key.replace(" ", "")
                statusDict[key] = lineSplited[1]
            return statusDict

        except ServiceNotFound as e:
            print(str(e))


class NSSMService(CMDService):
    def __init__(self):
        super().__init__()

    def startService(self, serviceName):
        cmdStr = "nssm start {}".format(serviceName)
        logger = Logger.getLogger()
        logger.info(cmdStr)
        result = subprocess.run(cmdStr, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.stderr:
            return result.stderr
        return result.stdout

    def stopService(self, serviceName):
        cmdStr = "nssm stop {}".format(serviceName)
        logger = Logger.getLogger()
        logger.info(cmdStr)
        result = subprocess.run(cmdStr, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.stderr:
            return result.stderr
        return result.stdout

    def restartService(self, serviceName):
        cmdStr = "nssm restart {}".format(serviceName)
        logger = Logger.getLogger()
        logger.info(cmdStr)
        result = subprocess.run(cmdStr, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.stderr:
            return result.stderr
        return result.stdout




if __name__ == "__main__":
    cmdService = CMDService()
    a = cmdService.getServiceStatusDict("mixsonService2")
    print(a)
    # print(cmdService.is_admin())
    # a = cmdService.getServiceStatusDict("abc")
    nssmService = NSSMService()
    nssmService.restartService("mixsonService2")
    b = cmdService.getServiceStatusDict("mixsonService2")
    print(b)