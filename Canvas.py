from Tkinter import *
import json
import random

root= Tk()
root.protocol("WM_DELETE_WINDOW", root.quit())
canvas=Canvas(root,width=1920,height=1080)
canvas.pack()

with open('eyetrackingdata.json', 'r') as f:
    j = json.loads(f.read())
    num = 0
    r = lambda: random.randint(0,255)

    color = '#000000'
    for i in range(len(j)):
        if j[str(i)]['num'] != num: 
            color = '#%02X%02X%02X' % (r(),r(),r())
            canvas.create_oval(j[str(i)]['X'], j[str(i)]['y'], j[str(i)]['X'] + 10, j[str(i)]['y'] + 10, fill=color)
            num = j[str(i)]['num']
        else:
            canvas.create_oval(j[str(i)]['X'], j[str(i)]['y'], j[str(i)]['X'] + 10, j[str(i)]['y'] + 10, fill=color)
            num = j[str(i)]['num']
root.mainloop()

