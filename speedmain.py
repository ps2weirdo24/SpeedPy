# DOWN = 11-15
# UP = 2-3


import pyspeedtest
import arrow
import time
import schedule
import json


st = pyspeedtest.SpeedTest()
TO_CONNECT = "https://www.google.com/"
DOWN_MIN = 11
DOWN_MAX = 15
UP_MIN = 2
UP_MAX = 3 
ALLOWANCE = .5
IS_OVER_ALLOWANCE = None


def data_to_str(the_float, dec_allow):
	if (the_float >= dec_allow):
		nice_percent = "%.2f" % (the_float*100)+"%"
		return(nice_percent)
	else:
		nice_percent = "%.2f" % (the_float*100)+"% ***"
		return(nice_percent)

def record_results(conn_obj):
	right_now = arrow.now("US/Pacific").format('YYYY-MM-DD HH:mm:ss')
	if conn_obj["conn"]:
		#if ((DOWN_MIN+DOWN_MAX)/2.0) >= ALLOWANCE
		percents = {"down_low": (float(conn_obj["down"])/DOWN_MIN),
					"down_middle": (float(conn_obj["down"])/((DOWN_MIN+DOWN_MAX)/2.0)),
					"up_low": (float(conn_obj["up"])/UP_MIN),
					"up_middle": (float(conn_obj["up"])/((UP_MIN+UP_MAX)/2.0))}
		to_write = "\n%s, %s, %s, %s, %s" % (right_now, str(conn_obj["conn"]),
									   str(conn_obj["down"]), str(conn_obj["up"]),
									   str(conn_obj["ping"]))
		second_write = "\n\t%s, %s, %s, %s, %s" % (str(ALLOWANCE),data_to_str(percents["down_low"],ALLOWANCE),
											   data_to_str(percents["down_middle"],ALLOWANCE),
											   data_to_str(percents["up_low"],ALLOWANCE),
											   data_to_str(percents["up_middle"],ALLOWANCE))
		txt_log = open("log.txt","a")
		txt_log.write((to_write+second_write))
		txt_log.close()
		print((to_write+second_write))
	else:
		to_write = "\n==========%s===Can't Connect==========" % (right_now)
		txt_log = open("log.txt", "a")
		txt_log.write(to_write)
		txt_log.close()
		print(to_write)

def connect_to(dest):
	connectionAlive = True
	the_down = 0
	the_up = 0
	the_ping = 0
	to_return = None	
	try:
		the_ping = st.ping()
		the_down = st.download()
		the_up = st.upload()
	except:
		connectionAlive = False
		return({"conn": False,"ping": 0,"down": 0,"up": 0})

	#print("Connected: %s" % (str(connectionAlive)))

	if connectionAlive:
		the_ping = str(int(the_ping))
		the_down = ("%.2f" % (the_down/1000000))
		the_up = ("%.2f" % (the_up/1000000))
		#print("Ping: %s" % (str(the_ping)))
		#print("Download: %s" % (str(the_down)))
		#print("Upload: %s" % (str(the_up)))
		return({"conn": True,"ping": the_ping,"down": the_down,"up": the_up})

def main():
	record_results(connect_to(TO_CONNECT))


if __name__ == "__main__":
	schedule.every(10).seconds.do(main)
	while True:
		schedule.run_pending()
		time.sleep(1)