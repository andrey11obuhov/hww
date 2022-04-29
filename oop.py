class Hotel:
    def __init__(self, num_rooms):
        self._rooms = [0 for _ in range(num_rooms)]

    def occypy(self, room_id):
        if self._rooms[room_id] == 0:
            self._rooms[room_id] = 1
        else:
            raise RuntimeError("Номер занят")

    def oc(self):
        return self._rooms.count(1)

    def money(self):
        return 5000*self._rooms.count(1)
    def free(self, room_id):
        self._rooms[room_id] = 0

    def __str__(self):
        a = ''
        for i in range(len(self._rooms)):
            if self._rooms[i] == 0:
                a += 'Номер ' + str(i + 1) + " свободен\n"
            else:
                a += 'Номер ' + str(i + 1) + " занят\n"
        return a

    def all_free(self):
        for i in range(len(self._rooms)):
            self._rooms[i] = 0


hotel = Hotel(5)
print(hotel._rooms)
hotel.occypy(3)
print(hotel._rooms)
hotel.free(3)
print(hotel._rooms)
