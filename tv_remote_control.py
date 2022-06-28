# We'll try to make a tv remote control in this file.

# We have to create class.

class tvRemoteControl():

    # define __init__  function
    def __init__(self,tv_status = "off",tv_volume = 0,tv_channel = "Dmax",tv_channel_list = "Dmax"):
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
    
    def tvOn(self, tv_on):
        print("TV is opening.")
        tv_on = "on"
        self.tv_status = tv_on

    def changeVolume(self,volume_change_quantity):
        self.tv_volume += volume_change_quantity
        print("Volume: ",self.tv_volume)