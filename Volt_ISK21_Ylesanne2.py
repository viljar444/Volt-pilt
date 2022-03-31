import pygame                                                #mooduli pygame importimine
pygame.init()                                                #pygame käivitamine

screen=pygame.display.set_mode([640,480])                    #soovitud suurusega akna tekitamine, mis lisatakse muutujasse.Akna mõõt 640x480 px.
pygame.display.set_caption("Ülesanne 2")                     #aknale nimetuse andmine

bg = pygame.image.load("bgshop.jpg")                         #pildi lisamine muutujasse
screen.blit(bg,[0,0])                                        #kuvab pildi kogu ekraani ulatuses, 0 koordinaatidega

seller = pygame.image.load("seller.png")                     #pildi lisamine ,muutuja omistab pildi.
seller = pygame.transform.scale(seller, [244, 300])          #transform abil saab pildi mõõtmeid muuta  xy koordinaadtidega
screen.blit(seller,[105,164])                                #pildi liigutamine vastavalt xy koordinaatidega

chat = pygame.image.load("chat.png")                         #pildi lisamine ,muutuja omistab pildi
chat = pygame.transform.scale(chat, [244, 214])              #transform abil saab pildi mõõtmeid muuta xy koordinaatidega
screen.blit(chat,[240,60])                                   #pildi liigutamine vastavalt xy koordinaatidega

font = pygame.font.Font(pygame.font.match_font('Tahoma'), 21)#Teksti font`i valimne, Tahoma suurus 21, omistab muutuja font
text = font.render("Tere, olen Viljar", True, [255,255,255]) #Teksti lisamine,pehmed servad, valge
screen.blit(text, [290,135])                                 #teksti liigutamine vastavalt xy koordinaatidega






pygame.display.flip()                                        #ekraani värskendamine





from sys import exit                         #mooduli importimine, et ekraan ei sulguks
while True:                                  #korduslause kui õige
        for event in pygame.event.get():     #event omistab mooduli parameetird
            if event.type == pygame.QUIT:    #tingimusel kui võrdne
                pygame.quit()                #lõpetab tegevuse kui, kasutaja aktiveerib
                exit()                       #väljub
