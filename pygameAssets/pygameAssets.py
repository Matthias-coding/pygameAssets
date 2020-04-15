import pygame
from pygame.locals import *
from math import sqrt
scrn = None

def getRect(surf, align, x, y):
    if align == 'center':
        return surf.get_rect(center=(x,y))
    elif align == 'topleft':
        return surf.get_rect(topleft=(x,y))
    elif align == 'bottomleft':
        return surf.get_rect(bottomleft=(x,y))    
    




class TextBox:
    screen = None
    def __init__(self, x, y, text = '', color = (0,0,0), fontSize = 60, fontFamily = None, align ='center', screen=None):
        super().__init__()       
        self.align = align
        self.color = color
        self.x = x
        self.y = y
        self.font = pygame.font.Font(fontFamily, fontSize)
        self.setText(text)

        self.screen = None

        if screen is not None:
            self.screen = screen



    def setText(self, text):
        self.text_surf = self.font.render(text, True, self.color)
        self.rect = getRect(self.text_surf, self.align,self.x, self.y)

    

    def draw(self, screen=None):
        if screen is not None:
            self.screen = screen
        elif Button.screen is not None and self.screen is None:
            self.screen = TextBox.screen

        self.screen.blit(self.text_surf, self.rect)

    def setPosition(self, x, y):
        self.rect = getRect(self.text_surf, self.align,x,y)

    @staticmethod
    def setScreen(screen):
        TextBox.screen = screen
        

class Button:
    screen = None
    def __init__(self, x, y, w, h, color = (102,102,102), activeColor = (150,150,150), text = '', textColor = (255,255,255), fontSize = 30, fontFamily = None, align='center', screen=None):
        super().__init__()
        self.surf = pygame.Surface((w,h))
        self.surf.fill(color)
        self.rect = getRect(self.surf, align, x, y)
        self.color = color
        self.activeColor = activeColor
        self.textColor = textColor
        self.align = align
        self.font = pygame.font.Font(fontFamily, fontSize)
        self.x = x
        self.y = y

        self.screen = None

        if screen is not None:
            self.screen = screen
            
        self.setText(text)
        
        

    def draw(self,screen=None):
        if screen is not None:
            self.screen = screen
        elif Button.screen is not None and self.screen is None:
            self.screen = Button.screen
        

        self.screen.blit(self.surf, self.rect)   
        self.screen.blit(self.text_surf, self.text_rect) 
    
    def setText(self, text):
        self.text = text
        self.text_surf = self.font.render(self.text, True, self.textColor)
        self.text_rect = getRect(self.text_surf, self.align, self.x, self.y)
        self.rect.center = self.text_rect.center

    def setPosition(self, x, y):
        self.x = x
        self.y = y
        self.setText(self.text)

    def setColor(self, color):
        self.color = color
        self.surf.fill(color)

    def isPressed(self, event):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                return True
            self.surf.fill(self.activeColor)
        else:
            self.surf.fill(self.color)
        return False

    @staticmethod
    def setScreen(screen):
        Button.screen = screen


class InputBox:
    screen = None
    def __init__(self,x, y, w, h, color = (200,200,200), activeColor = (200,200,200), text = '', textColor = (0,0,0), fontSize = 30, fontFamily = None, align='center', screen=None):
        super().__init__()
        self.surf = pygame.Surface((w,h))
        self.surf.fill(color)
        self.rect = getRect(self.surf, align, x, y)

        self.active = False
        self.text = text

        self.color = color
        self.activeColor = activeColor
        self.textColor = textColor
        self.align = align
        self.font = pygame.font.Font(fontFamily, fontSize)
        self.x = x
        self.y = y

        if screen is not None:
            self.screen = screen

        self.setText(text)

    def setText(self, text):
        self.text = text
        self.text_surf = self.font.render(self.text, True, self.textColor)
        self.text_rect = getRect(self.text_surf, self.align, self.x, self.y)
        self.rect.center = self.text_rect.center

    def draw(self, screen=None):
        if screen is not None:
            self.screen = screen
        elif Button.screen is not None and self.screen is None:
            self.screen = InputBox.screen

        self.screen.blit(self.surf, self.rect)   
        self.screen.blit(self.text_surf, self.text_rect) 

    def handle_event(self,event):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                self.active = not self.active

            if event.type == KEYDOWN:
                if self.active:
                    if event.key == K_RETURN:
                        return 'submit'
                    elif event.key == K_BACKSPACE:
                        self.text = self.text[:-1]
                    else:
                        self.text += event.unicode

                    self.setText(self.text)

    @staticmethod
    def setScreen(screen):
        InputBox.screen = screen


class CheckBox:
    screen = None
    def __init__(self,x, y, d, color = (200,200,200), activeColor = (200,200,200), text = '', textColor = (0,0,0), fontSize = 30, fontFamily = None, align='center', screen=None):
        super().__init__()
        self.surf = pygame.Surface((d,d))
        self.surf.fill(color)
        self.rect = getRect(self.surf, align, x, y)

        self.checked = False
        self.text = text

        self.color = color
        self.activeColor = activeColor
        self.textColor = textColor
        self.align = align
        self.font = pygame.font.Font(fontFamily, fontSize)
        self.x = x
        self.y = y

        if screen is not None:
            self.screen = screen

        l =  int(sqrt(2*(d*d)))-4
        x,y = self.rect.topleft
        self.xSurf1 = pygame.Surface((l,5), pygame.SRCALPHA)
        self.xSurf1.fill((0,0,0))
        self.xSurf1 = pygame.transform.rotate(self.xSurf1, -45)
        self.xRect1 = getRect(self.xSurf1, 'topleft', x, y)
        
        x,y = self.rect.bottomleft
        self.xSurf2 = pygame.Surface((l,5), pygame.SRCALPHA)
        self.xSurf2.fill((0,0,0))
        self.xSurf2 = pygame.transform.rotate(self.xSurf2, 45)
        self.xRect2 = getRect(self.xSurf2, 'bottomleft', x, y)



    def draw(self, screen=None):
        if screen is not None:
            self.screen = screen
        elif CheckBox.screen is not None and self.screen is None:
            self.screen = InputBox.screen

        self.screen.blit(self.surf, self.rect)
        if self.checked:
            self.screen.blit(self.xSurf1, self.xRect1)
            self.screen.blit(self.xSurf2, self.xRect2)

    def handle_event(self, event):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                self.checked = not self.checked
                return self.checked

    @staticmethod
    def setScreen(screen):
        CheckBox.screen = screen
