README 

github: 
https://github.com/bchehraz/Eagle_Eye/tree/master

Program Instructions: 

1. Open gui.py file 
2. Decide if you want to use the webcam on your computer, or a pre-recorded video. 
	a. Pre-recorded must come from a stationary camera, such as a surveillance 		camera. 
3. Once the video feed is chosen, a new window with the selected video will open.
4. Once open, the video will play and will begin to track a moving object with a green, bounded box surround the object. 
	a. If it is a pre-recorded video, video will stop playing once it reaches the 	end of the video. 
	b. If using a live feed, video will continue to play until the user quits.  

Future Work: 
Originally we wanted to have an a way to detect little movements that aren’t important to the motion tracking, such as the wind blowing the trees, or curtains swaying in the wind, to not track that and only track important movement.
With more time, this would be added to not be worried about non-important movement in the video feed. 

Also, we wanted to be able to track multiple objects with its own boxes for each movement. With these boxes we could color code for each object. 
If we had more time, we would add this functionality to our project. 

With more time, we would’ve had a better GUI with more control over the video. Having the Video not open through opencv, but implemented into our own built GUI. With access buttons, like pause, play, stop, etc. 

Along with the boxes, if we had more time we would’ve had a background filter, that darkens the background while highlighting for better visibility the moving object that is being tracked. 

