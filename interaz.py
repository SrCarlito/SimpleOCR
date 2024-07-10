from tkinter import *

# import pygame
# pygame.init()
# font = pygame.font.Font('freesansbold.ttf', 32)
# white = (255, 255, 255)
# green = (0, 255, 0)
# blue = (0, 0, 128)

# text = font.render('GeeksForGeeks', True, green, blue)
# textRect = text.get_rect()


# def show(image):
#     # windowSurface = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
#     windowSurface = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
#     img = pygame.image.load(image)

#     running = True
#     while running:
#         windowSurface.blit(img, (0, 0)) #Replace (0, 0) with desired coordinates
#         windowSurface.blit(text, textRect)
#         pygame.display.flip()
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_ESCAPE:
#                     running = False
                    
#     pygame.display.quit()
#     pygame.quit()
#     exit()

def show(image):
    root = Tk()
    root.attributes("-fullscreen",True)
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    canvas = Canvas(root,width=w,height=h)
    logo=PhotoImage(file=image)
    canvas.create_image(w/2, h/2, image=logo) #Change 0, 0 to whichever coordinates you need
 
    # Create label
    l = Label(canvas, text = "Fact of the Day")
    l.config(font =("Courier", 14))
    l.pack()
    canvas.pack()
    root.mainloop()


