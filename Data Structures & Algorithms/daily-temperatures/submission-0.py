class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days = [0]*len(temperatures)
        for i in range(len(temperatures)-1, -1, -1):
            while days[i] + i + 1 < len(temperatures):
                if temperatures[i] >= temperatures[days[i] + i + 1]:
                    if days[days[i] + i + 1] == 0:
                        days[i] = 0
                        break
                    days[i]+=days[days[i] + i + 1]
                else:
                    days[i]+=1
                    break
        return days
