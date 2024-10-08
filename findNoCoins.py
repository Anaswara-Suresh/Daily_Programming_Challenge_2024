def findNoCoins(coins, amount):
    coins.sort(reverse=True)
    count = 0  
    k = amount 
    
    for coin in coins:
        if k == 0:
            break
        count += k // coin
        k %= coin 
    
    if k != 0:
        return -1
    
    return count


print("Enter the values of coins with space in between:")
arr = list(map(int, input().split()))
print("Enter the total value:")
amount = int(input())

result = findNoCoins(arr, amount)

if result == -1:
    print("It's not possible to make the exact amount with the given coins.")
else:
    print(f"Minimum number of coins required: {result}")
