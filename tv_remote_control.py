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
    
    def __str__(self):
        return "TV Status: {} \nTV Volume: {} \nChannel: {} \nChannel List {}".format(self.tv_status,self.tv_volume,self.tv_channel,self.tv_channel_list)
    
    # tvOn function is for turn on tv
    def tvOn(self, tv_on):
        if (self.tv_status == "on"):
            print("TV still on.")
        else:
            time.sleep(0.7)
            tv_on = "on"
            self.tv_status = tv_on
            print("TV is opening.")

    # changeVolume function is for changing tv volume
    def changeVolume(self):
        while True:
            changeVolumQuantity = input("For lower '<': \nFor higher '>': ")

            if (changeVolumQuantity == "<"):
                if (self.tv_volume != 0):
                    self.tv_volume -= 1
            
            elif(changeVolumQuantity == ">"):
                if (self.tv_volume != 100):
                    self.tv_volume += 1
            print("TV Volume: {}".format(self.tv_volume))
        
    
    # tvOff function is for turn off tv
    def tvOff(self,tv_off):
        if (self.tv_status == "off"):
            print("TV still off.")
        else:
            time.sleep(0.7)
            tv_off = "off"
            self.tv_status = tv_off
            print("TV is off.")
    
    # addChannel function is for add new channel on Channel list
    def addChannel(self,newChannel):
        newChannel = input("Please enter which channel do you want add on Channel List: ")
        self.tv_channel_list.append(newChannel)
   
    # switchChannel function is for switch between of channels.
    def switchChannel(self):
        switchChannel = random.randint(0,len(self.tv_channel_list)-1)
        self.tv_channel = self.tv_channel_list[switchChannel]
        print("Channel: ",self.tv_channel)

    def __len__(self):
        return(len(self.tv_channel_list))


tv_remote_control = tvRemoteControl()

print('''
TV Operations:

Press 1 for Turn on TV.

Press 2 for Turn off TV.

Press 3 for change TV volume.

Press 4 for Add New Channel.

Press 5 for Change Channel.

Press 6 for learn the number of channels.

Press 7 for TV Informations.

Press 'q' for exit.
''')

while True:
    operation = input("Please enter operation: ")

    if (operation == 'q'):
        print("Exit from operations.")
    
    elif (operation == '1'):
        tv_remote_control.tvOn()
        time.sleep(0.5)
        print("TV is opening")
    
    elif (operation == '2'):
        tv_remote_control.tvOff()
        time.sleep(0.5)
        print("TV is turning off.")