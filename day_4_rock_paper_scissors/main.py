import random;

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rules = {
    0: {
        0 : 'draw',
        1 : 'lose',
        2 : 'win'
    },
    1: {
        0: 'win',
        1: 'draw',
        2: 'lose'
    },
    2: {
        0: 'lose',
        1: 'win',
        2: 'draw'
    }
}

options = {
    0: rock,
    1: paper,
    2: scissors
}

computer_choice = random.randint(1, 3);
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."));

result = rules.get(player_choice);
result = result.get(computer_choice);

print("\n You Chose:")
print(f"{options.get(player_choice)} \n");

print("Computer Chose:")
print(f"{options.get(computer_choice)} \n");

print(f"You {result}")
