class Elevator:
    def __init__(self, total_floor=5, now_floor=3):
        self.total_floor = total_floor
        self.now_floor = now_floor

    def up(self):
        if self.now_floor < self.total_floor:
            self.now_floor += 1
            print('Лифт поднимается на ' + str(self.now_floor) + ' этаж')
        else:
            print('Лифт не может подняться выше')

    def down(self):
        if self.now_floor > 1:
            self.now_floor -= 1
            print('Лифт опускается на ' + str(self.now_floor) + ' этаж')
        else:
            print('Лифт не может опуститься ниже')


elevator = Elevator(7, 6)
for i in range(8):
    elevator.up()
for i in range(8):
    elevator.down()
