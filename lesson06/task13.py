#Інвертування словника
from collections import defaultdict

d = {
  'apple': ['malum', 'pomum', 'popula'],
  'fruit': ['baca', 'bacca', 'popum'],
  'punishment': ['malum', 'multa']
}

print("Initial dictionary: ", d)

inverted_d = defaultdict(list)

for k, v in d.items():
   for val in v:
      inverted_d[val].append(k)

print("Inverted dictionary: ", dict(inverted_d))