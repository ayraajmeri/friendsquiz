# friendsquiz.py
# Buzzfeed-style quiz to see which Friends character you are most like.

#Importing tkinter moves 
from tkinter import *
from tkinter import ttk 
from PIL import ImageTk, Image


#this creates a window 
root = Tk()
root["bg"] = "black"

#this sets the defualt height and width of the window
root.geometry("700x1000") #figure out the right framing


#get title
root.title("Friends Personality Quiz")

#These are all of the quiz quesiton
frame1 = Frame(root)
frame2 = Frame(root)
frame3 = Frame(root)
frame4 = Frame(root)
frame5 = Frame(root)
frame6 = Frame(root)
frame7= Frame(root)
frame8 = Frame(root)

#Creating variables = 0 to keep score of which answer realtes to each character
global Rachel, Ross, Monica, Joey, Chandler, Pheobe
Rachel = 0
Ross = 0
Monica = 0
Joey = 0 
Chandler = 0
Phoebe  = 0

#This is the title
title = Label(frame1, text= "Which Friends character do you relate to the most based on your personality?", font= ("Arial", 17) )
title.place(x= 90, y= 5)

#q1(Label) is stating the question without a button 
q1 = Label(frame1, text= "What do you value the most?", font= ("Arial", 17)) 
q1.place(x= 245, y= 60)



#Functions to add to totals and swap to next window
def answer1(): 
    global Joey
    Joey = Joey + 1
    swapToFrame2()
    
def answer2():
    global Chandler, Ross
    Chandler = Chandler + 1
    Ross = Ross + 1
    swapToFrame2()
    
def answer3():
    global Monica, Ross
    Monica = Monica + 1 
    Ross = Ross + 1
    swapToFrame2()
    
def answer4():
    global Joey, Monica
    Joey = Joey + 1 
    Monica = Monica + 1
    swapToFrame2()
    
def answer5():
    global Rachel
    Rachel = Rachel + 1
    swapToFrame2()
    
def answer6():
    global Chandler, Ross
    Chandler = Chandler + 1
    Ross = Ross + 1
    swapToFrame2()


#Creating Buttons
a1 = Button(frame1, text= "Friends", font= ("Arial",15), highlightbackground= '#d42424', fg= 'white', command= lambda: answer1())
a1.place(x= 200, y= 140)

a2 = Button(frame1, text= "Money", font= ("Arial",15), highlightbackground= '#d42424', fg= 'white', command= lambda: answer2())
a2.place(x= 400, y= 140) 

a3 = Button(frame1, text= "Family", font= ("Arial",15), highlightbackground= '#d42424', fg= 'white', command= lambda: answer3())
a3.place(x=200, y= 220)

a4= Button(frame1, text= "Career", font= ("Arial",15), highlightbackground= '#d42424', fg= 'white', command= lambda: answer4())
a4.place(x= 400, y= 220)

a5= Button(frame1, text="Relationships", font= ("Arial",15), highlightbackground= '#d42424', fg= 'white', command= lambda: answer5())
a5.place(x= 200, y=300)

a6= Button(frame1, text= "Acceptance",font= ("Arial",15), highlightbackground= '#d42424', fg= 'white', command= lambda: answer6())
a6.place(x= 400, y= 300)

#Swapping frames to 2nd question
def swapToFrame2():
    frame2.pack(fill='both', expand=1)
    frame1.forget()

title = Label(frame2, text= "Which Friends character do you relate to the most based on your personality?", font= ("Arial", 17) )
title.place(x= 90, y= 10)
    
q2 = Label(frame2, text= "Pick a color:", font= ("Arial", 17))
q2.place(x= 275, y= 60)
    
    
def q2answer1():
    global Phoebe 
    Phoebe  = Phoebe  + 1
    swapToFrame3()

def q2answer2():
    global Ross, Chandler
    Ross = Ross + 1
    Chandler = Chandler + 1
    swapToFrame3()

def q2answer3():
    global Joey, Chandler
    Joey = Joey + 1 
    Chandler = Chandler + 1
    swapToFrame3()
    
def q2answer4():
    global Monica
    Monica = Monica + 1
    swapToFrame3()

def q2answer5():
    global Rachel
    Rachel = Rachel + 1
    swapToFrame3()
def q2answer6():
    global Joey
    Joey = Joey + 1
    swapToFrame3()

q2a1 = Button(frame2, text= "Purple",font= ("Arial",15), highlightbackground= '#9342f5', fg= 'white', borderwidth = 2, relief = "groove" ,  command= lambda: q2answer1())
q2a1.place(x= 200, y= 150)

    
q2a2 = Button(frame2, text= "Red", font= ("Arial",15), highlightbackground= '#e61010', fg= 'white', command= lambda: q2answer2())
q2a2.place(x= 400, y= 150)

