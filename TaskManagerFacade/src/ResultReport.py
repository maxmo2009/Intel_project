import cv






class ResultReport:
    RdArray = list()
    pm = 0
    def D_ImgReport(self,dArray,imgL,imgR,outDir):
        i0 = imgL
        i1 = imgR
        iMax = dArray.__len__()
        BlankImg = None
        self.BlankImg = cv.CreateImage((imgL.width,imgL.height), 32, 1)
        for i in range(0, iMax):
            #color0 = cv.Get2D(i0, dArray[i].Y, dArray[i].X)[0]
            #color1 = cv.Get2D(i0, dArray[i].Y, dArray[i].X)[1]
            #color2 = cv.Get2D(i0, dArray[i].Y, dArray[i].X)[2]
            #cv.Set2D(i0, dArray[i].Y, dArray[i].X, [color0 + 150, color1 - 50, color2 - 50, 0])
            #color0 = cv.Get2D(i1, dArray[i].Y, dArray[i].X)[0]
            #color1 = cv.Get2D(i1, dArray[i].Y, dArray[i].X)[1]
            #color2 = cv.Get2D(i1, dArray[i].Y, dArray[i].X)[2]
            cv.Set2D(self.BlankImg,dArray[i].Y, dArray[i].X, 255)
        if dArray !=[]:
            cv.SaveImage(outDir + str(self.pm) +'_diff.jpg', self.BlankImg)
            cv.SaveImage(outDir + str(self.pm) +'_org.jpg', imgL)
            cv.SaveImage(outDir + str(self.pm) +'_src.jpg', imgR)
            print 'a diff_picture has been saved'
            print 'a org_picture has been saved'
            print 'a src_picture has been saved'
        self.pm = self.pm+1
        print 'Report done!'


