__author__ = 'u1404'
import ipaddress
import sys
class IpCall(object):
    '''This is an ip class'''
    listIp = []
    listIpUsed =[]
    def ip_used2file(self):
        '''Make the ip that used into a file'''
        with open("ipUsed.txt","w") as fs:
            for i in range(len(self.listIpUsed)):
                fs.writelines(self.listIpUsed[i]+'\n')
    def ip_direct_req(self,ipNum):
        '''Get an ip from a file'''
        if ipNum > 0:
            for i in range(ipNum):
                if self.listIp:
                    lista = self.listIp.pop(-1)
                    print lista
                    self.listIpUsed.append(lista)
                else:
                    print "The ip pool is used up."
                    break
            self.ip_used2file()

    def ip_specify_req(self,ipData):
        '''Get the specify ip function'''
        if ipData in self.listIpUsed:
            print "It's an used ip , select another ip please!"
            print self.listIpUsed
        elif ipData in self.listIp:
            self.listIpUsed.append(self.listIp.pop(self.listIp.index(ipData)))
            print self.listIpUsed
            self.ip_used2file()
            print "assign success"
            print self.listIpUsed

        else :
            print 'The input data is out of the ip pool,redo it please!   '
            print self.listIp

    def ip_release(self,dataIp):
        '''This function is ursed to release ip'''
        if dataIp in self.listIpUsed:
            self.listIp.append(dataIp)
            self.listIpUsed.remove(dataIp)
            print 'release success'
            print self.listIpUsed
        else:
            print 'This Ip is not in used , check it please'
        self.ip_used2file()
    def open_ipfile_func(self,filename):
        '''open the ip file '''
        with open(filename) as fs:
            self.listIp = fs.readlines()
            if self.listIp[-1] == '':
                self.listIp.pop()
            for i in range(len(self.listIp)):
                if self.listIp[i].find('\n'):
                    self.listIp[i] = self.listIp[i][:-1]

    def __init__(self):
        self.open_ipfile_func('ip.txt')
        if len(sys.argv) == 3:
            choice = int(sys.argv[1])
            if choice == 1:
                self.ip_direct_req(int(sys.argv[2]))
            elif choice == 2:
                self.ip_specify_req(sys.argv[2])
            elif choice == 3 :
                self.ip_release(sys.argv[2])
            else:
                print "The first argument should be 1,2 or 3."
        else :
            print "the number of argument is wrong !"


if __name__ == '__main__':
        pass
a=IpCall()


