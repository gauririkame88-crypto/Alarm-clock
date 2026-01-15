#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
import datetime as dt
import time
import winsound as ws
from threading import Thread


def threading():
    t1 = Thread(target = alarm)
    t1.start()

def alarm():
    #infinite loop
    while True:
        #Set alarm time
        set_time = f'{hour.get()}:{minute.get()}:{second.get()}'
        #wait for 1 sec
        time.sleep(1)
        #get current time from sytem
        curr_time = dt.datetime.now().strftime('%H:%M:%S')
        print(curr_time,set_time)
        if curr_time == set_time:
            print("Wake UPP!!!")
            ws.PlaySound("C:\\Users\\shree\\Downloads\\Telegram Desktop\\morning_flower", ws.SND_ASYNC)

def update_time():
    curr_time = dt.datetime.now().strftime('%H:%M:%S')
    Alarm.after(1000,update_time)
#object of tkinter
Alarm = Tk()
Alarm.geometry('600x400')# will create a window of size 600 x 400


#adding labels to window
Label(Alarm, text = "MY ALARM CLOCK", font = ("Calibri 20 bold"), fg = 'green').pack(pady = 10)
Label(Alarm, text = "Set Time", font = ("Calibri 16 bold"), fg = 'blue').pack()
frame = Frame(Alarm)
frame.pack()

hour = StringVar(Alarm)
#stringvar()
hours = ('00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23')
#
hour.set(hours[0])


hr = OptionMenu(frame,hour,*hours)




hr.pack(side=LEFT)



minute = StringVar(Alarm)
minutes = ('00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40',
          '41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60')

minute.set(minutes[0])
mins = OptionMenu(frame,minute,*minutes)
mins.pack(side = LEFT)

second =StringVar(Alarm)
seconds = ('00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40',
          '41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60')

second.set(seconds[0])
mins = OptionMenu(frame,second,*seconds)
mins.pack(side = LEFT)

Button(Alarm, text = 'Set Alarm',font = ("Calibri 16 bold"), command = threading).pack(pady = 20)
Alarm.after(1000,update_time)
Alarm.mainloop()


# In[1]:


from tkinter import *
import datetime as dt
import time
import winsound as ws
from threading import Thread

# Global flag to control alarm
alarm_running = False
snooze_time = None

def threading():
    t1 = Thread(target=alarm)
    t1.start()

def alarm():
    global alarm_running, snooze_time
    alarm_running = True
    while alarm_running:
        # Set alarm time
        set_time = f'{hour.get()}:{minute.get()}:{second.get()} {am_pm.get()}'
        time.sleep(1)
        # Get current time in 12-hour format
        curr_time = dt.datetime.now().strftime('%I:%M:%S %p')
        print(curr_time, set_time)

        # If snooze is active, override set_time
        if snooze_time:
            set_time = snooze_time

        # Alarm trigger
        if curr_time == set_time:
            print("Wake UPP!!!")
            ws.PlaySound("C:\\Users\\shree\\Downloads\\tum prem ho .wav", ws.SND_ASYNC)


def stop_alarm():
    """Stops the alarm sound completely"""
    global alarm_running, snooze_time
    alarm_running = False
    snooze_time = None
    ws.PlaySound(None, ws.SND_PURGE)  # Stop any sound
    print("Alarm Stopped")

def snooze_alarm():
    """Stops the alarm sound and snoozes for 5 minutes"""
    global snooze_time
    ws.PlaySound(None, ws.SND_PURGE)  # Stop current sound
    # Add 5 minutes to current time and format to 12-hour with AM/PM
    snooze_dt = (dt.datetime.now() + dt.timedelta(minutes=1)).strftime('%I:%M:%S %p')
    snooze_time = snooze_dt
    print(f"Snoozed! Next alarm at {snooze_time}")

def update_time():
    curr_time = dt.datetime.now().strftime('%I:%M:%S %p')
    # Update again after 1 second
    Alarm.after(1000, update_time)

# Tkinter GUI
Alarm = Tk()
Alarm.geometry('600x400')
Alarm.title("Alarm Clock")

# Labels
Label(Alarm, text="MY ALARM CLOCK", font=("Calibri 20 bold"), fg='green').pack(pady=10)
Label(Alarm, text="Set Time (12-Hour Format)", font=("Calibri 16 bold"), fg='blue').pack()
frame = Frame(Alarm)
frame.pack()

# Hours dropdown (1–12)
hour = StringVar(Alarm)
hours = tuple(f"{i:02d}" for i in range(1, 13))
hour.set(hours[0])
OptionMenu(frame, hour, *hours).pack(side=LEFT)

# Minutes dropdown
minute = StringVar(Alarm)
minutes = tuple(f"{i:02d}" for i in range(60))
minute.set(minutes[0])
OptionMenu(frame, minute, *minutes).pack(side=LEFT)

# Seconds dropdown
second = StringVar(Alarm)
seconds = tuple(f"{i:02d}" for i in range(60))
second.set(seconds[0])
OptionMenu(frame, second, *seconds).pack(side=LEFT)

# AM/PM selector
am_pm = StringVar(Alarm)
am_pm.set("AM")
OptionMenu(frame, am_pm, "AM", "PM").pack(side=LEFT)

# Buttons
Button(Alarm, text='Set Alarm', font=("Calibri 16 bold"), command=threading).pack(pady=10)
Button(Alarm, text='Stop Alarm', font=("Calibri 16 bold"), fg="red", command=stop_alarm).pack(pady=5)
Button(Alarm, text='Snooze (1 min)', font=("Calibri 16 bold"), fg="blue", command=snooze_alarm).pack(pady=5)

# Start time updater
Alarm.after(1000, update_time)
Alarm.mainloop()

