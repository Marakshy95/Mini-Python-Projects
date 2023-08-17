highest_bidder_bid = 0

def compare_bidders():
  for key in bidders:
    if bidders[key] > highest_bidder_bid:
      highest_bidder_bid = bidders[key]


bidders = {
          }

final_bidder = False
while not final_bidder:
  user_name = input("What is your name? ")
  bid_amount = int(input("How much do u wanna bid? "))
  bidders[user_name] = bid_amount
  compare_bidders()
  more_bidders_question = input("Do you want to go again? ")
  if more_bidders_question == "No":
      final_bidder = True
      print(bidders)
  else:
      print(bidders)
      print(f"Congrats you wont {highest_bidder_bid}")
