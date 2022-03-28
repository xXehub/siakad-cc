import scriptabsen
import values
import pytz
from time import time, sleep
from datetime import datetime


# TIME-SECTION
WIB = pytz.timezone('Asia/Jakarta')
def setTimer(setTime):
    while True: 
        format = '%H:%M:%S'
        now = (datetime.now(WIB)).strftime(format)
        tomorrow = setTime
        timeRemain = datetime.strptime(tomorrow, format) - datetime.strptime(now, format)
        print("> Start at ", tomorrow, " | Time now: ", now, " | Time remaining: ", timeRemain, end="\r")
        sleep(1)
        if(now == tomorrow):
            break 


while True:
    print("="*81)
    print("READY!")
    # setTimer("05:50:00")
    sleep(5 - time() % 5)

    WIB = pytz.timezone('Asia/Jakarta')
    time_now = datetime.now(WIB)

    if (time_now.strftime('%a') != 'Sat' and
        time_now.strftime('%a') != 'Sun'):
    # if True: # Development
        temp = scriptabsen.runscript(values.account(), values.sitelogger(), values.browser())
        times = datetime.now(WIB)
        if(temp == True):
            print("> Absen berhasil pada " + times.strftime('%c'))
        elif(temp == False):
            print("> Absen gagal, SERVER SEKOLAH KENTANK, mencoba lagi " +
                    times.strftime('%c'))
            ass = scriptabsen.runscript(values.account(), values.sitelogger(), values.browser())
            if ass == True:
                timee = datetime.now(WIB)
                print("> Absen berhasil pada " + timee.strftime('%c'))
            else:
                print("> Gagal akses website")
        else:
            print("> Server-mu Down " + times.strftime('%c'))