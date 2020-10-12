from random import choices
# Estimate the probability of getting 5 or more heads from 7 spins
# # of a biased coin that settles on heads 60% of the time.
def trial():
     return choices('HT', cum_weights=(0.60, 1.00), k=7).count('H') >= 5

x = sum(trial() for i in range(10_000)) / 10_000
print(x)
