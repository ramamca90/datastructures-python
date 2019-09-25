'''
Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. 
In other words, given two integer arrays val[0..n-1] and wt[0..n-1] 
which represent values and weights associated with n items respectively. 
Also given an integer W which represents knapsack capacity, 
find out the items such that sum of the weights of those items of given subset is smaller than or equal to W.
You cannot break an item, either pick the complete item, or don’t pick it (0-1 property).
'''

# A Dynamic Programming based Python Program for 0-1 Knapsack problem 
# Returns the maximum value that can be put in a knapsack of capacity max_wt 
def knapSack(max_wt, wts, profites): 
    no_of_wts = len(wts)
    K = [[0 for x in range(max_wt + 1)] for x in range(no_of_wts + 1)] 
  
    # Build table K[][] in bottom up manner 
    for i in range(no_of_wts + 1): 
        for w in range(max_wt + 1): 
            if i==0 or w==0: 
                K[i][w] = 0
            elif wt[i-1] <= w: 
                K[i][w] = max(profites[i-1] + K[i-1][w-wts[i-1]],  K[i-1][w]) 
            else: 
                K[i][w] = K[i-1][w] 
#     for row in K:
#         print(row)
    tot_profit = K[no_of_wts][max_wt]
    print("Total profit:", tot_profit)
    
    ##printing weights to get profit K[no_of_wts][max_wt]
    
    print("Weight profit")
    w = max_wt 
    for i in range(no_of_wts, 0, -1): 
        if tot_profit <= 0: 
            break
        # either the result comes from the 
        # top (K[i-1][w]) or from (profits[i-1] 
        # + K[i-1] [w-wts[i-1]]) as in Knapsack 
        # table. If it comes from the latter 
        # one/ it means the item is included. 
        if tot_profit == K[i - 1][w]: 
            continue
        else: 
  
            # This item is included. 
            print(wts[i - 1], profites[i - 1]) 
              
            # Since this weight is included 
            # its value is deducted 
            tot_profit = tot_profit - profites[i - 1] 
            w = w - wts[i - 1] 
            
# Driver program to test above function 
profites = [60, 100, 120] 
wts = [10, 20, 30] 
max_wt = 50
knapSack(max_wt, wts, profites)
