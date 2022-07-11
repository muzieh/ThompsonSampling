import random
import numpy as np
import matplotlib.pyplot as plt

N = 10000
successProbability = [0.01, 0.2, 0.24, 0.10, 0.12, 0.22, 0.18]
d = len(successProbability)
posResponses = np.zeros(d)
negResponses = np.zeros(d)
selectedCount = np.zeros(d)
selections = []
for i in range(N):
    selected = 0
    maxRnd = 0
    for j in range(d):
        currentRnd = random.betavariate(posResponses[j] + 1, negResponses[j] + 1)
        if currentRnd > maxRnd:
            maxRnd = currentRnd
            selected = j
    if random.random() < successProbability[selected]:
        posResponses[selected] += 1
    else:
        negResponses[selected] += 1
    selectedCount[selected] += 1
    selections.append(selected)

plt.hist(selections)
plt.show()

