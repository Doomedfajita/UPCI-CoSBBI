from gazesdk import *
import time
import sys


    #url = get_connected_eye_tracker()
    #t = Tracker(url)
    #t.run_event_loop()

    #t.connect()
    #t.start_tracking()

    #while True:
        #data = t.event_queue.get()
        #time.sleep(1)
        #print (data.left.gaze_point_on_display_normalized, 
               #data.right.gaze_point_on_display_normalized)
        #t.event_queue.task_done()

    #t.stop_tracking()
    #t.disconnect()

    #t.break_event_loop()

def start_eye_stream(pat_id='0'):
    """
    Code for running eye tracker.
        ->Should be started when on LEMR home screen.
        ->Should be terminated after user unloads page of the last desired patient case.
    """
    global t
    global out_file
    # should be started before going to patient case.
    # could look to see if there is a calibration code bindings
    url = get_connected_eye_tracker()
    t = Tracker(url)
    t.run_event_loop()
    #out_file = open(local_dir + 'eye_stream/'+pat_id+'_'+str(time.time()) + '.txt','w+')
    t.connect()
    t.start_tracking()

    while True:
        try:
            curr_time = time.time()
            while curr_time + .5 > time.time():
                data = t.event_queue.get()
                leftX = data.left.gaze_point_on_display_normalized[0]
                rightX = data.right.gaze_point_on_display_normalized[0]
                leftY = data.left.gaze_point_on_display_normalized[1]
                rightY = data.right.gaze_point_on_display_normalized[1]
                if leftX !=0.0:
                    if rightX:	x = (leftX+rightX)/2.0
                    else:	x = leftX
                else:	x = rightX
                if leftY !=0.0:
                    if rightY:	y = (leftY+rightY)/2.0
                    else:	y = leftY
                else:	y = rightY

            computeX = (leftX + rightX)/ 2
            computeY = (leftY + rightY)/ 2
            print'(' + str(computeX) + ", " + str(computeY) + ')\n'
            #out_file.write(str(x)+','+str(y)+','+str(curr_time)+'\n')

            t.event_queue.task_done()
        except KeyboardInterrupt:
            print '\nEye Tracking Terminated'
            t.stop_tracking()
            t.disconnect()
            sys.exit()
start_eye_stream()
