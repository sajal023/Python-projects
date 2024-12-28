dic = {}


def bid_auction(n, amt):
    dic[n] = amt
    print(dic)


bidding = 0

while bidding == 0:
    name = input("enter the name: ")
    bid = int(input("enter the bid: "))
    bid_auction(name, bid)
    s = input("are there any other bidders? type 'Y' or 'N': ")
    if s == "N":
        bidding = 1
    else:
        "clear"

highest_bid = 0
i = 0
for i in dic:
    amount = dic[i]
    if amount > highest_bid:
        highest_bid = amount
print(f"Winner is {i} with highest bid {highest_bid}")
