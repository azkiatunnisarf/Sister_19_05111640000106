import Pyro4
import Pyro4.errors
import time
import threading
import sys
import uuid
import os

id = None
interval = 0
server = None
connected = True

def get_fileserver_object():
    uri = "PYRONAME:fileserver@localhost:7777"
    fserver = Pyro4.Proxy(uri)
    return fserver

if __name__=='__main__':
    f = get_fileserver_object()
    print(f.list())
    print(f.read('f2'))

def communicate():
    try:
        res = server.ok()
        if res.value == 'ok':
            pass
    except:
        return False
    return True

def ping():
    global connected
    while True and connected:
        alive = communicate()
        if not alive:
            alive = communicate()
            if not alive:
                print("\nconnection lost (ping ack)")
                break
        time.sleep(interval)
    close()

def job_ping_ack():
    t = threading.Thread(target=ping)
    t.start()
    return t

def job_heartbeat() -> threading.Thread:
    global id
    heartbeat = Heartbeat(id)
    t1 = threading.Thread(target=job_heartbeat_failure, args=(heartbeat,))
    t1.start()

    t = threading.Thread(target=expose_function_heartbeat, args=(heartbeat, id,))
    t.start()
    return heartbeat, t, t1

def job_heartbeat_failure(heartbeat):
    while True:
        if time.time() - heartbeat.last_received > 2*interval:
            print("\nserver is down [DETECT BY heartbeat]")
            break
        time.sleep(interval)
    close()

def close():
    server.connected_device_delete(id)
    print("disconnecting..")
    time.sleep(1.5)
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)

if __name__=='__main__':
    job_ping_ack()