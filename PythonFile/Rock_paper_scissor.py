#game
#player 1
while True:
    player1 = input("player 1, plz choose 'rock' or 'scissor' or 'paper'\n")
    player2 = input("player 2, plz choose 'rock' or 'scissor' or 'paper'\n")
    a = "rock"
    b = "scissor"
    c = "paper"

    if player1 == player2:
        print("u guys just draw, noob")
    if player1 == a and player2 == b:
        print("player1 win")
    if player1 == b and player2 == c:
        print("player1 win")
    if player1 == c and player2 == a:
        print("player1 win")
    if player2 == a and player1 == b:
        print("player2 win")
    if player2 == b and player1 == c:
        print("player2 win")
    if player2 == c and player1 == a:
        print("player2 win")

    loop = input("cont or not")
    if loop == "no":
        break

