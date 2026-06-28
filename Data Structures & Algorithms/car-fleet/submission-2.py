class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # initially have max n groups
        # we need to know if a car can catch up to another car ahead of it, sort by position
        
        n = len(position)
        cars = sorted([(position[i], speed[i]) for i in range(n)], key = lambda x: x[0])

        # iterate through each car to see how long it will take to reach the destination, if the next car is slower or equal, we group.
        #print(cars)
        times = [(target - position)/speed for position, speed in cars]
        groups = n
        stack = [times[0]]
        for i in range(n):
            # if the current one is fastest, 
            while stack and stack[-1] <= times[i]:
                stack.pop()
            stack.append(times[i])
            #print(stack)
        
        return len(stack)