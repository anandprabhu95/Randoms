import matplotlib.pyplot as plt

#init
xStart_ = 0.4
ratio_ = 0.1
numIters_ = 0
ratioList = []
equiXList = []


def logistic(ratio, xNow):
    xNext = ratio * xNow * (1 - xNow)
    return xNext


def equilibriumPopulation(ratio, xStart, numIters):
    x = xStart
    uniqueList = []
    while numIters < 100:
        x = logistic(ratio, x)
        x = round(x, 4)
        if numIters > 50 and x not in uniqueList:
            uniqueList.append(x)        
        numIters+=1
    return x, uniqueList


while ratio_ < 4:
    equiVars = equilibriumPopulation(ratio_, xStart_, numIters_)
    equiXList.extend(equiVars[1])

    for i in range(len(equiVars[1])):
        ratioList.append(ratio_)
    
    ratio_ += 0.0001

print(len(equiXList))
print(len(ratioList))
plt.scatter(ratioList, equiXList, s=0.05)
plt.show()

