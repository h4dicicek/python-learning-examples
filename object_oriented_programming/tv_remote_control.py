from posixpath import split
import time

# We'll try to make a tv remote control in this file.

# We have to create class.

class tvRemoteControl():

    # define __init__  function
    def __init__(self,tv_status = "off",tv_volume = 0,tv_channel = "1,Dmax",tv_channel_list = ["1,Dmax","2,National Geographic","3,FOX News","4,TLC"]):
        self.tv_status = tv_status
        self.tv_volume = tv_volume
        self.tv_channel = tv_channel
        self.tv_channel_list = tv_channel_list
    
    def tvInformations(self):
        return "TV Status: {} \nTV Volume: {} \nChannel: {} \nChannel List {}".format(self.tv_status,self.tv_volume,self.tv_channel,self.tv_channel_list)
    
    # tvOn function is for turn on tv
    def tvOn(self):
        if (self.tv_status == "on"):
            return "TV still on."
        else:
            time.sleep(0.7)
            self.tv_status = "on"
            return "TV is opening."

    # changeVolume function is for changing tv volume
    def changeVolume(self,changeVolumQuantity):
        if (changeVolumQuantity == "<"):
            if (self.tv_volume != 0):
                self.tv_volume -= 1
                return "TV Volume: {}".format(self.tv_volume)
        elif(changeVolumQuantity == ">"):
            if (self.tv_volume != 100):
                self.tv_volume += 1
                return "TV Volume: {}".format(self.tv_volume)
        else:
            return "TV Volume changed."

    # tvOff function is for turn off tv
    def tvOff(self):
        if (self.tv_status == "off"):
            return "TV still off."
        else:
            time.sleep(0.7)
            self.tv_status = "off"
            return "TV is turning off."

    # addChannel function is for add new channel on Channel list
    def addChannel(self,newChannel):
        self.tv_channel_list.append(newChannel)
   
    # switchChannel function is for switch between of channels.
    def switchChannel(self,newSwitchChannel):
        if (newSwitchChannel == "<"):
            if(self.tv_channel_list != self.tv_channel_list[0]):
                return self.tv_channel_list[-1]
        elif (newSwitchChannel == ">"):
            return self.tv_channel_list[+1]
    
    def switchChannelWithNumber(self,channelNumber):
        leng = len(self.tv_channel_list)
        for i in range(1,leng + 1):
            if (channelNumber == i):
                return self.tv_channel_list[i -1]

    def __len__(self):
        return len(self.tv_channel_list)

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

Press 8 for change channel with number.

Press q for exit.
''')

while True:
    operation = input("Please enter operation: ")

    if (operation == "q"):
        print("Exit from operations.")
        break

    elif (operation == "1"):
        print(tv_remote_control.tvOn())
    
    elif (operation == "2"):
        print(tv_remote_control.tvOff())

    elif (operation == "3"):
        changeVolumQuantity = input("For lower '<': \nFor higher '>': \nExit 'another button': ")
        print(tv_remote_control.changeVolume(changeVolumQuantity))

    elif (operation == "4"):
        newChannel = input("Please enter which channel do you want add on Channel List: ")
        print(tv_remote_control.addChannel(newChannel))
    
    elif (operation == "5"):
        newSwitchChannel = input("Previous Channel '<': \nNext Channel '>': ")
        print(tv_remote_control.switchChannel(newSwitchChannel)) 
    
    elif (operation == "6"):
        print("Number of Channels:",len(tv_remote_control))
           
    elif (operation == "7"):
        print(tv_remote_control.tvInformations())

    elif (operation == "8"):
        channelNumber = int(input("Please enter a channel number: "))
        print(tv_remote_control.switchChannelWithNumber(channelNumber))
    else:
        print("Operation is not found!")