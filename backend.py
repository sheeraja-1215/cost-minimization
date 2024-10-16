def getMin(arr, N):
    minInd = 0
    for i in range(1, N):
        if arr[i] < arr[minInd]:
            minInd = i
    return minInd

def getMax(arr, N):
    maxInd = 0
    for i in range(1, N):
        if arr[i] > arr[maxInd]:
            maxInd = i
    return maxInd

def minOf2(x, y):
    return x if x < y else y

def minCashFlowRec(amount, N, result):
    mxCredit = getMax(amount, N)
    mxDebit = getMin(amount, N)

    if amount[mxCredit] == 0 and amount[mxDebit] == 0:
        return

    min = minOf2(-amount[mxDebit], amount[mxCredit])
    amount[mxCredit] -= min
    amount[mxDebit] += min

    result.append(f"Person {mxDebit+1} pays {min} to Person {mxCredit+1}")

    minCashFlowRec(amount, N, result)

def minCashFlow(graph, N):
    amount = [0 for _ in range(N)]
    for p in range(N):
        for i in range(N):
            amount[p] += (graph[i][p] - graph[p][i])

    result = []
    minCashFlowRec(amount, N, result)
    return result
