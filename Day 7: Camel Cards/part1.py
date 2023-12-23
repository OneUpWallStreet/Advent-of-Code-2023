from collections import defaultdict
import json
file = open("input.txt")

def hmForHand(hand: str) -> defaultdict:
    hm = defaultdict(int)
    for ch in hand: hm[ch] += 1
    return hm

rankCounter = 0
result = 0


rm = {
    "5oak": [],
    "4oak": [],
    "fh": [],
    "toak": [],
    "tp": [],
    "op": [],
    "hc": []
}


for line in file.readlines():
    data = line.strip().split(" ")
    hand, bid = data[0], data[1]
    rankCounter += 1

    hm = hmForHand(hand)

    # 5 of a kind
    if len(hm) == 1: 
        rm["5oak"].append((hand,bid))
        continue
    # High Card
    if len(hm) == 5: 
        rm["hc"].append((hand,bid))
        continue
    
    # Three of a kind & Two Pair
    if len(hm) == 3:
        if max(hm.values()) == 3: rm["toak"].append((hand,bid))
        else: rm["tp"].append((hand,bid))
        continue

    # Full House & Four of a kind
    if len(hm) == 2:
        if min(hm.values()) == 1: rm["4oak"].append((hand,bid))
        else: rm["fh"].append((hand,bid))
        continue

    # One Pair
    if len(hm) == 4: rm["op"].append((hand,bid))
    

def handSorter(hand):

    ls = []
    
    order = {
        "A": 1, "K": 2, "Q": 3, "J": 4, "T": 5, 
        "9": 6, "8": 7, "7": 8, "6": 9, "5": 10,
        "4": 11, "3": 12, "2": 13 }
    for ch in hand[0]:  ls.append(order[ch])
    return tuple(ls)


for hand in rm.values():
    hand.sort(key=handSorter)

    for _, bid in hand:
        result += int(bid) * rankCounter
        rankCounter -= 1

print("the total winnings: ", result)

