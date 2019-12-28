# 19fa103; john k johnstone; jkj at uab dot edu; mit license

import lab06_19fa103 as lab06
from turtle import * # yes, you have to import it again
                     # (for the turtle calls in this file)

speed(10) # use speed(1) to see your drawing better;
          # for faster drawing, increase to speed(5), speed(0) for real fast

# ADD YOUR LINE FUNCTION CALLS HERE
# in quadrant 1

lab06.drawLine1 ((200,200), 45, 50)
lab06.drawLine2 ((150,200),(200,250))
# remember to avoid your other lines
# remember to set the pen color before your call

# ADD YOUR SQUARE FUNCTION CALLS HERE
# in quadrant 2

lab06.drawSquareFL((-200,200),50)
lab06.drawSquareG ((-250,200), 50)
lab06.drawSquareFR((-200,250),50)
lab06.drawSquare((-250,250),10,50)
# I'd suggest making all your squares the same size, say 50 pixels wide
# remember to avoid your other squares

# ADD YOUR TRIANGLE FUNCTION CALLS HERE
# in quadrant 3

lab06.drawTriFL ((-200,-200), 10, 50)
lab06.drawTri ((-250,-150), (-300,-200), (-200, -200))
lab06.drawFilledTri ((-190,-150), 120, 50)
# remember to avoid your other triangles

hideturtle() # aesthetically pleasing to remove the turtle from final drawing,
             # but you want to show the turtle and its orientation as you draw
done() # hold on to the screen, I'm not done admiring my squares


