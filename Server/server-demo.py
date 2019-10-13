from backend import *
import Pyro4

def server():
    daemon = Pyro4.Daemon(host="localhost")
    ns = Pyro4.locateNS("localhost",7777)
    x_GreetServer = Pyro4.expose(Backend)
    uri_greetserver = daemon.register(x_GreetServer)
    print("URI greet server : ", uri_greetserver)
    ns.register("mypyro", uri_greetserver)
    daemon.requestLoop()

if __name__ == '__main__':
    server()

