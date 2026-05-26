import random

symbols = ['🍒', '🍇', '🍉', '7️⃣']

def play():
  results = random.choices(symbols, k=3)

  print(results[0], "|", results[1], "|", results[2])

  if results[0] == '7️⃣' and results[1] == '7️⃣' and results[2] == '7️⃣':
      print("Jackpot!!")
  else:
      print("Thanks for Playing!!")

while True:
    play()

    choice = input("Play again? (Y/N): ")

    if choice.upper() == 'N':
        print("Game Over!")
        break
