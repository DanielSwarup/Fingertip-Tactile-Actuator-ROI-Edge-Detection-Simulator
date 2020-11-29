from sensor import*

import cv2
import numpy as np

import pygame
pygame.init()
class Camera:
    def __init__(self):
        self.imageCapture = cv2.VideoCapture(0)
        self.mouseX,self.mouseY = pygame.mouse.get_pos()
        self.screen = pygame.display.set_mode([640, 480])
        self.sensorWin = Sensor(self.screen)
        pygame.mouse.set_visible(False)
        pygame.display.set_caption("Tactile Sensor Visualization")
        self.__convertToEdge()
 

    def __convertToEdge(self):
        while True:
            self.__updateMousePos()
            if(self.mouseX<45) or (self.mouseX>600):
                self.mouseX = 320
                self.mouseY = 240
            if(self.mouseY<45) or (self.mouseY>440):
                self.mouseY = 240
                self.mouseX = 320
            self._ , self.image = self.imageCapture.read()
            self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
            
            self.upperLeft = ((self.mouseX-(self.mouseX*2))-40,self.mouseY - 40)
            self.bottomRight = ((self.mouseX-(self.mouseX*2))+40, self.mouseY + 40)

            self.rectImg = self.image[self.upperLeft[1] : self.bottomRight[1], self.upperLeft[0] : self.bottomRight[0]]

            self.sketcherRect = self.rectImg

            self.sketcherRect = self.createMask(self.sketcherRect)

            #Conversion for 3 channels to put back on original image (streaming)
            self.sketcherRectRgb = cv2.cvtColor(self.sketcherRect, cv2.COLOR_GRAY2RGB)

            #Replacing the sketched image on Region of Interest
            self.image[self.upperLeft[1] : self.bottomRight[1], self.upperLeft[0] : self.bottomRight[0]] = self.sketcherRectRgb


            #self.image = self.createMask(self.image)
            self.image = np.rot90(self.image)

            self.image = np.array(self.image)
            self.sensorWin.sensorVisualColor(self.mouseX, self.mouseY,self.image)

            self.image = pygame.surfarray.make_surface(self.image)

            self.screen.blit(self.image, (0,0))
            self.sensorWin.sensorVisualBoarderBox(self.mouseX,self.mouseY)

            pygame.display.flip()
            pygame.display.update()

            

            # #Has user quit game or not
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            if cv2.waitKey(1) == 113:  #q for quit
                break
        self.imageCapture.release()# Close the window
        cv2.destroyAllWindows()# De-allocate any associated memory usage 

    def __updateMousePos(self):
        self.mouseX, self.mouseY = pygame.mouse.get_pos()

    def createMask(self, image):
        self.imgGreyScale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        self.grayScaleBlur = cv2.GaussianBlur(self.imgGreyScale,(7,7),0)
        self.imgCanny = cv2.Canny(self.grayScaleBlur,10,80)
        self._, self.mask = cv2.threshold(self.imgCanny,30,255,cv2.THRESH_BINARY_INV)
        return self.mask