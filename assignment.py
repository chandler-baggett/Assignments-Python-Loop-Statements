# 1. The Range Riddle
# Task 1: Code Correction
for i in range(2, 5):
    print(7-i)

# Task 2: Your Mood Today
import random
days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
moods = ["Happy", "Sad", "Energetic", "Calm"]

for day in days_of_the_week:
    print("For " + day + ", I am " + random.choice(moods))

# Task 3: Going Backwards
for i in range(1, 11):
    print(11-i)

# 2. Double Scoop with Nested Loops
# Task 1: Code Correction
for i in range(3):
    for j in range(3):
        print("*")
print("\\n")

# Task 2: Your Mood Tracker
times_of_the_day = ["morning", "afternoon", "evening"]
for day in days_of_the_week:
    for time in times_of_the_day:
        print("On " + day + " " + time + ", I am " + random.choice(moods))

# Task 3: Multiplication Table
for row in range (1, 6):
    for col in range (1, 6):
        print(repr(row * col).rjust(4), end= " ")
        if col == 5:
            print("\n")

# 3. Mastering Python's For Loop
# Task 1: Code Correction
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

# Task 2: Your Mood Swings
i = 0
print("At 12AM I am " + random.choice(moods))
while i <= 23:
    if(i == 12 or i == 0):
        pass
    else:
        print("At " + (str(i % 12) if i > 12 else str(i)) + ("AM" if i <= 12 else "PM") + ", I am " + random.choice(moods))
    i += 1

# Task 3: The Persistent Loop
num = int(input("Please enter a number between 1 and 100: "))
num_list = []
i = 0
while i <= 50:
    random_num = random.randint(1, 100)
    num_list.append(random_num)
    i += 1

for elem in num_list:
    if elem == num:
        break
    else:
        print("The number was not found")

# 4. The Marshmallow Increment Challenge
# Task 1: Increment at the Start
marshmallows = 0
while marshmallows < 5:
    marshmallows += 1
    print("Added a marshmallow! Now there are " + str(marshmallows) + " marshmallows.")
# Prediction: Added a marshmallow! Now there are {1...2...3...4...5} marshmallows
    
# Task 2: Increment at the End
marshmallows = 0
while marshmallows < 5:
    print("Added a marshmallow! Now there are " + str(marshmallows) + " marshmallows.")
    marshmallows += 1
# Prediction: Added a marshmallow! Now there are {0...1...2...3...4} marshmallows
# The while loop is evaluated such that after the last line of the while loop is run, the condition is checked for trueness

# Task 3: Off-by-One Error Investigation
marshmallows = 0
marshmallow_bag = []
while marshmallows < 10:
    print("Added a marshmallow! Now there are " + str(len(marshmallow_bag)) + " marshmallows in the bag.")
    marshmallow_bag.append(i)
    marshmallows += 1

marshmallows = 0
marshmallow_bag = []
while marshmallows < 10:
    marshmallow_bag.append(i)
    marshmallows += 1
    print("Added a marshmallow! Now there are " + str(len(marshmallow_bag)) + " marshmallows in the bag.")

# off by one errors can be caused if you place the increment in apart of the loop that causes an unexpected output
    
# 5. Loop Condition Logic
# Task 1: Loop Condition Exploration
i = 0
while(True):
    if i == 5:
        break
    else:
        print("Here is a print statement!")
    i += 1

# 6. The Art of Loop Control
num = int(input("Please enter a number between 1 and 100: "))
num_list = []
i = 0
while i <= 50:
    random_num = random.randint(1, 100)
    num_list.append(random_num)
    i += 1

found = False
j = 0
while j < len(num_list):
    if num_list[j] == num:
        print("Your num was found at index " + str(j))
        found = True
    j += 1
else:
    print(f"Your num was " + ("not " if found == False else "") + "found")
# else block runs after the while loop

# Task 2: Loop Interruption with break
import datetime
while(True):
    seconds = datetime.datetime.now().second
    if seconds % 15 == 0:
        print(seconds)
        break
# breaking based on condition that seconds = 15, 30, 45, or 0
    
# Task 3: Skipping Iterations with continue
i = -1
while i < 100:
    i += 1
    if i % 3 == 0:
        # print(str(i) + " is divisible by 3!")
        # i += 1
        continue
    print(str(i) + " is not divisible by 3!")
# continue can be used to continue to the next iteration without the need to increase an iterator
    
# Task 4: The Placeholder pass
i = -1
while i < 100:
    # TODO: Implementation
    i += 1
    pass
