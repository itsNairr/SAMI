from ultralytics import YOLO
import pyrealsense2 as rs
import numpy as np
import cv2

crack_detect=YOLO("best.pt")

#initialize real-sense camera
#object that manages the flow of data from the camera
pipe = rs.pipeline()
#Create a config object, which is used to configure the camera for streaming
config = rs.config()

#Stream --> continous flow of data coming from the camera
#Image resolution 640 x 480, 8 bits per channel, and 30 FPS
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
#Depth is 16 bits per pixel, 30 FPS
#config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)

#Create alignment object (is used later to align depth frames to color frames)
align = rs.align(rs.stream.color)

pipe.start(config)
try: 
    while True:
        frames=pipe.wait_for_frames()
        color_frame=frames.get_color_frame()

        #if there is no frame continue
        if not color_frame: 
            continue 
        #(480,640,0) image height: 480, image width: 640, and 3 colour channels (BGR)
        image_array=np.asanyarray(color_frame.get_data())

        YOLO_results=crack_detect.predict(image_array, conf=0.4)

        #draw resultls on the image
        annotated_image = YOLO_results[0].plot()
        cv2.imshow("Crack Segmentation", annotated_image)
        if cv2.waitKey(1) & 0xFF == ord(" "):
            break

finally:
    pipe.stop()
    cv2.destroyAllWindows()