q2a3 = Button(frame2, text= "Blue", font= ("Arial",15), highlightbackground= '#0b15db', fg= 'white', command= lambda: q2answer3())
q2a3.place(x=200, y= 250)

q2a4 = Button(frame2, text= "Brown", font= ("Arial",15), highlightbackground= '#661721', fg= 'white',command= lambda: q2answer4())
q2a4.place(x= 400, y= 250)

q2a5 = Button(frame2, text= "Pink", font= ("Arial",15), highlightbackground= '#ed39d5', fg= 'white', command= lambda: q2answer5())
q2a5.place(x= 200, y=350)

q2a6 = Button(frame2, text= "Green", font= ("Arial",15), highlightbackground= '#25942c', fg= 'white',command= lambda: q2answer6())
q2a6.place(x= 400, y= 350)

frame1.pack(fill='both', expand=1)

title = Label(frame3, text= "Which Friends character do you relate to the most based on your personality?", font= ("Arial", 17) )
title.place(x= 90, y= 10)

# start third question 
def swapToFrame3():
    frame3.pack(fill='both', expand=1)
    frame2.forget()

q3 = Label(frame3, text= "What is your best quality?", font= ("Arial", 17) )
q3.place(x= 240, y= 60)

def q3answer1():
    global Ross 
    Ross = Ross + 1
    swapToFrame4()

def q3answer2():
    global Rachel
    Rachel = Rachel + 1
    swapToFrame4() 

def q3answer3():
    global Monica 
    Monica = Monica + 1
    swapToFrame4() 

def q3answer4():
    global Joey, Ross, Monica, Chandler, Rachel, Phoebe  
    Joey = Joey + 1
    Ross = Ross + 1 
    Monica = Monica + 1
    Rachel = Rachel + 1
    Chandler = Chandler + 1 
    Phoebe = Phoebe + 1
    swapToFrame4() 

def q3answer5():
    global Chandler 
    Chandler = Chandler + 1
    swapToFrame4()

def q3answer6():
    global Phoebe 
    Phoebe  = Phoebe  + 1
    swapToFrame4()

q3a1 = Button(frame3, text= "Smart", font= ("Arial",15), highlightbackground= '#8b12a1', fg= 'white',command= lambda: q3answer1())
q3a1.place(x= 200, y= 150)

q3a2 = Button(frame3, text= "Honest", font= ("Arial",15), highlightbackground= '#8b12a1', fg= 'white', command= lambda: q3answer2())
q3a2.place(x= 400, y= 150)

q3a3 = Button(frame3, text= "Being Clean", font= ("Arial",15), highlightbackground= '#8b12a1', fg= 'white', command= lambda: q3answer3())
q3a3.place(x=200, y= 250)

q3a4 = Button(frame3, text= "Hard-working", font= ("Arial",15), highlightbackground= '#8b12a1', fg= 'white', command= lambda: q3answer4())
q3a4.place(x= 400, y= 250)

q3a5 = Button(frame3, text= "Laid Back", font= ("Arial",15), highlightbackground= '#8b12a1', fg= 'white', command= lambda: q3answer5())
q3a5.place(x= 200, y=350)

q3a6 = Button(frame3, text= "Being yourself", font= ("Arial",15), highlightbackground= '#8b12a1', fg= 'white', command= lambda: q3answer6())
q3a6.place(x= 400, y= 350)


def swapToFrame4():
    frame4.pack(fill='both', expand=1)
    frame3.forget()

title = Label(frame3, text= "Which Friends character do you relate to the most based on your personality?", font= ("Arial", 17) )
title.place(x= 90, y= 10)

q4 = Label(frame4, text= "What is your favorite Ice Cream Flavor?", font= ("Arial", 17))
q4.place(x= 210, y= 60) 

def q4answer1():
    global Chandler 
    Chandler = Chandler + 1
    swapToFrame5()

def q4answer2():
    global Phoebe 
    Phoebe = Phoebe + 1
    swapToFrame5()

def q4answer3():
    global Ross
    Ross = Ross + 1
    swapToFrame5()

def q4answer4():
    global Joey 
    Joey = Joey + 1
    swapToFrame5()
   
def q4answer5():
    global Rachel
    Rachel = Rachel + 1
    swapToFrame5()

def q4answer6():
    global Monica
    Monica = Monica + 1
    swapToFrame5()

q4a1 = Button(frame4, text= "Chocolate", font= ("Arial",15), highlightbackground= '#e872ad', fg= 'white', command= lambda: q4answer1())
q4a1.place(x= 200, y= 150)

q4a2 = Button(frame4, text= "Strawberry", font= ("Arial",15), highlightbackground= '#e872ad', fg= 'white', command= lambda: q4answer2())
q4a2.place(x= 400, y= 150)

