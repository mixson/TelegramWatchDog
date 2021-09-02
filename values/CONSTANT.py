RunningServerIp = "127.0.0.1"
# RunningServerIp = "10.39.64.26"
# RunningServerIp = "10.39.64.28"
# RunningServerIp = "10.39.64.30"

class MySelfServiceInfo:
    IP = "127.0.0.1"
    ServiceNameList = ["mixsonService2", "TelegramWatchDogService"]
    HealthTestClassList = []
    botTelegramKey = "1793814419:AAEQBMQq9YaBxLg23NQ-g3NXSuMAhWIrSjo"

class UATServiceInfo:
    IP = "10.39.64.26"
    ServiceNameList = ["protekService", "TelegramWatchDogService", "protekServiceTransition"]
    HealthTestClassList = []
    botTelegramKey = "1670008316:AAF_njgNiImyQ8xFZlqNFwcYtxqAjj3HSTE"

class ProductionServiceInfo:
    IP = "10.39.64.28"
    ServiceNameList = ["protekRegularService", "protekRegularServiceTelegram", "TelegramWatchDogService", "stagingTelegramView", "protekRegularServiceTelegramTransition"]
    HealthTestClassList = []
    botTelegramKey = "1811414419:AAFWa_U56JInzqd4VDX5Wph8df2xs2RgKUM"

class StandByServiceInfo:
    IP = "10.39.64.30"
    ServiceNameList = ["protekService", "TelegramWatchDogService", "protekServiceTransition"]
    HealthTestClassList = []
    botTelegramKey = "1840521479:AAEJD8hRV2fB5MmQoTdd1fwdNSqZLTDeotI"



DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"