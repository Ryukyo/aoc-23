history = [[int(i) for i in s.split()] for s in open('day9.txt').read().split('\n') if s.strip()]

def extrapolate(history_entry):
        # base case: all elements 0
        if sum(i != 0 for i in history_entry) == 0:
            return 0
        
        m = []
        for i in range(len(history_entry) - 1):
            # calculate the difference between 2 consecutive elements
            m.append(history_entry[i+1] - history_entry[i])
        # return the most recent data history entry and recursively extrapolate on the calculated differences
        return history_entry[-1] + extrapolate(m)

print(sum(extrapolate(i) for i in history))
print(sum(extrapolate(i[::-1]) for i in history))