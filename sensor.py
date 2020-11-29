import pygame
pygame.init()


class Sensor:
    def __init__(self, screen):
        #To adjust sensitivity of pixel groups for activation change this. Currently checking is done with if self.sensitivity>average then actuate
        self.sensitivity = 220

        self.sensWinWidth = 200
        self.sensWinHeight = 200
        self.screen = screen
        self.mouseX,self.mouseY = pygame.mouse.get_pos()

        self.circleColor = [(0,0,0),(0,0,0),(0,0,0),(0,0,0),
                            (0,0,0),(0,0,0),(0,0,0),(0,0,0),
                            (0,0,0),(0,0,0),(0,0,0),(0,0,0),
                            (0,0,0),(0,0,0),(0,0,0),(0,0,0)]
        self.circleStrength = [2,2,2,2,
                               2,2,2,2,
                               2,2,2,2,
                               2,2,2,2]
        self.activationColor = (200,200,0)

    def getAvgColor( self, x ,y ,n, image):
        self.r, self.g, self.b = 0, 0, 0
        self.counter = 0
        for i in range(x, x+n+1):
            for j in range(y, y+n+1):
                self.pixlB, self.pixlG, self.pixlR = image[i, j]  
                self.r += self.pixlR
                self.g += self.pixlG
                self.b += self.pixlB
                self.counter += 1
        return ((self.r/self.counter)+(self.g/self.counter)+(self.b/self.counter))/3

    def sensorVisualColor(self, mouseX,mouseY, image):
        #Top Row
        #[0]
        if self.sensitivity> self.getAvgColor(self.mouseX-40,self.mouseY-40,20,image):
            self.circleStrength[0] = 0
            self.circleColor[0] = self.activationColor
        else:
            self.circleStrength[0] = 2
            self.circleColor[0] = (0,0,0)
        #[1]
        if self.sensitivity> self.getAvgColor(self.mouseX-20,self.mouseY-40,20,image):
            self.circleStrength[1] = 0
            self.circleColor[1] = self.activationColor
        else:
            self.circleStrength[1] = 2
            self.circleColor[1] = (0,0,0)
        #[2]
        if self.sensitivity> self.getAvgColor(self.mouseX,self.mouseY-40,20,image):
            self.circleStrength[2] = 0
            self.circleColor[2] = self.activationColor
        else:
            self.circleStrength[2] = 2
            self.circleColor[2] = (0,0,0)
        #[3]
        if self.sensitivity> self.getAvgColor(self.mouseX+20,self.mouseY-40,20,image):
            self.circleStrength[3] = 0
            self.circleColor[3] = self.activationColor
        else:
            self.circleStrength[3] = 2
            self.circleColor[3] = (0,0,0)
        #Second Row
        #[4]
        if self.sensitivity> self.getAvgColor(self.mouseX-40,self.mouseY-20,20,image):
            self.circleStrength[4] = 0
            self.circleColor[4] = self.activationColor
        else:
            self.circleStrength[4] = 2
            self.circleColor[4] = (0,0,0)
        #[5]
        if self.sensitivity> self.getAvgColor(self.mouseX-20,self.mouseY-20,20,image):
            self.circleStrength[5] = 0
            self.circleColor[5] = self.activationColor
        else:
            self.circleStrength[5] = 2
            self.circleColor[5] = (0,0,0)
        #[6]
        if self.sensitivity> self.getAvgColor(self.mouseX,self.mouseY-20,20,image):
            self.circleStrength[6] = 0
            self.circleColor[6] = self.activationColor
        else:
            self.circleStrength[6] = 2
            self.circleColor[6] = (0,0,0)
        #[7]
        if self.sensitivity> self.getAvgColor(self.mouseX+20,self.mouseY-20,20,image):
            self.circleStrength[7] = 0
            self.circleColor[7] = self.activationColor
        else:
            self.circleStrength[7] = 2
            self.circleColor[7] = (0,0,0)      
        #Third Row
        #[8]
        if self.sensitivity> self.getAvgColor(self.mouseX-40,self.mouseY,20,image):
            self.circleStrength[8] = 0
            self.circleColor[8] = self.activationColor
        else:
            self.circleStrength[8] = 2
            self.circleColor[8] = (0,0,0)
        #[9]
        if self.sensitivity> self.getAvgColor(self.mouseX-20,self.mouseY,20,image):
            self.circleStrength[9] = 0
            self.circleColor[9] = self.activationColor
        else:
            self.circleStrength[9] = 2
            self.circleColor[9] = (0,0,0)
        #[10]
        if self.sensitivity> self.getAvgColor(self.mouseX,self.mouseY,20,image):
            self.circleStrength[10] = 0
            self.circleColor[10] = self.activationColor
        else:
            self.circleStrength[10] = 2
            self.circleColor[10] = (0,0,0)
        #[11]
        if self.sensitivity> self.getAvgColor(self.mouseX+20,self.mouseY,20,image):
            self.circleStrength[11] = 0
            self.circleColor[11] = self.activationColor
        else:
            self.circleStrength[11] = 2
            self.circleColor[11] = (0,0,0)       
        #Fourth Row
        #[12]
        if self.sensitivity> self.getAvgColor(self.mouseX-40,self.mouseY+20,20,image):
            self.circleStrength[12] = 0
            self.circleColor[12] = self.activationColor
        else:
            self.circleStrength[12] = 2
            self.circleColor[12] = (0,0,0)
        #[13]
        if self.sensitivity> self.getAvgColor(self.mouseX-20,self.mouseY+20,20,image):
            self.circleStrength[13] = 0
            self.circleColor[13] = self.activationColor
        else:
            self.circleStrength[13] = 2
            self.circleColor[13] = (0,0,0)
        #[14]
        if self.sensitivity> self.getAvgColor(self.mouseX,self.mouseY+20,20,image):
            self.circleStrength[14] = 0
            self.circleColor[14] = self.activationColor
        else:
            self.circleStrength[14] = 2
            self.circleColor[14] = (0,0,0)
        #[15]
        if self.sensitivity> self.getAvgColor(self.mouseX+20,self.mouseY+20,20,image):
            self.circleStrength[15] = 0
            self.circleColor[15] = self.activationColor
        else:
            self.circleStrength[15] = 2
            self.circleColor[15] = (0,0,0) 

    def sensorVisualBoarderBox(self, mouseX, mouseY):
        self.mouseX = mouseX
        self.mouseY = mouseY
        pygame.draw.rect(self.screen, (0, 0, 0), (self.mouseX -40, self.mouseY -40, 80, 80), 1)
 
        #Top Row
        #[0]
        pygame.draw.circle(self.screen,(self.circleColor[0]),(self.mouseX-30,self.mouseY-30),10,self.circleStrength[0])
        #[1]
        pygame.draw.circle(self.screen,(self.circleColor[1]),(self.mouseX-10,self.mouseY-30),10,self.circleStrength[1])
        #[2]
        pygame.draw.circle(self.screen,(self.circleColor[2]),(self.mouseX+10,self.mouseY-30),10,self.circleStrength[2])
        #[3]
        pygame.draw.circle(self.screen,(self.circleColor[3]),(self.mouseX+30,self.mouseY-30),10,self.circleStrength[3])     
        #Second Row
        #[4]
        pygame.draw.circle(self.screen,(self.circleColor[4]),(self.mouseX-30,self.mouseY-10),10,self.circleStrength[4])
        #[5]
        pygame.draw.circle(self.screen,(self.circleColor[5]),(self.mouseX-10,self.mouseY-10),10,self.circleStrength[5])
        #[6]
        pygame.draw.circle(self.screen,(self.circleColor[6]),(self.mouseX+10,self.mouseY-10),10,self.circleStrength[6])
        #[7]
        pygame.draw.circle(self.screen,(self.circleColor[7]),(self.mouseX+30,self.mouseY-10),10,self.circleStrength[7])

        #Third Row
        #[8]
        pygame.draw.circle(self.screen,(self.circleColor[8]),(self.mouseX-30,self.mouseY+10),10,self.circleStrength[8])
        #[9]
        pygame.draw.circle(self.screen,(self.circleColor[9]),(self.mouseX-10,self.mouseY+10),10,self.circleStrength[9])
        #[10]
        pygame.draw.circle(self.screen,(self.circleColor[10]),(self.mouseX+10,self.mouseY+10),10,self.circleStrength[10])
        #[11]
        pygame.draw.circle(self.screen,(self.circleColor[11]),(self.mouseX+30,self.mouseY+10),10,self.circleStrength[11])
        #Fourth Row
        #[12]
        pygame.draw.circle(self.screen,(self.circleColor[12]),(self.mouseX-30,self.mouseY+30),10,self.circleStrength[12])
        #[13]
        pygame.draw.circle(self.screen,(self.circleColor[13]),(self.mouseX-10,self.mouseY+30),10,self.circleStrength[13])
        #[14]
        pygame.draw.circle(self.screen,(self.circleColor[14]),(self.mouseX+10,self.mouseY+30),10,self.circleStrength[14])
        #[15]
        pygame.draw.circle(self.screen,(self.circleColor[15]),(self.mouseX+30,self.mouseY+30),10,self.circleStrength[15])
