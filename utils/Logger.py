import os
import datetime
import logging

currentDir = "\\".join(os.getcwd().split("\\")[0:-1])
loggingDirPath = os.path.join(currentDir, "log")


def getLogger():

    today = datetime.datetime.now()
    todayStr = "{}_{}_{}".format(today.year, today.month, today.day)
    fileName = "{}_{}.txt".format("DailyRouteLog", "{}".format(todayStr))
    # config
    logging.captureWarnings(True)
    # formatter = logging.Formatter('[%(asctime)s] (%(levelname)s) %(message)s')
    formatter = logging.Formatter('[%(asctime)s] p%(process)s {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s')
    myLogger = logging.getLogger("py.warnings")
    myLogger.setLevel(logging.NOTSET)

    if not os.path.exists(loggingDirPath):
        os.makedirs(loggingDirPath)

    if str(os.path.join(loggingDirPath, fileName)) in [handler.baseFilename for handler in myLogger.handlers if hasattr(handler, "baseFilename")]:
        myLogger.handlers = []

    fileHandler = logging.FileHandler(os.path.join(loggingDirPath, fileName))
    fileHandler.setFormatter(formatter)
    myLogger.addHandler(fileHandler)

    consoleHandler = logging.StreamHandler()
    consoleHandler.setLevel(logging.DEBUG)
    consoleHandler.setFormatter(formatter)
    myLogger.addHandler(consoleHandler)

    return myLogger

if __name__ == "__main__":
    a = []
    for _ in range(3):
        a.append(getLogger())

    print("")