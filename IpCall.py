__author__ = 'u1404'
import ipaddress
import random

class IpCall(object):
    '''This is an ip class'''
    dt ={}
    listIp = []
    listIpUsed =[]
    def list2dict(self):
        '''Change the ip list into a ip dict'''
        for i in range(len(self.listIp)):
            self.dt[self.listIp[i]] = i

    def ip2file(self):
        '''Make the ip that used into a file'''
        with open("ipUsed.txt","w") as fs:
            for i in range(len(self.listIpUsed)):
                fs.writelines(self.listIpUsed[i]+'\n')
            #fs.flush()

    def ip_direct_req(self,ipNum):
        '''Get an ip from a file'''
        if ipNum > 0:
            while ipNum:
                if self.listIp:
                    lista = self.listIp.pop(-1)
                    print lista
                    self.listIpUsed.append(lista)
                else:
                    print "The ip pool is used up."
                    break

                ipNum -= 1
            #print self.listIpUsed
            self.ip2file()
        #print "ip_dirct_req does"
        #print self.listIpUsed

    def ip_specify_req(self,ipData):
        '''Get the specify ip function'''

        if ipData in self.listIpUsed:
            print "It's an used ip , select another ip please!"
            print self.listIpUsed

        elif ipData in self.listIp:
            self.listIpUsed.append(self.listIp.pop(self.listIp.index(ipData)))
            print self.listIpUsed

            self.ip2file()
            print "assign success"
            return True
        else :
            print 'The input data is out of the ip range,redo it please!   '
    def ip_release(self,dataIp):
        '''This function is ursed to release ip'''
        if dataIp in self.listIpUsed:
            self.listIp.append(dataIp)
            self.listIpUsed.remove(dataIp)
            print 'release success'
            print self.listIpUsed
        else:
            print 'This Ip is not in used , check it please'


    def open_file_func(self,filename):
        '''open the ip file '''
        with open(filename) as fs:
            #print fs.readlines()
            self.listIp = fs.readlines()
            if self.listIp[-1] == '':
                self.listIp.pop()

            #print self.listIp
    def ip_init(self):
        '''Generate an ip range into a file'''
        #dataIp = raw_input('input the CIDR network (e.g.,192.168.1.0/24):  ')
        dataIp = u"192.168.1.0/24"
        net = ipaddress.ip_network(dataIp)
        with open("ip.txt",'wt') as f:
            for i in net :
                f.writelines(str(i))
                f.write('\n')


    def __init__(self):
        self.ip_init()
        self.open_file_func('ip.txt')

        print '1.input an ip range       '
        print '2.input a specify ip      '
        print '3.input the released ip   '
        while True:
            #print self.listIpUsed
            #self.ip2file()
            choice = input("intput your choice:  ")
            if not choice:
                break
            elif choice == 1:
                num = input('input the number of ip you want to get:  ')
                self.ip_direct_req(num)
            elif choice == 2:

                while True:
                    ipData = raw_input('input the specify ip(e.g.,192.168.1.x):  ')
                    if not ipData:break
                    state = self.ip_specify_req(ipData)
                    if state:
                        break
            elif choice == 3:
                dataIp = raw_input("Input the ip which you want to release :")
                self.ip_release(dataIp)
            else:
                print "choise the 1 , 2 or 3  !"

    if __name__ == '__main__':
        pass



a = IpCall()
