import Moteur_Physique as ExecuteEuler
import pygame

window_surface = None
largeur = 0
longueur = 0

sky=135,206,235
dirt=91,60,17
black = 0, 0, 0
arial_font = None


def begin(ScreenWidth,ScreenHeight):
    global window_surface

    global arial_font
    
    global largeur,longueur
    
    largeur = ScreenHeight
    longueur = ScreenWidth
    
    pygame.init()
    window_surface = pygame.display.set_mode(size=(ScreenWidth,ScreenHeight))
    arial_font = pygame.font.SysFont("arial", 30)
    
    
def Display(positionY,vitesseVerticale,vx_new,h):
    
    
    global window_surface
    global largeur
    global longeur
    global arial_font
    global black
    global dirt
    global sky
 
    rect_form=pygame.Rect(0,largeur/2+positionY,longueur,largeur)
    
    pygame.draw.rect(window_surface,dirt,rect_form)
    
    rect_sky=pygame.Rect(0,0,longueur,largeur/2+positionY)
    
    pygame.draw.rect(window_surface,sky,rect_sky)
    
    pygame.draw.line(window_surface,black,[0,largeur/2+positionY],[longueur,largeur/2+positionY],5)

    # display text
    
    
    vitesse_verticale = arial_font.render('VS: {:.2f}'.format(vitesseVerticale), True, (0,0,0) )
    
    window_surface.blit(vitesse_verticale,(30,30))

    vitesse_horizontal = arial_font.render('VH: {:.2f}'.format(vx_new), True, (0,0,0) )
    
    window_surface.blit(vitesse_horizontal,(30,70))

    
    
    Haltitude = arial_font.render('H: {:.2f}'.format(h), True, (0,0,0) )
    
    window_surface.blit(Haltitude,(30,110))
 

    assiette = arial_font.render('H: {:.2f}'.format(positionY), True, (0,0,0) )
    
    window_surface.blit(assiette,(30,160))


   
    
    pygame.display.flip()
    

def display(a,b,c,d):
    
    global window_surface
        
    window_surface.fill((255,255,255))
    
    
    window_surface.fill((0,255,0),rect=[0,0,500,250])
    
    
    
    window_surface.fill((255,0,0),rect=[0,250,500,250])
    pygame.display.update()