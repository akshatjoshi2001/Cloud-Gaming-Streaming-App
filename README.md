# Cloud-Gaming-Streaming-App

Cloud gaming apps are starting to become popular these days  (example Stadia, Project xCloud, GeForce Now). 

I wanted to create something similar so that I can understand the challenges invloved in creating such services.

This uses win32gui and PIL to capture the screen, compress them to JPEG, and uses a flask server to stream it (Motion JPEG). In this case I am capturing the screen of a PSP emulator (PPSSPP).


It is in very initial stages.

## To do

* MJPEG is very slow (upto 5 FPS). I wish to migrate to AV1/VP9 codecs. Will have to see how to do it.
* I haven't added controls yet. Will be using WebSockets in the future for controls.


