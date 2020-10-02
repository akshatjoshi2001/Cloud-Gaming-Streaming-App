import numpy as np
import cv2
import time
from threading import Thread, Lock
from PIL import ImageGrab
import win32gui
from flask import Flask,Response

def enum_cb(hwnd, results):
    winlist.append((hwnd, win32gui.GetWindowText(hwnd)))
toplist, winlist = [], []
win32gui.EnumWindows(enum_cb, toplist)
ppsspp = [(hwnd, title) for hwnd, title in winlist if 'ppsspp' in title.lower()]
ppsspp = ppsspp[0]
hwnd = ppsspp[0]
win32gui.SetForegroundWindow(hwnd)

frame_en = None
frame_cache = None
lock = Lock()
def update():

def capt():
    while(True):
        global lock, frame_en
        bbox = win32gui.GetWindowRect(hwnd)
        img = ImageGrab.grab(bbox)
        img_np = np.array(img)
        img_np1 = cv2.resize(img_np,(360,240))
        
        # convert color space from BGR to RGB
        frame = cv2.cvtColor(img_np1, cv2.COLOR_BGR2RGB)
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 70]
        
        (flag, a) = cv2.imencode(".jpg", frame,encode_param)
        frame_cache = 
        with lock:
            frame_en = a
            #time.sleep(0.1)
            
        
        
         
t = Thread(target=capt,daemon=True)
t.start()
def gen():
    
    while(True):

        with lock:
            #print("Bytes written....")
            yield( b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(frame_en) + b'\r\n')

app = Flask(__name__)
@app.route('/')
def vidfeed():
    return Response(gen(),mimetype="multipart/x-mixed-replace; boundary=frame")

app.run(host="0.0.0.0",threaded=True)

