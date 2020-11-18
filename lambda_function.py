import pyinotify
import re
import os
import greengrasssdk
import json

# Creating a greengrass core sdk client
client = greengrasssdk.client('iot-data')
connected = False
lastconnectedstate = False
PATH = '/greengrass/ggc/var/log/system/runtime.log'

class EventHandler(pyinotify.ProcessEvent):
    def __init__(self, *args, **kwargs):
        super(EventHandler, self).__init__(*args, **kwargs)
        self.file = open(PATH)
        self.position = sum(1 for line in self.file)
        self.print_lines()

    def process_IN_MODIFY(self, event):
        isConnected = self.print_lines()
        if(lastconnectedstate != connected):
            client.publish(topic='connectivity/state',payload=json.dumps({"connected": isConnected }))
        lastconnectedstate = connected
        
    def print_lines(self):
        new_lines = self.file.read()
        last_n = new_lines.rfind('\n')
        if last_n >= 0:
            self.position += last_n + 1
            if(new_lines[:last_n].find('Reconnect failed, sleeping for') >= 0):
                connected = False
            if(new_lines[:last_n].find('MQTT connection connected.') >= 0):
                connected = True
        self.file.seek(self.position)
        return connected

def lambda_handler(event, context):
    return 'Hello from Lambda'

wm = pyinotify.WatchManager()
handler = EventHandler()
notifier = pyinotify.Notifier(wm, handler)
wm.add_watch(PATH, pyinotify.IN_MODIFY, rec=True)
notifier.loop()