from collections import defaultdict

d = {'k1': 1}

# print(d['k2'])

d = defaultdict(object)

print(d['ONE'])

d = defaultdict(lambda: 0)

d['ONE']

d['TWO'] = 2

print(d)
