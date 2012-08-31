import os.path
import cv
import os
from ConfigFileReader import*
from ResultReport import*

class Point:          #custom class to store points
    X = int()
    Y = int()

    def __init__(self, x, y):
        self.X = x
        self.Y = y

class CompareImgTool:
    RR = ResultReport()
    CR = ConfigFileReader()

    imgL = None
    imgR = None
    imgMask = None
    pixelValue = list()
    dArray = list()

    bL = float();            #blue value of image0
    gL = float();            #green value of image0
    rL = float();            #red value of image0
    bR = float();            #blue value of image1
    gR = float();            #green value of image1
    rR = float();
    bM = float();            #blue value of image1
    gM = float();            #green value of image1
    rM = float();
    bM = 255
    gM = 255
    rM = 255


    def getImgL(self,TestPath_1,fnum,cropY):
        self.imgL = cv.LoadImage (TestPath_1 + str(fnum) + '.png',1)

        imgWidth = int(self.imgL.width)
        imgHeight = int(self.imgL.height)
        crop_Y = int(cropY)

        src_regionL = cv.GetSubRect(self.imgL,(0, crop_Y, imgWidth, imgHeight - crop_Y))
        self.imgL=src_regionL
        #cv.NamedWindow ('mywin')
        #cv.ShowImage ('mywin', self.imgL)
        #cv.WaitKey (0)

    def getMask(self,maskPath,fnum,cropY):
        self.imgMask = None
        if(os.path.exists(maskPath + str(fnum) + '.png')):
            self.imgMask = cv.LoadImage(maskPath + str(fnum) + '.png',1)
            imgWidth = int(self.imgMask.width)
            imgHeight = int(self.imgMask.height)
            crop_Y = int(cropY)
            src_regionMask = cv.GetSubRect(self.imgMask,(0,crop_Y,imgWidth,imgHeight - crop_Y))
            self.imgMask = src_regionMask
            #cv.NamedWindow ('mywi2n')
            #cv.ShowImage ('mywi2n', self.imgMask)
            #cv.WaitKey (0)

    def getImgR(self,TestPath_2,fnum,cropY):
        self.imgR = cv.LoadImage (TestPath_2 + str(fnum) + '.png',1)

        imgWidth = int(self.imgR.width)
        imgHeight = int(self.imgR.height)
        crop_Y = int(cropY)

        src_regionR = cv.GetSubRect(self.imgR,(0,crop_Y,imgWidth,imgHeight - crop_Y))
        self.imgR = src_regionR
        #cv.NamedWindow ('mywi2n')
        #cv.ShowImage ('mywi2n', self.imgR)
        #cv.WaitKey (0)

    def ComparePixel(self, x, y, threshold):                       #checks if pixels at x,y of image0 and image1 have a difference below threshold value
                self.pixelValue = cv.Get2D(self.imgL, y, x);
                self.bL = self.pixelValue[0];
                self.gL = self.pixelValue[1];
                self.rL = self.pixelValue[2];
                self.pixelValue = cv.Get2D(self.imgR, y, x);
                self.bR = self.pixelValue[0];
                self.gR = self.pixelValue[1];
                self.rR = self.pixelValue[2];
                if self.imgMask != None:
                    self.pixelValue = cv.Get2D(self.imgMask, y, x);
                    self.bM = self.pixelValue[0];
                    self.gM = self.pixelValue[1];
                    self.rM = self.pixelValue[2];

                if self.bL - self.bR > -int(threshold) and self.gL - self.gR > -int(threshold) and self.rL - self.rR > -int(threshold):
                    #print(self.bM)
                    #print(self.gM)
                    return True;                                  #difference is below threshold value
                if self.bM == 0 and self.gM == 0 and self.rM == 0:
                    return True
                else:
                    return False;



    def CompareThread(self,threshold): #funuction that compares two images
        outDir = self.CR.getAttribute('CompareImage Setting','Result_folder')
        imgLWidth = self.imgL.width
        imgLHeight = self.imgL.height
        imgRWidth = self.imgR.width
        imgRHeight = self.imgL.height
        self.dArray = []
        if imgLWidth == imgRWidth and imgLHeight == imgRHeight:
            print "computing..."
            iMax = imgLWidth
            jMax = imgLHeight
            for i in range(0, iMax):
                for j in range(0, jMax):
                    if self.ComparePixel(i, j, threshold) == False:          #loop through all pixels to find different ones
                        self.dArray.append(Point(i, j));
        print self.dArray
        self.RR.D_ImgReport(self.dArray,self.imgL,self.imgR,outDir)
