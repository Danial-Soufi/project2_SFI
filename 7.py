# تعریف یک دسته ورق استاندارد
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
deck = [f"{rank} of {suit}" for suit in suits for rank in ranks]
for card in deck:
    print(card)
