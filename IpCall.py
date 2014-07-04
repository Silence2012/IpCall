__author__ = 'u1404'
import ipaddress
import sys
class IpCall(object):
    '''This is an ip class'''
    listIp = []
    listIpUsed =[]
    def ip2file(self):
        '''Make the ip that used into a file'''
        with open("ipUsed.txt","w") as fs:
            for i in range(len(self.listIpUsed)):
                fs.writelines(self.listIpUsed[i]+'\n')
        with open("ip.txt","w") as f:
            for i in range(len(self.listIp)):
                f.writelines(self.listIp[i]+'\n')
    def ip_direct_req(self,ipNum):
        '''Get an ip from a file'''
        if ipNum > 0:
            print "The new ip is : "
            for i in range(ipNum):
                if self.listIp:
                    ipData = self.listIp.pop(-1)
                    print ipData
                    self.listIpUsed.append( ipData)
                else:
                    print "The ip pool is used up."
            print "The list of ip that is used is: %s" % self.listIpUsed
            self.ip2file()
            print "assign success! "

    def ip_specify_req(self,ipData):
        '''Get the specify ip function'''
        if ipData in self.listIpUsed:
            print "It's an used ip , select another ip please!"
            print "The list of the ip that is used is : %s " % self.listIpUsed
        elif ipData in self.listIp:
            self.listIpUsed.append(self.listIp.pop(self.listIp.index(ipData)))
            print self.listIpUsed
            self.ip2file()
            print "assign success"
            print self.listIpUsed

        else :
            print 'The input data is out of the ip pool,redo it please!   '
            print self.listIp

    def ip_release(self,*args):
        '''This function is ursed to release ip'''
        for i in range(len(args[0])):
            print args[0]
            print args[0][i]
            if args[0][i] in self.listIpUsed:
                self.listIp.append(args[0][i])
                self.listIpUsed.remove(args[0][i])
                print 'release success'
                print self.listIpUsed
            else:
                print 'This Ip is not in used , check it please'
                print 'The list of the ip that is used is :' , self.listIpUsed
        self.ip2file()
    def open_ipfile_func(self):
        '''open the ip file '''
        with open("ip.txt") as fs:
            self.listIp = fs.readlines()
            if len(self.listIp) != 0:
                if self.listIp[-1] == '':
                    self.listIp.pop()
                for i in range(len(self.listIp)):
                    if self.listIp[i].find('\n') != -1:
                        self.listIp[i] = self.listIp[i][:-1]

            else:
                print  "the context of the ip.txt file is null! "
        with open("ipUsed.txt") as f:
            self.listIpUsed = f.readlines()
            if len(self.listIpUsed) != 0:
                if self.listIpUsed[-1] == '':
                    self.listIpUsed.pop()
                for i in range(len(self.listIpUsed)):
                    if self.listIpUsed[i].find('\n') != -1:
                        self.listIpUsed[i] = self.listIpUsed[i][:-1]


    def __init__(self):
        self.open_ipfile_func()
        if len(sys.argv) >= 3:
            choice = int(sys.argv[1])
            if choice == 1:
                self.ip_direct_req(int(sys.argv[2]))
            elif choice == 2:
                self.ip_specify_req(sys.argv[2])
            elif choice == 3 :
                self.ip_release(sys.argv[2:])
            else:
                print "The first argument should be 1,2 or 3."
        else :
            print "the number of argument is wrong !"


if __name__ == '__main__':
        pass
a=IpCall()


