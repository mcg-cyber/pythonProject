class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.current_floor = bottom_floor
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor

    def go_to_floor(self, target_floor):
        if target_floor < self.bottom_floor or target_floor > self.top_floor:
            print("Invalid floor number")
            return

        while self.current_floor != target_floor:
            if self.current_floor < target_floor:
                self.floor_up()
            else:
                self.floor_down()

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator is now at floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator is now at floor {self.current_floor}")


class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]

    def run_elevator(self, elevator_num, target_floor):
        if elevator_num < 0 or elevator_num >= len(self.elevators):
            print("Invalid elevator number")
            return

        print(f"Running elevator {elevator_num} to floor {target_floor}")
        self.elevators[elevator_num].go_to_floor(target_floor)

    def fire_alarm(self):
        print("Fire alarm activated. Moving all elevators to the bottom floor.")
        for elevator in self.elevators:
            elevator.go_to_floor(self.elevators[0].bottom_floor)


# Test the Building class with fire alarm
building = Building(1, 10, 2)
building.run_elevator(0, 5)
building.run_elevator(1, 7)

building.fire_alarm()
