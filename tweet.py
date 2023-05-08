from twython import TwythonStreamer
exec(open("initkeys.py").read())

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print("Got it")
        
stream = MyStreamer(c_k, c_s, a_t, a_s)
stream.statuses.filter(track="harris_iot")
