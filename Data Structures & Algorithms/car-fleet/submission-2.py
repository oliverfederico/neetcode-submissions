class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), key=lambda x: x[0],reverse=True)
        print(cars)
        fleets = 0
        times = []
        for p, s in cars:
            time = (target - p) / s
            print(time)
            print(times)
            if not times or time > times[-1]:
                times.append(time)
                fleets +=1
        return fleets




