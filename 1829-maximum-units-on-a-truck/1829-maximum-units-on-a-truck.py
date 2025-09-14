class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: -x[1])
        totalnumber=0
        for numberboxes,units in boxTypes:
            if truckSize<=numberboxes:
                totalnumber+=(truckSize*units)
                break
            totalnumber+=(numberboxes*units)
            truckSize-=numberboxes
        return totalnumber