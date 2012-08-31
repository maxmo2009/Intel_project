
import os
import time
from ConfigFileReader import*

class CaptureImgTool:
    CfReader = ConfigFileReader()

    def CaptureScreen(self,Browser,WebAddress,TimeDelay):
        os.system('adb shell am start -a android.intent.action.VIEW -n '+Browser+' -d '+WebAddress)#browser,address
        time.sleep(TimeDelay)
        os.system('adb shell /system/bin/screencap -p /sdcard/img.png')#need to design file syst

    def SavePic(self,SavePath,PicName):
        os.system('adb pull /sdcard/img.png '+ SavePath + PicName +'.png')
        os.system('echo "Screenshot saved')



