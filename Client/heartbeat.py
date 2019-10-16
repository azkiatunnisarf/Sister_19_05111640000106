import Pyro4
import time
import threading

class Heartbeat(object):
    def __init__(self, id):
        self.counter = 0
        self.last_received = time.time()
        self.id = id
        self.connected_device_summary = {}
        self.connected_device = []
        self.connected_device_thread_job = []

def __connect_heartbeat_server(self, id):
        time.sleep(self.ping_interval())
        try:
            uri = "PYRONAME:heartbeat-{}@localhost:7777".format(id)
            server = Pyro4.Proxy(uri)
        except:
            return None
        return server

def __new_thread_job(self, id):
        server = self.__connect_heartbeat_server(id)
        server.add_heartbeat_summary(id)
        while True:
            try:
                res = server.signal_heartbeat_all_to_all(id)
                # print(res)
            except (Pyro4.errors.ConnectionClosedError, Pyro4.errors.CommunicationError) as e:
                print(str(e))
                break
            time.sleep(self.ping_interval())