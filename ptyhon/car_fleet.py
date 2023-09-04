class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pos = sorted(position, reverse=True)
        d = dict(zip(position, speed))

        for i in pos:
            sp = d[i]
            time = (target - i) / sp
            if len(stack) > 0 and stack[-1] >= time:
                time = stack[-1]
                stack.pop()
            stack.append(time)

        return len(stack)
