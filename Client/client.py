import Pyro4
import Pyro4.errors
import time
import threading
import sys
import uuid
import os

def get_fileserver_object():
    uri = "PYRONAME:fileserver@localhost:7777"
    fserver = Pyro4.Proxy(uri)
    return fserver

if __name__=='__main__':
    f = get_fileserver_object()
    print(f.list())
    print(f.read('f2'))

def ping_server():
    global connected
    while True and connected:
        alive = communicate()
        if not alive:
            alive = communicate()
            if not alive:
                print("\nserver is down [DETECT BY ping ack]")
                break
        time.sleep(interval)
    close()

def job_ping_server_ping_ack() -> threading.Thread:
    t = threading.Thread(target=ping_server)
    t.start()
    return t

def gracefully_exits():
     # unregister device on server 
    server.connected_device_delete(id)
    print("disconnecting..")
    time.sleep(1.5)
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)