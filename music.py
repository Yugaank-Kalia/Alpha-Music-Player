import pygame,time,os

pygame.init()
pygame.mixer.init()

Display = pygame.display.set_mode((800,600))
img = pygame.image.load("C:\\Users\\****\\Desktop\\Music player\\800px-Guitar-Wallpaper-music-24173658-1680-1050.png")



white=(255,255,255)

yellow = (200,200,0)
l_yellow = (255,255,0)

l_red = (255,0,0)
red =(230,0,0)

orange = (255,160,0)

l_green  = (0,255,0)
green = (34,177,76)

l_ok =(175,100,100)
ok = (150,100,100)

black = (0,0,0)

grey = (90,90,90)
gameExit = False
volume = 0.75

path1 = raw_input('Enter the full path of your songs folder : ')
path = path1.replace('\\','\\\\')
path += '\\'
files = []
name = []
font = pygame.font.SysFont('Century Gothic',25)

for filename in os.listdir(path):
    if filename.endswith(".mp3"):
        pat = os.path.abspath(filename)
        files.append(filename)
        name.append(filename)

for i in range(len(files)):
    files[i] = path + files[i]   

    
file_index = 0
pygame.mixer.music.load(files[file_index])
#-----------------------------------------------Functions
def shuffle(list_of_songs,name_of_songs):
    import random
    temp = list()
    temp.extend(([],[]))
    shuffle = True
    while shuffle:
        if len(list_of_songs)!=0:
            i = random.randrange(len(list_of_songs))
            temp[0].append(list_of_songs[i])
            list_of_songs.pop(i)
            temp[1].append(name_of_songs[i])
            name_of_songs.pop(i)
        else:
            shuffle = False
    return temp


def text_objects(text,color):
    textSurface = font.render(text,True,color)
    return textSurface , textSurface.get_rect()



def text(msg,color,x,y,w,h):
    textSurf,textRect = text_objects(msg,color)
    textRect.center = ((x+(w/2)),(y+(h/2)))
    Display.blit(textSurf , textRect)

#-----------------------------------------------Class Buttons
class Button(object):
    def play(self,text,x,y,w,h,inactive_col,active_col):
        self.cur = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()

        if x + w > self.cur[0] > x and y+h > self.cur[1] > y:
            pygame.draw.ellipse(Display,active_col,(x,y,w,h))

            if self.click[0]==1 :
                if pygame.mixer.music.get_busy()==1:
                    pygame.mixer.music.unpause()
                else:
                    pygame.mixer.music.load(files[file_index])
                    pygame.mixer.music.play()


        else:
            pygame.draw.ellipse(Display,inactive_col,(x,y,w,h))


    def pause(self,text,x,y,w,h,inactive_col,active_col):
        self.cur = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()

        if x + w > self.cur[0] > x and y+h > self.cur[1] > y:
            pygame.draw.ellipse(Display,active_col,(x,y,w,h))

            if self.click[0]==1:
                pygame.mixer.music.pause()


        else:
            pygame.draw.ellipse(Display,inactive_col,(x,y,w,h))


    def next_button(self,text,x,y,w,h,inactive_col,active_col):
        global file_index
        self.cur = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()

        if x + w > self.cur[0] > x and y+h > self.cur[1] > y:
            pygame.draw.ellipse(Display,active_col,(x,y,w,h))

            if self.click[0]==1:
                if files[file_index] == files[-1]:
                    file_index=0
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(files[file_index])
                    pygame.mixer.music.play()
                else:
                    file_index += 1
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(files[file_index])
                    pygame.mixer.music.play()
        else:
            pygame.draw.ellipse(Display,inactive_col,(x,y,w,h))

    def prev_button(self,text,x,y,w,h,inactive_col,active_col):
        global file_index
        self.cur = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()
        pos = pygame.mixer.music.get_pos()
        if x + w > self.cur[0] > x and y+h > self.cur[1] > y:
            pygame.draw.ellipse(Display,active_col,(x,y,w,h))

            if self.click[0]==1:
                if pos>5000:
                    play_song()
                else:
                    if files[file_index] == files[0]:
                        file_index = -1
                        pygame.mixer.music.stop()
                        pygame.mixer.music.load(files[file_index])
                        pygame.mixer.music.play()
                    else:
                        file_index -= 1
                        pygame.mixer.music.stop()
                        pygame.mixer.music.load(files[file_index])
                        pygame.mixer.music.play()

        else:
            pygame.draw.ellipse(Display,inactive_col,(x,y,w,h))





    def volume_up(self,text,x,y,w,h,inactive_col,active_col):
        global volume
        pygame.mouse.get_cursor()
        self.cur = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()


        if x + w > self.cur[0] > x and y+h > self.cur[1] > y:
            pygame.draw.ellipse(Display,active_col,(x,y,w,h))
            if self.click[0]==1:
                if volume != 1.0:
                    pygame.mixer.music.set_volume(volume + 0.075)
                    volume += 0.075
                else:
                    pass
        else:
            pygame.draw.ellipse(Display,inactive_col,(x,y,w,h))

    def volume_down(self,text,x,y,w,h,inactive_col,active_col):
        global volume
        pygame.mouse.get_cursor()
        self.cur = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()


        if x + w > self.cur[0] > x and y+h > self.cur[1] > y:
            pygame.draw.ellipse(Display,active_col,(x,y,w,h))
            if self.click[0]==1:
                if volume != 0:
                    pygame.mixer.music.set_volume(volume - 0.075)
                    volume -= 0.075
                else:
                    pass
        else:
            pygame.draw.ellipse(Display,inactive_col,(x,y,w,h))

    def shuffle_button(self,text,x,y,w,h,inactive_col,active_col):
        global name,files
        self.cur = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()

        if x + w > self.cur[0] > x and y+h > self.cur[1] > y:
            pygame.draw.ellipse(Display,active_col,(x,y,w,h))

            if self.click[0]==1 :
                new = shuffle(files,name)
                files = new
                name = new[1]
            else:
                pass
        else:
            pygame.draw.ellipse(Display,inactive_col,(x,y,w,h))


#----------------------------------------------------Main
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

        pygame.draw.rect(Display,grey,(0,400,800,200))
        Display.blit(img,(0,-20))

        play=Button().play('Play',250,500,100,50,green,l_green)
        pause=Button().pause('Pause',400,500,100,50,red,l_red)
        prev_button=Button().prev_button('Prev',105,500,100,50,yellow,l_yellow)
        next_button=Button().next_button('Next',550,500,100,50,yellow,l_yellow)
        volume_up=Button().volume_up('+',700,30,30,30,l_ok,ok)
        volume_down=Button().volume_down('-',700,400,30,30,l_ok,ok)
        shuffle_button=Button().shuffle_button("S",50,400,30,30,white,grey)

        pygame.draw.rect(Display,white,(703,75,25,310))
        pygame.draw.rect(Display,grey,(703,75,25,10))
        pygame.draw.rect(Display,grey,(703,375,25,10))


        text('Play',black,250,500,100,50)
        text('Pause',black,400,500,100,50)
        text('Prev',black,105,500,100,50)
        text('Next',black,550,500,100,50)
        text('+',black,700,30,30,30)
        text('-',black,700,400,30,30)
        text("S",black,50,400,30,30)

        names = str(name[file_index])
        names = names[:len(names)-4] 
        text(names,white,350,425,100,50)
        pygame.display.update()


pygame.quit()
