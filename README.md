# UPCI-CoSBBI
Javascript app, integrating eyetracking and medical data visualization to create a predictive algorithm for AOI in scans. 

>>gazestuff.py is an altered version of code originally written by Andrew King.  This is built off of the Gaze SDK which has dependancies Cython,
and Python 2.7. 

### Roadmap:
* AMI.js in browser:  ✅
* Eyetracking visualization in browser: ✅
* Refine Eyetracking Accuracy:  ❌
* Eyetracking visualization overlay in AMI.js:  ❌
* Canvas open on medical image:  ❌
* Export coordinates (x,y,t) relative to image:  ❌ 
* Calculate fixations using algorithm:  ❌
* Associate fixations with heatmap/ranking system:  ❌
* Installation package:  ❌
* Docs: ❌


### Usage:
-----------------------------------
##### Pre-requisites:
*Bash Ubuntu on Windows, not necessary for eyetracking, but necessary for ami.js
*Windows 10
*Python 2.7
-----------------------------------
##### Instructions for eye tracking visualization:
1. Download gazesdk from balancana
1. Install AMI.js (this requires node, among other things.  See their git @ FNNDSC)
1. Check to make sure node is up to date
1. Dowload this repository
1. Navigate to where you downloaded it
1. run "gazestuffold.py" (this continuously dumps coordinates into eyetrackingdata.json)
1. run `node server.js` to initialize server at localhost
    1. To view this file in browser, navigate to http:/localhost:3000/data **NOTE you must have CORS enabled for this to work
    1. To enable CORS on chrome, simply open a command promt, navigate to your chrome installation folder, and type `chrome.exe --user-data-dir="C:/Chrome dev session" --disable-web-security`.  This will open an instance of chrome with CORS enabled.  
    Then you will be able to view the hosted JSON file.
1. Copy and paste the filepath to the directory where you downloaded the repository into the browser, the filepath should end with test.html
1. The black square marks your vision

#Patch Notes:

App #2 (7/27/17):  Integrated server script within app running on localhost:3000.  Path to eyetrackingdata.json is localhost:3000/data.  Fixed issues with app compatibility.  Still having issues with window resize, fix coming soon.





>>>>>>> 1895de41e45b058ee3d8f6db77787403703ca602
