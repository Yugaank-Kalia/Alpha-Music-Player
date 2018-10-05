# Alpha-Music-Player
A simple music player written in Python with PyGame, a library made for creation of games in python. One of my first projects in Python. 

This code snippet will 

1.You'll need to install PyGame and import it. 
2.Initiate the **Mixer of PyGame** and Create a display give it dimensions. 
3.Fill the display with colours. 
4.Set fps of update() function. 
5.It will Run until it hits event.type == pygame.QUIT condition. 
```
import pygame
pygame.init()
pygame.display.init()
window = pygame.display.set_mode((1000,1000),pygame.RESIZABLE)
pygame.display.set_caption('Apollo Music Player')
gray = (50,50,50)
window.fill(gray)
clock = pygame.time.Clock()
fps = 30
def play_a_song(name_of_song):
    pygame.mixer.music.load(name_of_song)
    pygame.mixer.music.play()
play_a_song("Lights Go Out.mp3")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(fps)
    pygame.display.update()
    
pygame.quit()

```
## To run this module on your computer
```
pip install pygame
```
then edit **music.py** and change the path to your music file. 
**This snippet handles only one song at a time because of the drawbacks of PyGame**