# pass can be used as a placeholder for code that needs to be implemented in the future

# Task 1: Dice Rolling Simulator
import random

# Initialize a dictionary to keep track of dice roll frequencies
roll_count = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

# Let's roll the dice 10 times
for _ in range(10):
    dice_roll = random.randint(1, 6)
    # Update the roll_count dictionary
    roll_count[dice_roll] += 1
    print("You rolled a " + str(dice_roll) + "!")

# Print out the frequency of each number
for number, frequency in roll_count.items():
    print(f"Number {number} was rolled {frequency} times.")

# Task 2: Random Choice Game
stuff = ["shoes", "socks", "pants", "shirt", "hat"]
inp = input("Please choose one of the following that might be randomly selected by the computer: " + str(stuff) + ": ")
print("Your input is " + inp)
computers_choice = random.choice(stuff)
print("The computer randomly chose " + computers_choice)
if computers_choice == inp:
    print("You guessed correctly.")
else:
    print("You did not guess correctly.")

# Task 3: Shuffling a Deck
cards_list = []
i = 1
while i <= 52:
    cards_list.append(i)
    i += 1
print(cards_list)
random.shuffle(cards_list)
print(cards_list)
# shuffle can be used for randomization in gaming, making the world less predictable (or less boring)

# 8. The Random Challenge Course
# Task 1: The Guessing Game
inp = int(input("Please guess a number between 1 and 5: "))
num = random.randint(1, 5)
if(inp < num):
    print("Too low!")
elif(inp > num):
    print("Too high!")
else:
    print("Correct! The number was " + str(inp))

# Task 2: The Magic 8-Ball
eight_ball = ["It is certain",
              "It is decidedly so",
              "Without a doubt",
              "Yes definitely",
              "You may rely on it",
              "As I see it, yes",
              "Most likely",
              "Outlook good",
              "Yes",
              "Signs point to yes",
              "Reply hazy, try again",
              "Ask again later",
              "Better not tell you now",
              "Cannot predict now",
              "Concentrate and ask again",
              "Don't count on it",
              "My reply is no",
              "My sources say no",
              "Outlook not so good",
              "Very doubtful"]

inp = input("Ask the 8-ball a question: ")
print("Response: " + random.choice(eight_ball))

# Task 3: The Card Picker
suits = ['hearts', 'diamonds', 'spades', 'clubs']
ranks = ['two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king', 'ace']
suit = input("Enter an input from " + str(suits) + ": ")
rank = input("Enter an input from " + str(ranks) + ": ")

computers_suit = random.choice(suits)
computers_rank = random.choice(rank)

if suit == computers_suit and rank == computers_rank:
    print("You guessed correctly!")
else:
    print("You did not guess correctly")

# 9. Looping Lists - The Rhythm of Repetition
# Task 1: The for Loop DJ Set
# Our playlist of genres
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

# Initialize track number
track_number = 1

genre_dict = {'Jazz': 'Pretty smooth!', 'Rock': 'Alive and energetic!', 'Hip-hop': 'Fun beats!', 'Classical': 'Always classic!'}

# Spinning through the genres
for genre in genres:
    print(f"Track {track_number}: Now playing {genre}")
    print(genre_dict[genre])
    track_number += 1

# Task 2: The Remix Artist with while
# Our playlist is still going
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
i = 0  # We start at the first track

# Keep the party alive until we've reached a specific genre
stop_genre = 'Hip-hop'

# Keep the party alive until we've reached the end or the stop_genre
while i < len(genres) and genres[i] != stop_genre:
    print("Remixing: " + genres[i])
    i += 1  # Move to the next track

# Task 3: Light Show Technician Loop
# Our playlist needs a light show
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
unsuitable_genre = 'Classical'

for index in range(len(genres)):
    if genres[index] == unsuitable_genre:
        continue  # Skip the light show for this genre
    print(f"Track {index + 1}: {genres[index]} - Light show is on!")

# 10. Advanced Looping Techniques
# Task 1: The Selective DJ

# Selective playlist slice
selected_genres = genres[1:4]  # From Rock to Classical

# Loop through the selected slice
for genre in selected_genres:
    print("Selective play: " + genre)

# Task 2: The One-Liner Band with List Comprehensions
# List comprehension to append "Music" to each genre
music_genres = [genre + " Music" for genre in genres]
print(music_genres)

# Task 3: Numerical Beats with range
# Countdown with range
for number in range(10, 0, -1):
    print(number)
print("The beat drops now!")