q4a3 = Button(frame4, text= "Vanilla", font= ("Arial",15), highlightbackground= '#e872ad', fg= 'white',command= lambda: q4answer3())
q4a3.place(x=200, y= 250)

q4a4 = Button(frame4, text= "Rocky Road", font= ("Arial",15), highlightbackground= '#e872ad', fg= 'white', command= lambda: q4answer4())
q4a4.place(x= 400, y= 250)

q4a5 = Button(frame4, text= "Coconut", font= ("Arial",15), highlightbackground= '#e872ad', fg= 'white', command= lambda: q4answer5())
q4a5.place(x= 200, y=350)

q4a6 = Button(frame4, text= "Mint Chocolate Chip", font= ("Arial",15), highlightbackground= '#e872ad', fg= 'white', command= lambda: q4answer6())
q4a6.place(x= 400, y= 350)

def swapToFrame5():
    frame5.pack(fill='both', expand=1)
    frame4.forget()

title = Label(frame4, text= "Which Friends character do you relate to the most based on your personality?",font= ("Arial", 17) )
title.place(x= 90, y= 10)

q5 = Label(frame5, text= "Pick your favorite school subject?", font= ("Arial", 17))
q5.place(x= 220, y= 60)

def q5answer1():
    global Chandler 
    Chandler = Chandler + 1
    swapToFrame6()

def q5answer2():
    global Ross
    Ross = Ross + 1
    swapToFrame6()

def q5answer3( ):
    global Monica, Phoebe
    Monica = Monica + 1
    Phoebe = Phoebe + 1
    swapToFrame6()

def q5answer4(): 
    global Rachel 
    Rachel = Rachel + 1
    swapToFrame6()

def q5answer5():
    global Joey 
    Joey = Joey + 1
    swapToFrame6()

def q5answer6():
    global Joey, Phoebe 
    Joey = Joey + 1
    Phoebe = Phoebe + 1
    swapToFrame6()

q5a1 = Button(frame5, text= "Math",  font= ("Arial",15), highlightbackground= '#0a0109', fg= 'white', command= lambda: q5answer1())
q5a1.place(x= 200, y= 150)

q5a2 = Button(frame5, text= "History", font= ("Arial",15), highlightbackground= '#0a0109', fg= 'white',  command= lambda: q5answer2())
q5a2.place(x= 400, y= 150)

q5a3 = Button(frame5, text= "Science", font= ("Arial",15), highlightbackground= '#0a0109', fg= 'white', command= lambda: q5answer3())
q5a3.place(x=200, y= 250)

q5a4 = Button(frame5, text= "English", font= ("Arial",15), highlightbackground= '#0a0109', fg= 'white',  command= lambda: q5answer4())
q5a4.place(x= 400, y= 250)

q5a5 = Button(frame5, text= "Theater", font= ("Arial",15), highlightbackground= '#0a0109', fg= 'white', command= lambda: q5answer5())
q5a5.place(x= 200, y=350)

q5a6 = Button(frame5, text= "I hate school", font= ("Arial",15), highlightbackground= '#0a0109', fg= 'white', command= lambda: q5answer6())
q5a6.place(x= 400, y= 350)

def swapToFrame6():
    frame6.pack(fill='both', expand=1)
    frame5.forget()

title = Label(frame5, text= "Which Friends character do you relate to the most based on your personality?",font= ("Arial", 17) )
title.place(x= 90, y= 10)

q6 = Label(frame6, text= "What is your favorite food?", font= ("Arial", 17))
q6.place(x= 250, y= 60)


def q6answer1():
    global Phoebe 
    Phoebe = Phoebe + 1
    swapToFrame7()

def q6answer2():
    global Ross, Joey 
    Ross = Ross + 1
    Joey = Joey + 1
    swapToFrame7()

def q6answer3():
    global Chandler, Joey 
    Chandler = Chandler + 1
    Joey = Joey + 1
    swapToFrame7()

def q6answer4():
    global Joey 
    Joey = Joey + 1
    swapToFrame7()

def q6answer5():
    global Monica
    Monica = Monica + 1
    swapToFrame7()

def q6answer6():
    global Rachel 
    Rachel = Rachel + 1
    swapToFrame7()

q6a1 = Button(frame6, text= "Mac n Cheese", font= ("Arial",15), highlightbackground= '#1c8c63', fg= 'white', command= lambda: q6answer1())
q6a1.place(x= 200, y= 150)

q6a2 = Button(frame6, text= "Burgers", font= ("Arial",15), highlightbackground= '#1c8c63', fg= 'white', command= lambda: q6answer2())
q6a2.place(x= 400, y= 150)

q6a3 = Button(frame6, text= "Pizza", font= ("Arial",15), highlightbackground= '#1c8c63', fg= 'white', command= lambda: q6answer3())
q6a3.place(x=200, y= 250)

