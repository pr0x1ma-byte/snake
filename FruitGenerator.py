import threading
from random import randint
import sys
import tty
import time
import unicornhat as unicorn
unicorn.brightness(.5)
unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
width,height=unicorn.get_shape()
unicorn.rotation(0)

class fruitGenerator(threading.Thread):
      def __init__(self,observer):
	  self.observer = observer;
	  threading.Thread.__init__(self);
	  self.greenApple=[128,255,0];
	  self.redApple=[255,102,102];
	  self.basket=[self.greenApple,self.redApple];
#	  self.fruit = [];
      def run(self):
	  while not self.observer.exit:
	     if len(self.observer.fruitBasket) < 4:
		fruit=[randint(0,width-1),randint(0,height-1),self.basket[randint(0,1)]];
	        self.observer.addFruit(fruit);
	     time.sleep(5);
      def draw(self):
	  for i in self.observer.fruitBasket:
	      unicorn.set_pixel(i[0],i[1],i[2][0],i[2][1],i[2][2]);		
	
