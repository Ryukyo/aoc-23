history = [[int(i) for i in s.split()] for s in open('day9.txt').read().split('\n') if s.strip()]

def extrapolate(history_entry):
        if sum(i != 0 for i in history_entry) == 0:
            return 0
        m = []
        for i in range(len(history_entry) - 1):
            m.append(history_entry[i+1] - history_entry[i])
        return history_entry[-1] + extrapolate(m)

print(sum(extrapolate(i) for i in history))
