class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank = 0
        minTank = float('inf')
        idx = None
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < minTank:
                minTank = tank
                idx = i
        return -1 if tank < 0 else (1 + idx) % len(gas)
