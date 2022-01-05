from microbit import *

def makeBinary(intValue,padding):
    number = intValue
    returnValue = ""
    brightness = 7 #value 0 to 8
    while number >0:
        bit = int(number % 2)
        if bit > 0:
            bit = brightness
        quotient = int(number / 2)
        returnValue = str(bit)+returnValue
        number = quotient
    for i in range(len(returnValue),padding):
        returnValue = "0"+returnValue
    return returnValue

timeAdvance = 0
minuteAdvance = 0
hourAdvance = 0
secondCounter = 0
while True:
    if button_a.was_pressed():
        #advance hours
        hourAdvance = hourAdvance + 1
        if hourAdvance > 23:
            hourAdvance = 0
        timeAdvance = (hourAdvance*60*60*1000)+(minuteAdvance*60*1000)
    elif button_b.was_pressed():
       #advance minutes
       minuteAdvance = minuteAdvance + 1
       if minuteAdvance > 59:
           minuteAdvance = 0
       timeAdvance = (hourAdvance*60*60*1000)+(minuteAdvance*60*1000)
    else:
        #calculate and display time
        if (running_time()-secondCounter) > 1000:
            secondCounter = running_time()
            seconds = (running_time()/1000)%60
            minutes = ((running_time()+timeAdvance)/1000/60)%60
            hours = ((running_time()+timeAdvance)/1000/60/60)%24
            pmString = "0"
            addthirtyMString = "00000"
            addthirtySString = "00000"
            if hours>12:
                pmString = "7"
                hours = hours - 12
            if minutes>29:
                addthirtyMString = "00700"
                minutes = minutes - 30
            if seconds>29:
                addthirtySString = "00700"
                seconds = seconds - 30
            hourString = makeBinary(hours,4)
            minuteString = makeBinary(minutes,5)
            secondString = makeBinary(seconds,5)
            time = Image(pmString+hourString+":"+minuteString+":"+addthirtyMString+":"+secondString+":"+addthirtySString)
            display.show(time)