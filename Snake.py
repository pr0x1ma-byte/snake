
from random import randint
import unicornhat as unicorn
import threading
unicorn.brightness(.5)
unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
width,height=unicorn.get_shape()
unicorn.rotation(0)

class snake(threading.Thread):
      def __init__(self,observer):
	  threading.Thread.__init__(self);
	  self.stack=[[randint(0,width-1),randint(0,height-1)]]
	  self.head=self.stack[0]
	  self.tail=self.stack[len(self.stack)-1]	
	  self.size=1
	  self.direction=1
	  self.observer = observer
	  self.fruitExtract=[]
      def fruitCollision(self):
	  for i in self.observer.fruitBasket:
	      if i[0]==self.head[0] and i[1]==self.head[1]:
	         self.fruitExtract.insert(0,i);
	         self.observer.fruitBasket.remove(i);
      def addNode(self):
	  #generate new body, then insert old head into body
	  self.genBody();
	  self.size+=1;
      def remNode(self):
	  self.genBody();
	  self.removeTail();			  
      def genBody(self):
	  _x = None;
	  _y = None;
	  if self.direction==1:
	     #up
	     _x = self.head[0];
	     _y = self.head[1];
             _y += 1;
             if _y > height -1:
	        #wrap from top wall back to bottom
 	        _y = 0;

	  if self.direction==2:
	     #right 
   	     _y = self.head[1];
             _x = self.head[0];
	     _x-= 1;
	     if _x < 0:
	        #wrap from right wall back to left
                _x = width-1;
          if self.direction==3:
	     #left
	     _y = self.head[1];
	     _x = self.head[0];
             _x+= 1;
	     if _x > width -1:
	        #wrap from left wall back to right
	        _x = 0;
	  if self.direction==4:
	     #down
	     _x = self.head[0];
	     _y = self.head[1];
	     _y-= 1;
	     if _y < 0:
		#wrap from bottom wall back to top
	        _y = height -1;
   
	  newHead = [_x,_y]
	  self.head = newHead;
#	  self.direction = randint(1,3);			         	     
	  self.stack.insert(0,newHead);

      def removeTail(self):
	  if len(self.stack)==0:
	     #do nothing, head and tail are same coordinates
	     _default=1;	
     	  else:
	     del self.stack[len(self.stack)-1]
      def newHeadCheck(self):
	  _body=[];
	  _body=list(self.stack);
	  if len(_body)>1:
             _body.remove(self.head);
	     _index=0;
   	     for i in _body:
	         if self.head[0]==i[0] and self.head[1]==i[1]:
	            self.bodyCollision(_body,_index);
		    break;
                 _index+=1; 
      def bodyCollision(self,body,_index):
	   self.observer.exit=True;
#	   _length = len(body);
#	   _count=_index;
#	   for i in range(_index,_length-1):
#	       del self.stack[_count];
#              _count+=1;
	   self.observer.end();
	   self.observer.bodyCollision=True;
	   self.observer.cleanup();
      def draw(self):
	  unicorn.clear();
	  self.observer.fruitGenerator.draw();
	  for i in self.stack:
	      unicorn.set_pixel(i[0],i[1],255,0,255);
	  unicorn.show();
      def setDirection(self,_d):
	  self.direction = _d;	
      def run(self):
	  while not self.observer.exit:
		self.fruitCollision();
	        if len(self.fruitExtract)>0:
	           for i in self.fruitExtract:
	               self.addNode();
	           self.fruitExtract=[]
		   self.newHeadCheck();
		else:
	           self.remNode();
	 	   self.newHeadCheck();

	        if self.observer.bodyCollision:
	           self.observer.end();
	           break;
	        self.draw();
	        time.sleep(.1);#.2 works well..  		
#	  if self.observer.exit:
#	     unicorn.clear();
#	     print("size: "+str(self.size));
#	     self.observer.cleanup();
