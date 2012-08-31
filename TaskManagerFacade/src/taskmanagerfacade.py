from CaptureImgTool import* 
from ConfigFileReader import*
from CompareImgTool import*
from ResultReport import*
import shutil
import os
import sys



class TaskManagerFacade:
    CS = CaptureImgTool()
    CR = ConfigFileReader()
    CI = CompareImgTool()


    def ExecuteUnit_maskImgLoad(self):
        mskFld = self.CR.getAttribute('CompareImage Setting','Mask_folder')
        Crop_Y = self.CR.getAttribute('CaptureImage Setting','Crop_X')
        self.CI.getMask(mskFld,0,Crop_Y)

    def Execute_compareImgTst(self):#need add mask modeul
        print 'ExecuteUnit_compareImgTst'
        Tst_fld_1 = self.CR.getAttribute('CompareImage Setting','Test_folder_1')
        Tst_fld_2 = self.CR.getAttribute('CompareImage Setting','Test_folder_2')
        mskFld = self.CR.getAttribute('CompareImage Setting','Mask_folder')
        Thd = self.CR.getAttribute('CompareImage Setting','Threshold')
        Crop_Y = self.CR.getAttribute('CaptureImage Setting','Crop_X')
        webpage_amount = self.CR.getAttribute('General Setting','Test_webpage_amount')
        for i in range(int(webpage_amount)):
            self.CI.getImgL(Tst_fld_1,i,Crop_Y)
            self.CI.getImgR(Tst_fld_2,i,Crop_Y)
            self.CI.getMask(mskFld,i,Crop_Y)
            self.CI.CompareThread(Thd)

    def ExecuteUnit_getImg(self):
        print 'ExecuteUnit_getImg'
        self.CR.getFile()
        Tst_fld_1 = self.CR.getAttribute('Test_folder_1')
        Tst_fld_2 = self.CR.getAttribute('Test_folder_2')
        self.CI.getImgL(Tst_fld_1,2,50)
        self.CI.getImgR(Tst_fld_2,2,50)

    
    def System_init(self,DDir1,DDir2):
        shutil.rmtree(DDir1)
        shutil.rmtree(DDir2)

    def ExecuteUnit_quit_shell(self):
        print'ExecuteUnit_quit_shell'
        os.system('quit')

    def ExecuteUnit_exit_shell(self):
        print'ExecuteUnit_exit_shell'
        os.system('exit')

    def ExecuteUnit_captureScreen(self):
        print'ExecuteUnit_captureScreen'
        self.CS.CaptureScreen('com.android.browser/.BrowserActivity','html5doctor.com',20)

    def ExecuteUnit_configReader(self):
        print'ExecuteUnit_configReader'
        print self.CR.getAttribute('CaptureImage Setting','Saved_picture_Path_for_brw1')

    def Execute_captureScreen(self):
        print 'Execute_captureScreen'
        PC_info = self.CR.getAttribute('General Setting','PC_Platform_version')
        And_info = self.CR.getAttribute('General Setting','Android_Platform_version')
        Test_amount = self.CR.getAttribute('General Setting','Test_webpage_amount')
        Test_webpage_path = self.CR.getAttribute('General Setting','Test_webpage_folder_path')
        Test_browser_1 = self.CR.getAttribute('General Setting','Test_webbrowser_instance_1_activity_name')
        Test_browser_2 = self.CR.getAttribute('General Setting','Test_webbrowser_instance_2_activity_name')
        Timer = self.CR.getAttribute('CaptureImage Setting','Time_delay')
        Saved_pic_path_1 = self.CR.getAttribute('CaptureImage Setting','Saved_picture_Path_for_brw1')
        Saved_pic_path_2 = self.CR.getAttribute('CaptureImage Setting','Saved_picture_Path_for_brw2')

        try:
            Website_file = open(Test_webpage_path)
        except IOError:
            print "please input a valid website test field file"
            return False
        web_list = []
        web_list = Website_file.readlines()
        for i in range(int(Test_amount)):
            self.CS.CaptureScreen(Test_browser_1,web_list[i],float(Timer))
            self.CS.SavePic(Saved_pic_path_1,str(i))
        for i in range(int(Test_amount)):
            self.CS.CaptureScreen(Test_browser_2,web_list[i],float(Timer))
            self.CS.SavePic(Saved_pic_path_2,str(i))
        print 'CaptureScreen finished'

      
if __name__ == "__main__":
    print "This is TaskManagerfacade working"
    TMF = TaskManagerFacade()
   
    if "-sc" in sys.argv[1]:
        TMF.Execute_captureScreen()
    if "-t" in sys.argv[1]:
        TMF.Execute_captureScreen()
        TMF.Execute_compareImgTst()
    if "-ci" in sys.argv[1]:
        TMF.Execute_compareImgTst()

    #TMF.ExecuteUnit_maskImgLoad()
   