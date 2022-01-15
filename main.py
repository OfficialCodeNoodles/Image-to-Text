#Dependencies
from PIL import Image 

directory = input("Type the name of the image you would like to convert: ")

image = Image.open(directory) 
imageSize = image.size 
imageData = image.getdata() 

newWidth = int(input(
    "Type a new size in characters you want the image to be: "
)) 

#Scales height to match aspect ratio. 
newSize = [ newWidth, int(newWidth * (imageSize[1] / imageSize[0])) ]
#How many pixels it moves on both axis' per iteration. 
increment = [ imageSize[0] // newSize[0], imageSize[1] // newSize[1] ]
#Character array. Leftmost represents black and rightmost represents white. 
characters = [
    '`', '.', ',', '+', '=', 'o', 'x', 'X', 'Q', 'W', '@'
]

#Turns 2d-coordinate to 1d-coordinate for the imageData array.
def getIndex(coord: tuple) -> int:
    return (coord[1] * imageSize[0]) + coord[0]
#Gets pixel from image using a 2d-coordinate. 
def getPixel(coord: tuple) -> tuple:
    return imageData[getIndex(coord)]
#Takes the average of a colors components. 
def grayScale(color: tuple) -> int:
    return (color[0] + color[1] + color[2]) / 3

#Loops through the imageData array using 2 loops. The y is first because we 
#print out each line from the top left to the bottom right going line by line
#on the x-axis. 
for y in range(0, newSize[1]):
    for x in range(0, newSize[0]):
        #Generates new coordinate. 
        coordinate = ( x*increment[0], y*increment[1] )
        color = getPixel(coordinate)
        grayValue = grayScale(color)
        #Constrains charIndex to value between 0 and characters array size. 
        charIndex = grayValue // (255 / len(characters))
        charIndex = int(charIndex)

        #Prints new pixel (character). 
        print(characters[charIndex], end='')
    #Newline. 
    print() 

#This keeps the program open so you can take a picture if you want. 
input()