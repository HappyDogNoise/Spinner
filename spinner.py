#import of all required modules
import turtle
import random
from tkinter import *
import time

class Selector(Tk):
    """object for the tkinter window where items are input"""
    
    def __init__(self,Drawer):
        """init method creates window and sets up all widgets"""
        
        #window itself
        self.Window = Tk()
        
        #holds the turtle screen
        self.Drawer = Drawer
        
        #the window's title 
        self.Window.title("Yes")
        
        #creates a label as the window's title
        self.title = Label(self.Window,text = "The Spinner",font = "futura 32 bold")
        self.title.pack()
        
        #creates a label for any errors located
        self.ERRORS = Label(self.Window)
        self.ERRORS.pack()
        
        #creates the list of items
        self.Items = []
        
        #makes window full screen
        self.Window.geometry("1920x1080")
        
        #creates a text entry widgit
        self.e = Entry(self.Window)
        self.e.pack()

        #sets the return key as a entry
        self.Window.bind('<Return>',self.Entered)
        
        #creates the button to kill the window and start the turltle
        self.EndButton = Button(self.Window,text = 'done',command = self.Finnished)
        self.EndButton.pack()


        #loops the window
        self.Window.mainloop()

    #what happens when the return key is pressed
    def Entered(self,a):
        """once the enter key is pressed, the contents is colected"""
        
        #appends the list with what was in the entry widgit
        self.Items.append(self.e.get())
        
        #removes the contence of the entry widgit
        self.e.delete(0,'end')

        #prints the list 
        print(self.Items)
    
    #what to do when done button pressed
    def Finnished(self):
        """when all inputs colected the turtle screen is run"""
        
        #makes sure that there have been inputs
        if len(self.Items) > 1:
            
            if self.e.get() != "":
                #puts whatever was in the entry widgit in the list
                self.Entered(1)
            
            #destroys the window
            self.Window.destroy()
            
            #starts the turtle
            self.Spinner = screen(self.Items,self.Drawer)
            
        else:
            
            #changes the error label to show the error
            self.ERRORS.config(text = "ERROR: not enough inputs made",fg = "red")
    

class screen:
    """object for the turtle screen"""
    
    def __init__(self,Items,screen):
        """init method for the turtle function sets up speed colour and starts the spinning"""
        
        self.don = turtle.Turtle() #creates the turtle for circle
        self.don.speed(0) #sets to max speed
        self.don.ht() #hides the turtle arrow
        
        self.sam = turtle.Turtle() #creates the turtle for the spinning animation      
        self.sam.speed(0) #sets sam to max speed
        self.sam.seth(0) #make sam look up
        
        self.Items = Items #gets the item list
        
        self.screen = screen #sets the turtle screen
        
        self.screen.setup(width=1.0, height=1.0, startx=None, starty=None) #full screen
        
        if len(self.Items) > 0:
        
            self.screen.onscreenclick(self.start) #starts the spinner on every click of the screen
    
    def circle(self):
        """draws the circle that the spinner will spin on"""
        
        self.don.pu()
        
        self.don.seth(90)
        
        self.don.goto(0,-250)
        
        self.don.pd()
        
        self.don.circle(250)
    
    def lookUp(self,turt):
        """makes the turtle look straight up (towards y = 0)"""
        
        turt.seth(0)
    
    def section(self):
        """splits the circle into the given ammount of sections"""
        
        self.lookUp(self.don)
        
        #for every item in the list
        for i in range(len(self.Items)):
            
            self.don.pu()
        
            self.don.goto(0,0)
            
            self.don.pd()
            
            self.don.fd(250)
            
            self.don.rt(360 / len(self.Items))
    
    def fillLabels(self):
        """adds labels to each section of the spinner"""
        
        self.lookUp(self.don)
        
        #for every item in the list
        for i in range(len(self.Items)):
            
            self.don.pu()
            
            self.don.goto(0,0)
            
            self.don.rt((360 / len(self.Items)) * (1 / 4))
            
            self.don.fd(175)
            
            self.don.pd()
            
            self.don.write(self.Items[i], font=('Arial', 16, 'bold'), align='center')
            
            self.don.pu()
            
            self.don.back(175)
            
            self.don.rt((360 / len(self.Items)) * (3 / 4))
               
    def spinAnim(self):
        """shows the needle of the turtle"""
        
        self.sam.pu()
        
        self.sam.goto(0,0)
        
        self.sam.pd()
        
        self.sam.fd(175)
        
        time.sleep(0.05)

    def Selector(self):
        """Draws the screen and labels everything. also starts the spinning"""
        
        #creates the labeled circle
        self.circle() 
        self.section() 
        self.fillLabels()
        self.screen.update()
        
        #makes the spinner slow down
        time = random.uniform(30,50)
        Vel = random.randint(20,30)
        deceleration = Vel / (time)
        
        #starts the spinning
        while Vel > 0.05:
            
            self.sam.clear()
            
            self.sam.rt(Vel - deceleration)
            
            Vel -= deceleration
            
            self.spinAnim()
            
            self.screen.update()
            
        self.selected()
    
    def selected(self):
        """finds the winner"""
        pointing = self.sam.heading()
        
        separators = 360 / len(self.Items)

        for i in range(len(self.Items)):

            if pointing < separators * (i + 1):

                self.Items.pop(i)
                break

        
    def start(self,x,y):
        """starts the function on a click"""
        
        self.sam.clear()
        self.don.clear()
        
        if len(self.Items) > 1:
            self.Selector()
        else:
            self.Fireworks()
            
    def Fireworks(self):
        """runs a little victory animation for the final item"""
        self.screen.bgcolor("#000000")
        self.don.pu()
        self.don.goto(0,0)
        self.don.pd()
        self.don.color('red')
        self.don.write(self.Items[0],font = ('Arial', 16, 'bold'), align = 'left')

if __name__ == '__main__':
    
    turtleScreen = turtle.Screen()
    turtleScreen.mode("logo")
    turtleScreen.tracer(0)
    turtleScreen.setup(0,0)
    
    
    window = Selector(turtleScreen)
    
    
    
    
    
    
    










