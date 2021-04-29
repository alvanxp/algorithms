def count_subsets(num, sum):
    #TODO: Write - Your - Code
    n = len(num)
    dp = [[False for x in range(sum+1)] for y in range(n)]
    for i in range(n):
        dp[i][0] = True
    for i in range(1, sum+1):
        dp[0][i] = i == num[0]
    for i in range(1, n):
        for s in range(1, sum+1):
            if dp[i-1][s]:
                dp[i][s] = True
            elif s >= i:
                dp[i][s] = dp[i-1][s-num[i]]
    return -1


def main():
    print("Total number of subsets " + str(count_subsets([1, 1, 2, 3], 4)))
    print("Total number of subsets: " + str(count_subsets([1, 2, 7, 1, 5], 9)))


main()
