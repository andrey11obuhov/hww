class Hotel:
    def __init__(self, nums):
        self._rooms = {"SGL": 0,"DBL": 0, "Junior suite":0, "Suite":0}
        self.sgl=nums[0]
        self.dbl=nums[1]
        self.js=nums[2]
        self.s=nums[3]


    def occypy(self, type):
        if type=="SGL":
            if  self._rooms["SGL"]<self.sgl:
                self._rooms["SGL"]+=1
            else:
                raise RuntimeError("Номер занят")
        if type=="DBL":
            if  self._rooms["DBL"]<self.dbl:
                self._rooms["DBL"]+=1
            else:
                raise RuntimeError("Номер занят")
        if type=="Junior suite":
            if  self._rooms["Junior suite"]<self.js:
                self._rooms["Junior suite"]+=1
            else:
                raise RuntimeError("Номер занят")
        if type=="Suite":
            if  self._rooms["Suite"]<self.s:
                self._rooms["Suite"]+=1
            else:
                raise RuntimeError("Номер занят")




    def oc(self):
        return self._rooms["SGL"]+self._rooms["DBL"]+self._rooms["Junior suite"]+self._rooms["Suite"]

    def money(self):
        return 5000*self._rooms["SGL"]+6000*self._rooms["DBL"]+12000*self._rooms["Junior suite"]+30000*self._rooms["Suite"]
    def free(self, room_type):
        if self._rooms[room_type]==0:
            print("Все номера свободны")
        else:
            self._rooms[room_type] -=1


    def all_free(self):
        self._rooms["SGL"] =0
        self._rooms["DBL"] =0
        self._rooms["Junior suite"] =0
        self._rooms["Suite"]=0



hotel = Hotel([5, 6, 9, 8])
print(hotel._rooms)
hotel.occypy("SGL")
hotel.occypy("SGL")
hotel.occypy("SGL")
hotel.occypy("DBL")
print(hotel.money())
print(hotel._rooms)
hotel.free("SGL")
print(hotel._rooms)
