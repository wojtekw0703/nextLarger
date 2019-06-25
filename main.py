def nextLarger(A):

    stack =[]
    ans = []
    for x in A[::-1]:
        while stack and x > stack[-1]:
            stack.pop()
        ans.append(stack[-1] if stack else -1)
        stack.append(x)
    return ans[::-1]


A = [6, 7, 3, 8]
print(nextLarger(A))
