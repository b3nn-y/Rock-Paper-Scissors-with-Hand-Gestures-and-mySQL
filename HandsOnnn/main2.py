import csv
import copy
import argparse
import itertools
from collections import Counter
from collections import deque

import cv2
import kivy
from kivy.app import App
from kivy.uix.video import Video


import cv2 as cv
import numpy as np
import mediapipe as mp

from utils import CvFpsCalc
from model import KeyPointClassifier
from model import PointHistoryClassifier
import kivy
from kivy.app import App
kivy.require('1.9.0')
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.core.audio import SoundLoader
import time
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from app import main
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
import keyboard
from tabulate import tabulate
import mysql.connector

Builder.load_string("""
<ScreenOne>:
    Image:
        
        source:'gif2.gif'
        
        
        allow_stretch: True
        anim_delay: 1/30
        sound: root.sound()
        
        anim_loop: 1
        
        
        

	Button:
	    
		bold: True
		text: "CLICK TO START"
		font_name: 'font.otf'
		font_size: "45dp"
        color: 0, 0,0, .4
			
		background_color : 1, 0, 1, 0
		on_press:
		    root.soundd()
			root.manager.transition.direction = 'left'
			root.manager.transition.duration = 1
			root.manager.current = 'screen_three'
    
    
    
            
    
                


<ScreenTwo@GridLayout>:
    Image:
        source:'tm.png'
           
           
        BoxLayout:
            size_hint: self.size
            size: 100, 50
            orientation: 'vertical'
                
        
            Button:
                text: 'BACK'
                on_press:
                    sound: root.sound()
                    root.manager.transition.direction = 'right'
                    root.manager.transition.duration = 1
                    root.manager.current = 'screen_three'
                
    
    
            
    
    

<ScreenThree>:
    Image:
        source:'menu.png'
        
           
           
        BoxLayout:
            size_hint: self.size
            size: 200, 100
            orientation: 'vertical'
                
        
            Button:
                text: 'PLAY'
                on_press:
                    sound: root.sound()
                    root.manager.transition.direction = 'left'
                    root.manager.transition.duration = 1
                    root.manager.current = 'screen_four'
                    
            Button:
                text: 'TEAM MEMBERS'
                on_press:
                    sound: root.sound()
                    root.manager.transition.direction = 'left'
                    root.manager.transition.duration = 1
                    root.manager.current = 'screen_two'
                    root.mem()
            Button:
                text: 'SCORES'
                on_press:
                    sound: root.sound()
                    root.scores()
                    root.manager.transition.direction = 'left'
                    root.manager.transition.duration = 1
                    root.manager.current = 'screen_five'
                

<ScreenFour>:
    Image:
        source:'rulestoo.png'
        
           
           
        BoxLayout:
            size_hint: self.size
            size: 200, 100
            orientation: 'vertical'
                
        
            Button:
                text: 'START'
                on_press:
                    sound: root.sound()
                    root.play()
                    
            Button:
                text: 'HOME'
                on_press:
                    sound: root.sound()
                    root.manager.transition.direction = 'right'
                    root.manager.transition.duration = 1
                    root.manager.current = 'screen_three'
	
		
<ScreenFive>:
    Image:
        source:'scores.png'
           
           
        BoxLayout:
            size_hint: self.size
            size: 100, 50
            orientation: 'vertical'
                
        
            Button:
                text: 'BACK'
                on_press:
                    sound: root.sound()
                    root.manager.transition.direction = 'right'
                    root.manager.transition.duration = 1
                    root.manager.current = 'screen_three'
	

""")
db = mysql.connector.connect(host="localhost", user="root", passwd="root",database = "handson")
mc = db.cursor()

def bgmusic():

    b = SoundLoader.load(filename='bggg.mp3')
    b.loop = True

    b.play()


class ScreenOne(Screen,GridLayout):
    def sound(self):
        b=SoundLoader.load(filename='intro.mp3')

        b.play()

        #b.stop()
    def soundd(self):
        b=SoundLoader.load(filename='click.wav')

        b.play()






class ScreenTwo(Screen,BoxLayout):
    def sound(self):
        b=SoundLoader.load(filename='click.wav')

        b.play()


class ScreenThree(Screen):
    bgmusic()

    def sound(self):
        b=SoundLoader.load(filename='click.wav')

        b.play()

    def scores(self):
        #mc.execute("select * from scores")
        # db.commit()
        #results = mc.fetchall()
        #print(tabulate(results,
        #               headers=['gID', 'UserName', 'No_of_GamesPlayed', 'Player_Score', 'AI_Score', 'No_of_Draws',
        #                       'Overall_PlayerWinorLose'], tablefmt='psql'))

        mc.execute("select * from scores")
        #db.commit()
        results = mc.fetchall()


        print(tabulate(results,
                       headers=['gID', 'UserName', 'No_of_GamesPlayed', 'Player_Score', 'AI_Score', 'No_of_Draws',
                                'Overall_PlayerWinorLose'], tablefmt='psql'))
        return
    def mem(self):
        print("The Team Members are:")
        print("\t *Benny Samuel")
        print("\t *Sibyll Dominic")
        print("\t *Logesh.S")



        #b.stop()
class ScreenFour(Screen):
    def play(self):
        main()




    def sound(self):
        b = SoundLoader.load(filename='click.wav')

        b.play()



class ScreenFive(Screen):
    def sound(self):
        b = SoundLoader.load(filename='click.wav')

        b.play()

screen_manager = ScreenManager()

# Add the screens to the manager and then supply a name
# that is used to switch screens
screen_manager.add_widget(ScreenOne(name="screen_one"))
screen_manager.add_widget(ScreenTwo(name="screen_two"))
screen_manager.add_widget(ScreenThree(name="screen_three"))
screen_manager.add_widget(ScreenFour(name="screen_four"))
screen_manager.add_widget(ScreenFive(name="screen_five"))
# Create a class for all screens in which you can include
# helpful methods specific to that screen

class HandsOnnApp(App):
    def build(self):
        return screen_manager





# The ScreenManager controls moving between screens



# Create the App class






# run the app



if __name__ == '__main__':

    app = HandsOnnApp()
    app.run()


