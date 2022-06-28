import random
import time

# We'll try to make a tv remote control in this file.

# We have to create class.

class tvRemoteControl():

    # define __init__  function
    def __init__(self,tv_status = "off",tv_volume = 0,tv_channel = "Dmax",tv_channel_list = ["Dmax"]):
        self.tv_status = tv_status
        self.tv_volume = tv_volume
        self.tv_channel = tv_channel
        self.tv_channel_list = tv_channel_list
    
    def tvInformations(self):
        print("""
        Informations:
            Status: {}
            Volume: {}
            Channel: {}
        """.format(self.tv_status,self.tv_volume,self.tv_channel))
    
    # tvOn function is for turn on tv
    def tvOn(self, tv_on):
        time.sleep(0.7)
        print("TV is opening.")
        tv_on = "on"
        self.tv_status = tv_on

    # changeVolume function is for changing tv volume
    def changeVolume(self,volume_change_quantity):
        self.tv_volume += volume_change_quantity
        time.sleep(0.4)
        print("Volume: ",self.tv_volume)
    
    # tvOff function is for turn off tv
    def tvOff(self,tv_off):
        time.sleep(0.7)
        print("TV is off.")
        tv_off = "off"
        self.tv_status = tv_off
    
    # addChannel function is for add new channel on Channel list
    def addChannel(self,newChannel):
        newChannel = str(input("Please enter which channel do you want add on Channel List: "))
        self.tv_channel_list.append(newChannel)