import os

class Backend(object):

    def __init__(self):
        pass

    def create(self,filename="",value=""):
        path = os.getcwd()
        name = filename
        filename = os.path.join(path, filename)
        f = open(filename, "w+")
        f.write(value)
        f.close()
        return "[ Nama file: {}, Isi : {} ]".format(name,value)

    def update(self,filename="",value=""):
        path = os.getcwd()
        name = filename
        filename = os.path.join(path, filename)
        if(os.path.exists(filename)):
            f = open(filename, "w+")
            f.write(value)
            f.close()
            return "[ Nama file: {}, Isi : {} ]".format(name,value)
        else:
            return "file not found!"

    def read(self,filename=""):
        path = os.getcwd()
        filename = os.path.join(path, filename)
        if(os.path.exists(filename)):
            fd = os.open(filename, os.O_RDWR)
            ret = os.read(fd,16*1024)
            print ret
            os.close(fd)
            return ret
        else:
            return "file not found!"


    def delete(self,filename=""):
        path = os.getcwd()
        filename = os.path.join(path, filename)
        if(os.path.exists(filename)):
            os.remove(filename)
            return("successfully deleted")
        else:
            return "file not found!"

    def show(self):
        files = []
        path = os.getcwd()
        print path
        # r=root, d=directories, f = files
        for r, d, f in os.walk(path):
            for file in f:
                if '.txt' in file:
                    files.append(file)

        return files



if __name__ == '__main__':
    k = Backend()
