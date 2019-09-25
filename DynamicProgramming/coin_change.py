'''
Given a value N, if we want to make change for N cents, and we have infinite supply of each of S = { S1, S2, .. , Sm} valued coins, 
how many ways can we make the change? The order of coins doesn’t matter.

For example, for N = 4 and S = {1,2,3}, there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}. 
             So output should be 4. 
             For N = 10 and S = {2, 5, 3, 6}, there are five solutions: {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}. 
             So the output should be 5.
'''


def no_ways_make_change(total_value, coins):
    table = [0]* (total_value + 1)
    table[0] = 1
    for coin in range(len(coins)):
        print(table)
        for value in range(coins[coin], total_value + 1):
            table[value] += table[value-coins[coin]]
    print(table)
    return table[-1]
  
value = 5
coins = [1, 2, 3]
no_ways_make_change(value, coins)  
