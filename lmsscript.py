import datetime
from selenium import webdriver 

import time as t


TimeTable = {"monday" : {'2:32' : 'https://tiet.zoom.us/my/csed6'}
}


def link(timetable,time):
    if time in timetable:
        link=timetable[time]
        return link
    else:
        nextime = timetable.get(time) or timetable[ 
        min(timetable.keys(), key = lambda key: abs(key-time))]
        sleep(nextime)

        
        

def main():
    driver =  webdriver.Chrome("chromedriver")
    now = datetime.datetime.now()
    day = now.strftime("%A")
    time = f"{now.hour}:{now.minute}"   
    #opens link according to day and time 
    timetable = Timetable[day]
    link = link(timetable,time) #returns link according tpo thi time 
    openzoom(link)

def openzoom(link):
    driver =  webdriver.Chrome("chromedriver")
    driver.get(link)
    
def sleep(time):
    nowtime = now.hour*60*60+now.minute*60
    t = time.split(:)
    t = t[0]*60*60+t[1]*60
    t.sleep(t-nowtime)
    main()  
    
    

if __name__ == "__main__":
    main()
 