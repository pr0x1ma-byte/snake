from Snake import snake
from User import user
from FruitGenerator import fruitGenerator
import unicornhat as unicorn
from pyfiglet import figlet_format
import os
import sys
k=-1
unicorn.brightness(.5)
unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
width,height=unicorn.get_shape()
unicorn.rotation(0)
class observer():
      def __init__(self):
	  self.exit = False;
	  self.snake = snake(self);
          self.user = user(self);
	  self.fruitGenerator = fruitGenerator(self);
	  self.fruitBasket=[];
	  self.bodyCollision=False
      def end(self):
	  self.exit = True;
      def up(self):
	  self.snake.setDirection(1);
      def down(self):
	  self.snake.setDirection(4);
      def right(self):
	  self.snake.setDirection(2);
      def left(self):
	  self.snake.setDirection(3);
      def addFruit(self,fruit):
	  self.fruitBasket.insert(0,fruit);
      def cleanup(self):
	  unicorn.clear();
	  unicorn.rotation(90);
	  for i in range(100):
	      self.showScore();
	  os.system('stty sane');
	  sys.exit();	
      def showScore(self):
	  score = str(self.snake.size);
	  _figlet = figlet_format(score+' ',"banner");
	  textMatrix = _figlet.split("\n")[:width];
	  textWidth = len(textMatrix[0]);
	  global k;
	  k=0 if k>=100*textWidth else k+1
	  for h in range(height):
	      for w in range(width):
	          hPos = (k+h) % textWidth
	          chr = textMatrix[w][hPos]
	          if chr == ' ':
	             unicorn.set_pixel(width-w-1,h,0,0,0);
	          else:
	             unicorn.set_pixel(width-w-1,h,255,0,0)
          unicorn.show();	
      def begin(self):
	  self.user.start();			
#	  self.snake.addNode();
	  try:
	   self.fruitGenerator.start();
	   self.snake.start();
	  except:
	   self.end();
	   self.cleanup();
