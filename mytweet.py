from twython import TwythonStreamer

exec(open("initkeys.py").read())

count = 0

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            global count
            count = count + 1
            if count >= 3:
                print("Ian G. Harris is popular!")

stream = MyStreamer(c_k, c_s, a_t, a_s)

stream.statuses.filter(track="Ian G. Harris")
