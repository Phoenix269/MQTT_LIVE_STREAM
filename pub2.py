
import paho.mqtt.publish as publish # MQTT client
import cv2 #lib for openCV
import base64
import json

MQTT_SERVER = "localhost"
MQTT_PATH1 = "vid_chan"



def devcam():
	###########code for video streaming#######
	cap = cv2.VideoCapture(0)
	while True:
		# Capture frame-by-frame
		ret, frame = cap.read()
		frame = cv2.resize(frame, (640, 480))
		result, buffer = cv2.imencode('.jpg', frame)
		jpg_as_text = base64.b64encode(buffer)
		publish.single(MQTT_PATH1, jpg_as_text, hostname=MQTT_SERVER)
		frame_count = int(cap.get(cv2.CAP_PROP_FPS))
		#print(frame_count)
		cv2.imshow('frame',frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
		cap.release()
		cv2.destroyAllWindows()



if __name__== "__main__":
	devcam()

