from gazesdk import *
import time
import sys
import json
import random
import Tkinter as tk

listOfFixations = {}
timeout = time.time() + 10
nameCounter = 0

def start_eye_stream(pat_id='0'):
   
    global listOfFixations
    global t
    global out_file
    global nameCounter
   
    url = get_connected_eye_tracker()
    t = Tracker(url)
    t.run_event_loop()
    #out_file = open(local_dir + 'eye_stream/'+pat_id+'_'+str(time.time()) + '.txt','w+')
    t.connect()
    t.start_tracking()

    window = []
    xPrev = 0
    yPrev = 0
    fixNum = 0
    counter = 0
    
    currentTime = time.time()

    while True:
        try:
            data = t.event_queue.get()
            leftX = data.left.gaze_point_on_display_normalized[0]
            rightX = data.right.gaze_point_on_display_normalized[0]
            leftY = data.left.gaze_point_on_display_normalized[1]
            rightY = data.right.gaze_point_on_display_normalized[1]
            # if leftX !=0.0:
            #       if rightX:	x = (leftX+rightX)/2.0
            #       else:	x = leftX
            # else:	x = rightX

            # if leftY !=0.0:
            #       if rightY:	y = (leftY+rightY)/2.0
            #       else:	y = leftY

            currentX = ((leftX + rightX)/ 2) * 1920
            currentY = ((leftY + rightY)/ 2) * 1080

            # coordinates = {}

            # coordinates["location"] = {
            #     'xCoordinate': currentX,
            #     'yCoordinate': currentY
            # }


            #Just remember that you are appending fixations as 
            if ((currentX - xPrev)**(2) + (currentY - yPrev)**(2))**(.5) > 60:
                if window:
                    for i in window:
                        listOfFixations[str(nameCounter)] = {
                            'X':  i[0],
                            'y':  i[1],
                            'num':  i[2]
                        }
                        nameCounter += 1
                    window = []
                    fixNum += 1
                    counter = 0
                else:
                    pass 
                xPrev = currentX
                yPrev = currentY
            elif ((currentX - xPrev)**(2) + (currentY - yPrev)**(2))**(.5) < 60:
                window.append([currentX, currentY, fixNum])

            # if time.time() = currentTime:
            #     break

            #print(output)

            #file = open("eyetrackingdata.txt", "w")
            #file.write(str(computeX) + ',' + str(computeY) + ',' + str(time.time()))
            #readfile = open("eyetrackingdata.txt", 'r').read()
            #print(readfile)

                #out_file.write(str(x)+','+str(y)+','+str(curr_time)+'\n')
                #help.append[computeX, computeY, curr_time]
            #t.event_queue.task_done()



        except KeyboardInterrupt:
            print(listOfFixations)
            try:
                with open("eyetrackingdata.json", "w") as f:
                    f.write(json.dumps(listOfFixations))
            except:
                pass
            
            print '\nEye Tracking Terminated'
            t.event_queue.task_done()
            t.stop_tracking()
            t.disconnect()
            sys.exit()
            



start_eye_stream()
