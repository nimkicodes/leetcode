class Solution:
    def countTestedDevices(self, batteryPercentages):
        count = 0
        
        for percent in batteryPercentages:
            if percent > count:
                count += 1
        
        return count