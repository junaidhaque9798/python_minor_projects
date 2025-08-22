import ascii as art
print(art.logo)
logo = """
  ____  _       _       
 | __ )(_) __ _| | __ _ 
 |  _ \| |/ _` | |/ _` |
 | |_) | | (_| | | (_| |
 |____/|_|\__, |_|\__,_|
          |___/         
"""
print(logo)


def find_highest_bidder(bidding_dictionary):
    highest_bid = 0
    winner = ""
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"\nWinner is {winner} with a bid of {highest_bid}")


bids = {}
continue_bidding = True

while continue_bidding:
    name = input("What is your name? ")
    price = int(input("What is your bid? $"))
    bids[name] = price

    should_continue = input("Are there any other bidders? Yes or No? ").lower()

    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 100)  # Clears the screen (kind of)
