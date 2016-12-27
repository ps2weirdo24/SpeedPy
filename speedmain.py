import pyspeedtest

"""
connectionAlive = True

st = pyspeedtest.SpeedTest()
try:
	the_ping = st.ping()
except:
	connectionAlive = False

print("Connected: %s" % (str(connectionAlive)))

if connectionAlive:
	the_down = st.download()
	the_up = st.upload()
	the_ping = str(int(the_ping))
	the_down = ("%.2f" % (the_down/1000000))
	the_up = ("%.2f" % (the_up/1000000))
	print("Ping: %s" % (str(the_ping)))
	print("Download: %s" % (str(the_down)))
	print("Upload: %s" % (str(the_up)))





print("Done!")
"""