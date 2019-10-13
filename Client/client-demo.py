import Pyro4
import os

uri = "PYRONAME:mypyro@locahost:7777"

def client_create(filename,value):
    server = Pyro4.Proxy(uri)
    print '\n'
    print(server.create_file(filename,value))
    print '\n'

def client_read(filename):
    server = Pyro4.Proxy(uri)
    print '\n'
    print(server.read_file(filename))
    print '\n'

def client_update(filename,value):
    server = Pyro4.Proxy(uri)
    print '\n'
    print(server.update_file(filename,value))
    print '\n'

def client_delete(filename):
    server = Pyro4.Proxy(uri)
    print '\n'
    print(server.delete_file(filename))
    print '\n'

def client_show():
    server = Pyro4.Proxy(uri)
    print '\n'
    print '\n'.join(server.show_file())
    print '\n'

def client_send(filename):
    name = filename
    path = os.getcwd()
    filename = os.path.join(path, filename)

    if (os.path.exists(filename)):
        fd = os.open(filename, os.O_RDWR)
        ret = os.read(fd, 16 * 1024)
        os.close(fd)
        client_create(name,ret)
    else:
        print "File not found"

def check_ping():
    #hostname = "myhost"
    response = os.system("ping -c 1")
    if response == 0:
        pingstatus = "active"
    else:
        pingstatus = "failure"
    return pingstatus


if __name__=='__main__':
    file = ""
    while True:
        print("nano | cat | update | rm | ls | ping | quit")
        cmd = raw_input("cmd (press enter) : ")
        if(cmd == 'nano'):
            filename = raw_input("filename => ")
            value = raw_input("value => ")
            client_create(filename,value)
        elif(cmd == 'cat'):
            filename = raw_input("filename => ")
            client_read(filename)
        elif(cmd == 'update'):
            filename = raw_input("filename => ")
            value = raw_input("value => ")
            client_update(filename,value)
        elif(cmd == 'rm'):
            filename = raw_input("filename => ")
            client_delete(filename)
        elif (cmd == 'ls'):
            client_show()
        elif (cmd == 'ping'):
            value = raw_input("")
            check_ping(value)
        elif(cmd == 'quit'):
            print("QUIT")
            exit()
        else:
            print("Input error")