import os
# 0:Surprise, 1:Fear, 2:Disgust, 3:Happiness, 4:Sadness, 5:Anger, 6:Neutral
dict = {"angry":5,"disgust":2,"fear":1,"happy":3,"neutral":6,"sad":4,"surprise":0}
directory = 'datasets/fer2013'

# Open the directory and view its contents
contents = os.listdir(directory)
f = open("ferEmoLabellist.txt", "a")

for dir in contents:
    dirpath= os.path.join(directory, dir)
    classes = os.listdir(dirpath)
    for item in classes:
        lable = dict[item]
        path= os.path.join(dirpath, item)
        images = os.listdir(path)
        for img in images:
            f.write(img + " "+ str(lable)+ "\n")

f.close()



f = open("ferEmoLabellist.txt",'r')
filedata = f.read()
f.close()

newdata = filedata.replace("PrivateTest", "Test").replace("PublicTest", "Test")

f = open("ferEmoLabellist.txt",'w')
f.write(newdata)
f.close()



