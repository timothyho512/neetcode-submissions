class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # The thinking would be we need to have something to be able to remember the day
        # it is counting for every element of the day

        # one of the solution I am thinking currently
        # is maybe we can have a stack that sotre a tuple including (the temperatur, and the index)

        # so we loop through the array,
        # put things into a stack
        # if the incoming temperature is higher, then we pop the stack, and we output[i] with the difference in the index (which is the date)

        # at the end, clear the stack and set output[i] to zero

        stack = []
        output = [0]*len(temperatures)

        for i, temp in enumerate(temperatures):

            if stack:
                s_i, s_t = stack[-1]
                while stack and s_t < temp:
                    s_i, s_t = stack.pop()
                    output[s_i] = i - s_i
                    
                    if stack:
                        s_i, s_t = stack[-1]
            
            stack.append((i, temp))

        return output