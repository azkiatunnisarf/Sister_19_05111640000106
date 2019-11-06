import os
import Pyro4

class FileServer(object):
    def __init__(self):
        self.pyro_server = ["fileserver0","fileserver1","fileserver2"]
        self.pyro = dict()

    def pyro_connect(self):
        i = 0
        for list in self.pyro_server:
            uri = "PYRONAME:{}@localhost:7777" . format(list)
            self.pyro[i] = Pyro4.Proxy(uri)
            i+=1

    def ls(self):
        files = []
        path = os.getcwd()
        print path
        for r, d, f in os.walk(path):
            for file in f:
                if '.txt' in file:
                    files.append(file)

        return files

    def touch(self, name='filename000',isi=None):
        for x in range(0, len(self.pyro)):
            self.pyro[x].create(name, isi)

        path = os.getcwd()
        name = name
        filename = os.path.join(path, name)
        f = open(filename, "w+")
        f.write(isi)
        f.close()
        return "[ filename : {}, content : {} ]".format(name,isi)

    def cat(self,name='filename000'):
        path = os.getcwd()
        filename = os.path.join(path, name)
        if(os.path.exists(filename)):
            fd = os.open(filename, os.O_RDWR)
            ret = os.read(fd,16*1024)
            print ret
            os.close(fd)
            return ret
        else:
            return "file not found!"


    def update(self,name='filename000',content=''):
        for x in range(0, len(self.pyro)):
            self.pyro[x].update(name, content)

        path = os.getcwd()
        name = name
        filename = os.path.join(path, name)
        if(os.path.exists(filename)):
            f = open(filename, "w+")
            f.write(content)
            f.close()
            return "[ filename : {}, content : {} ]".format(name,content)
        else:
            return "file not found!"


    def rm(self,name='filename000'):

        flag = 0

        for x in range(0, len(self.pyro)):
            flag += 1
            self.pyro[x].delete(name)

        if(flag == len(self.pyro)):
            path = os.getcwd()
            filename = os.path.join(path, name)
            if(os.path.exists(filename)):
                os.remove(filename)
                return("successfully deleted")
            else:
                print "file not found!"
        else:
            return "Error"

if __name__ == '__main__':
    k = FileServer()