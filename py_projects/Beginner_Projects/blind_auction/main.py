import art
print(art.logo)
# TODO-1: Ask the user for input

# TODO-2: Save data into dictionary {name: price}

# TODO-3: Whether if new bids need to be added

# TODO-4: Compare bids in dictionary
def compare_bid(bidding_dic):

    winner = ""
    highest_bid = 0
    for bidder in bidding_dic:
       bid = bidding_dic[bidder]
       if bid > highest_bid:
           highest_bid = bid
           winner = bidder

    print(f"The winner is {winner} with the highest bid of ${highest_bid}")


bids = {}
should_continue = True

while should_continue:
    name = input("What is your name? ")
    price = int(input("What is your bid? $"))
    bids[name] = price
    more_bids = input("Are there any other bidders? Type 'yes' or 'no' .").lower()
    if more_bids == 'no':
        should_continue = False
        compare_bid(bids)
    elif more_bids == 'yes':
        print("\n" * 20)

