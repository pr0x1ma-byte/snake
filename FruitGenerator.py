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
class user(threading.Thread):
      def __init__(self,observer):
          threading.Thread.__init__(self)
          self.observer = observer
      def getObserver(self):
          return self.observer
      def run(self):
          ob = self.getObserver()
          tty.setraw(sys.stdin.fileno())
          while not ob.exit:
#                if  bal.getExit():
#                    bal.setUserExit();
#                    break;
#                else:
                 ch = sys.stdin.read(1)
                 if (ch == 'w'):
                    ob.up()
                 elif (ch == 's'):
                    ob.down()
                 elif ch == 'a':
                    ob.left()
                 elif ch == 'd':
                    ob.right()
                 elif ch == 'b':
		    ob.end();	
                    break;
	  print("size: "+str(ob.snake.size));
	  ob.end();
          ob.cleanup(); 	
