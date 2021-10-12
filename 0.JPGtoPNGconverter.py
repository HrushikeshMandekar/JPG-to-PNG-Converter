import sys
import os # or you can use pathlib module here
from PIL import Image

# grab first and second argument
photos_folder = sys.argv[1] # takes Photos/ input
new_folder = sys.argv[2] # takes new/ input 

# check is new folder exists, if not create it to put the images.
if not os.path.exists(new_folder):
    # os.path.exists(new_folder) tells whether the new folder exist or not
    os.makedirs(new_folder) # creates the new folder
    print(f"{new_folder} created! :)")
    
# loop through entire filder photos and convert images into png and save them into new folder.
i = 0   # used for counter
for fileName in os.listdir(photos_folder):
    # os.listdir(photos_folder) to traverse through the files in Photos folder.
    img = Image.open(f'{photos_folder}{fileName}')  
    only_name = os.path.splitext(fileName)[0] 
    # os.path.splitext(fileName) splet the file name into parts for e.g. tiger.jpg will be parted into ('tiger','.jpg'), [0] is used to access the first element.
    img.save(f"{new_folder}{only_name}.png", "png")
    i += 1
    print(f"{i} Done")

print(f"All DONE! Total number of files converted to .png format: {i}")


#~~~~~OUTPUT~~~~
#
#C:\Users\HP>cd Desktop\jpg to png converter
#C:\Users\HP\Desktop\jpg to png converter>0.JPGtoPNGconverter.py photos/ new/
#new/ created! :)
#1 Done
#2 Done
#3 Done
#4 Done
#5 Done
#6 Done
#7 Done
#8 Done
#9 Done
#10 Done
#All DONE! Total number of files converted to .png format: 10
#'''