q6a4 = Button(frame6, text= "Turkey", font= ("Arial",15), highlightbackground= '#1c8c63', fg= 'white', command= lambda: q6answer4())
q6a4.place(x= 400, y= 250)

q6a5 = Button(frame6, text= "Pasta", font= ("Arial",15), highlightbackground= '#1c8c63', fg= 'white', command= lambda: q6answer5())
q6a5.place(x= 200, y=350)

q6a6 = Button(frame6, text= "Salad", font= ("Arial",15), highlightbackground= '#1c8c63', fg= 'white', command= lambda: q6answer6())
q6a6.place(x= 400, y= 350)

def swapToFrame7():
    frame7.pack(fill='both', expand=1)
    frame6.forget()

title = Label(frame6, text= "Which Friends character do you relate to the most based on your personality?", font= ("Arial", 17) )
title.place(x= 90, y= 10)

title = Label(frame7, text= "Which Friends character do you relate to the most based on your personality?", font= ("Arial", 17) )
title.place(x= 90, y= 10)

q5 = Label(frame7, text= "Pick a pet: ", font= ("Arial", 17))
q5.place(x= 300, y= 60)

def q7answer1():
    global Phoebe
    Phoebe = Phoebe + 1
    swapToFrame8()

def q7answer2():
    global Phoebe, Monica 
    Phoebe = Phoebe + 1 
    Monica = Monica + 1
    swapToFrame8()

def q7answer3():
    global Ross
    Ross = Ross + 1
    swapToFrame8()

def q7answer4():
    global Chandler 
    Chandler = Chandler + 1
    swapToFrame8()

def q7answer5():
    global Rachel 
    Rachel = Rachel + 1
    swapToFrame8()

def q7answer6():
    global Monica 
    Monica = Monica + 1
    swapToFrame8()

q7a1 = Button(frame7, text= "Dogs", font= ("Arial",15), highlightbackground= '#f58d16', fg= 'white', command= lambda: q7answer1())
q7a1.place(x= 200, y= 150)

q7a2 = Button(frame7, text= "Cats", font= ("Arial",15), highlightbackground= '#f58d16', fg= 'white', command= lambda: q7answer2())
q7a2.place(x= 400, y= 150)

q7a3 = Button(frame7, text= "Monkeys", font= ("Arial",15), highlightbackground= '#f58d16', fg= 'white',  command= lambda: q7answer3())
q7a3.place(x=200, y= 250)

q7a4 = Button(frame7, text= "Birds", font= ("Arial",15), highlightbackground= '#f58d16', fg= 'white', command= lambda: q7answer4())
q7a4.place(x= 400, y= 250)

q7a5 = Button(frame7, text= "Horses", font= ("Arial",15), highlightbackground= '#f58d16', fg= 'white',  command= lambda: q7answer5())
q7a5.place(x= 200, y=350)

q7a6 = Button(frame7, text= "I don't like pets", font= ("Arial",15), highlightbackground= '#f58d16', fg= 'white', command= lambda: q7answer6())
q7a6.place(x= 400, y= 350)

def swapToFrame8():
    frame8.pack(fill='both', expand=1)
    frame7.forget()
    global Ross, Chandler, Joey, Rachel, Monica, Phoebe
    highestscore = max(Ross, Chandler, Joey, Rachel, Monica, Phoebe)
    if highestscore == Ross:
       winner =  Label(frame8, text= "Ross",  font=("Arial", 20))
       winner.place(x= 200, y= 90)

    elif highestscore == Chandler: 
        winner =  Label(frame8, text= "Chandler", font=("Arial", 20))
        winner.place(x= 200, y= 90)
    elif highestscore == Rachel:
         winner =  Label(frame8, text= "Rachel", font=("Arial", 20))
         winner.place(x= 200, y= 90)
         
    elif highestscore == Joey:
        winner =  Label(frame8, text= "Joey", font=("Arial", 20))
        winner.place(x= 200, y= 90)
    
    elif highestscore == Monica:
        winner =  Label(frame8, text= "Monica", font=("Arial", 20))
        winner.place(x= 200, y= 90)

    elif highestscore == Phoebe:
        winner =  Label(frame8, text= "Phoebe", font=("Arial", 20))
        winner.place(x= 200, y= 90)
       
  


    # my_img = ImageTk.PhotoImage(Image.open("ross.png"))
    # my_label = Label(image= my_img)
    # my_label.place(x=200, y= 200)
    # img = Image.open("ross.png") 
    # photo=ImageTk.PhotoImage(img)

    # img  = Image.open("ross.png") 
    # photo=ImageTk.PhotoImage(img)
    # lab=Label(image=photo).place(x=50,y=50)

resultstitle = Label(frame8, text= "Based on your options, you relate most to...", font=("Arial", 24))
resultstitle.place(x= 145, y= 10)









#this is the main loop which continuously runs the window
root.mainloop()

