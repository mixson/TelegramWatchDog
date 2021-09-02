import os, sys
import ast
import socket
import datetime
import traceback

currentDir = "\\".join(os.getcwd().split("\\")[0:-1])
sys.path.insert(0, currentDir)

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

from values import CONSTANT
from utils import SystemService
from utils import SocketService
from utils import Logger

def getServiceInfo():
    # runningServiceIP = CONSTANT.RunningServerIp
    runningServiceIP = SocketService.getIpAddress()

    if runningServiceIP == "10.39.64.26":
        return CONSTANT.UATServiceInfo
    if runningServiceIP == "10.39.64.28":
        return CONSTANT.ProductionServiceInfo
    if runningServiceIP == "10.39.64.30":
        return CONSTANT.StandByServiceInfo

    return CONSTANT.MySelfServiceInfo

logger = Logger.getLogger()

serverInfo = getServiceInfo()
print(serverInfo.IP)
print(serverInfo.botTelegramKey)
print(serverInfo.__class__.__name__)
logger.info(serverInfo.IP)
logger.info(serverInfo.botTelegramKey)
logger.info(serverInfo.__class__.__name__)
updater = Updater(token=serverInfo.botTelegramKey, use_context=False)
# updater = Updater(token="1793814419:AAEQBMQq9YaBxLg23NQ-g3NXSuMAhWIrSjo", use_context=False)



def runCmd(cmd):
    return os.system(cmd)


def getServiceStatusMsg():
    msg = ""
    nssmService = SystemService.NSSMService()

    for serviceName in serverInfo.ServiceNameList:
        serviceStatusDict = nssmService.getServiceStatusDict(serviceName)
        msg += str(serviceStatusDict) + "\n\n"

    return msg

def CM_getServiceStatus(bot, update):
    print("getServiceStatus")
    msg = "{}\n\n".format(datetime.datetime.now().strftime(CONSTANT.DATETIME_FORMAT))

    msg += getServiceStatusMsg()

    bot.send_message(update.message.chat.id, msg, parse_mode=ParseMode.HTML)

def CM_startService(bot, update):
    try:
        msg = "{}\n\n".format(datetime.datetime.now().strftime(CONSTANT.DATETIME_FORMAT))

        logger = Logger.getLogger()
        inputText = update.message.text

        userInfoLog = str(update.effective_message.chat)
        loggingMsg = "{}\n{}".format(inputText, userInfoLog)
        logger.debug(loggingMsg)

        clearedInputText = inputText.split(" ")[-1:]
        targetServiceName = clearedInputText[0]

        if targetServiceName not in serverInfo.ServiceNameList:
            msg += "{} is not in the ServiceList".format(targetServiceName)
            bot.send_message(update.message.chat.id, msg, parse_mode=ParseMode.HTML)
            return None

        nssmService = SystemService.NSSMService()
        nssmService.startService(targetServiceName)


        statusDict = nssmService.getServiceStatusDict(targetServiceName)
        msg += str(statusDict)

        bot.send_message(update.message.chat.id, msg, parse_mode=ParseMode.HTML)
    except Exception as e:
        logger.error(str(e))
        logger.error(msg)
        logger.error(traceback.format_exc())

def CM_stopService(bot, update):
    try:
        msg = "{}\n\n".format(datetime.datetime.now().strftime(CONSTANT.DATETIME_FORMAT))

        logger = Logger.getLogger()
        inputText = update.message.text

        userInfoLog = str(update.effective_message.chat)
        loggingMsg = "{}\n{}".format(inputText, userInfoLog)
        logger.debug(loggingMsg)

        clearedInputText = inputText.split(" ")[-1:]
        targetServiceName = clearedInputText[0]

        if targetServiceName not in serverInfo.ServiceNameList:
            msg += "{} is not in the ServiceList".format(targetServiceName)
            bot.send_message(update.message.chat.id, msg, parse_mode=ParseMode.HTML)
            return None

        nssmService = SystemService.NSSMService()
        nssmService.stopService(targetServiceName)


        statusDict = nssmService.getServiceStatusDict(targetServiceName)
        msg += str(statusDict)

        bot.send_message(update.message.chat.id, msg, parse_mode=ParseMode.HTML)
    except Exception as e:
        logger.error(str(e))
        logger.error(msg)
        logger.error(traceback.format_exc())

def CM_restartService(bot, update):
    try:
        msg = "{}\n\n".format(datetime.datetime.now().strftime(CONSTANT.DATETIME_FORMAT))

        logger = Logger.getLogger()
        inputText = update.message.text

        userInfoLog = str(update.effective_message.chat)
        loggingMsg = "{}\n{}".format(inputText, userInfoLog)
        logger.debug(loggingMsg)

        clearedInputText = inputText.split(" ")[-1:]
        targetServiceName = clearedInputText[0]

        if targetServiceName not in serverInfo.ServiceNameList:
            msg += "{} is not in the ServiceList".format(targetServiceName)
            bot.send_message(update.message.chat.id, msg, parse_mode=ParseMode.HTML)
            return None

        nssmService = SystemService.NSSMService()
        nssmService.restartService(targetServiceName)


        statusDict = nssmService.getServiceStatusDict(targetServiceName)
        msg += str(statusDict)

        bot.send_message(update.message.chat.id, msg, parse_mode=ParseMode.HTML)
    except Exception as e:
        logger.error(str(e))
        logger.error(msg)
        logger.error(traceback.format_exc())

def initTGHandler(updater):
    current_module = sys.modules[__name__]
    allFunctionName = getFileFunctionName(__file__)
    for function in allFunctionName:
        functionName = function.name
        if "CM_" in functionName:
            tgCMD = functionName[3:]
            # print(tgCMD)
            addTGHandler(updater, tgCMD, getattr(current_module, functionName))

def getFileFunctionName(filename):
    print(filename)
    with open(filename) as file:
        node = ast.parse(file.read())
    classes = [n for n in node.body if isinstance(n, ast.FunctionDef)]
    return classes

def addTGHandler(updater, name, function):
    updater.dispatcher.add_handler(CommandHandler(name, function))

if __name__ == "__main__":

    initTGHandler(updater)
    updater.start_polling()
    updater.idle()
