class Solution:
    def countTestedDevices(self, batteryPercentages):
        count = 0
        decrease = 0
        
        for percent in batteryPercentages:
            if percent > decrease:
                count += 1
                decrease += 1 
        
        return count