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
        print("TV Status: {} \nTV Volume: {} \nChannel: {} \nChannel List {}".format(self.tv_status,self.tv_volume,self.tv_channel,self.tv_channel_list))
    
    # tvOn function is for turn on tv
    def tvOn(self):
        if (self.tv_status == "on"):
            print("TV still on.")
        else:
            time.sleep(0.7)
            self.tv_status = "on"
            print("TV is opening.")

    # changeVolume function is for changing tv volume
    def changeVolume(self):
        while True:
            changeVolumQuantity = input("For lower '<': \nFor higher '>': \nExit 'another button': ")

            if (changeVolumQuantity == "<"):
                if (self.tv_volume != 0):
                    self.tv_volume -= 1
                    print("TV Volume: {}".format(self.tv_volume))
            elif(changeVolumQuantity == ">"):
                if (self.tv_volume != 100):
                    self.tv_volume += 1
                    print("TV Volume: {}".format(self.tv_volume))
            else:
                print("TV Volume changed.")
                break

    # tvOff function is for turn off tv
    def tvOff(self):
        if (self.tv_status == "off"):
            print("TV still off.")
        else:
            time.sleep(0.7)
            print("TV is turning off.")
            self.tv_status = "off"

    # addChannel function is for add new channel on Channel list
    def addChannel(self):
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

Press q for exit.
''')

while True:
    operation = input("Please enter operation: ")

    if (operation == "q"):
        print("Exit from operations.")
        break

    elif (operation == "1"):
        tv_remote_control.tvOn()
    
    elif (operation == "2"):
        tv_remote_control.tvOff()

    elif (operation == "3"):
        tv_remote_control.changeVolume()

    elif (operation == "4"):
        tv_remote_control.addChannel()
    
    elif (operation == "5"):
        tv_remote_control.switchChannel()   
    
    elif (operation == "6"):
        print("Number of Channels:",len(tv_remote_control))
           
    elif (operation == "7"):
        tv_remote_control.tvInformations()
    
    else:
        print("Operation is not found!")