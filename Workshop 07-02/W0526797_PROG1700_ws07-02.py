groceries = {
    "Apples": 3.50,
    "Bananas": 2.75,
    "Bread": 2.99,
    "Milk": 4.29,
    "Eggs": 3.49
}

total_cost = 0
total_quantity = 0
while True:
    item = input("Enter item to purchase (or 'done' to finish): ")
    if item.lower() == 'done':
        break
    if item in groceries:
        quantity = int(input(f"Enter quantity of {item}: "))
        total_quantity += quantity
        cost = groceries[item] * quantity
        if cost / quantity > 4:
            cost = cost * 0.9  # Apply 10% discount
            print("You get a discount!")
        print(f"{quantity} x {item} @ ${groceries[item]:.2f} each: ${cost:.2f}")
        total_cost += cost
    else:
        print(f"Item '{item}' not found in grocery list.")
print(f"Your total cost is: ${total_cost:.2f}")
print(f"Total quantity purchased: {total_quantity}")
print(f"Most expensive item: {max(groceries, key=groceries.get)} at ${max(groceries.values()):.2f}")

# --- 2. ---


students = []
grades = []
print("Enter student name (or 'done' to finish)")
while True:
    name = input("Enter student name: ")
    if name.lower() == 'done':
        break
    grade = float(input(f"Enter grade for {name}: "))
    if grade < 0 or grade > 100:
        print("Invalid grade. Please enter a grade between 0 and 100.")
        continue
    students.append(name)
    grades.append(grade)


print("\nStudent Grades:")
for i in range(len(students)):
    print(f"{students[i]:10} {grades[i]:.0f}")
print(f"Average grade: {sum(grades)/len(grades):.2f}")
print(f"Highest grade: {max(grades):.0f} {students[grades.index(max(grades))]}")
print(f"Lowest grade: {min(grades):.0f} {students[grades.index(min(grades))]}")
print(f"Honour roll:")
for i in range(len(grades)):
    if grades[i] >= 90:
        print(f"{students[i]:10} {grades[i]:.0f}") 


# --- 3. ---


scores = {"Alex": 12, "Priya": 18, "Jordan": 9}

print("Enter player name:")
while True:
    name = input("Player name (or 'done' to finish): ")
    if name.lower() == 'done':
        break
    if name in scores:
        points = int(input(f"Enter points scored by {name}: "))
        scores[name] += points
        continue

    # name not in scores
    answer = input("Player not found. Add as new player? (yes/no): ")
    if answer == 'yes':
        points = int(input(f"Enter points scored by {name}: "))
        scores[name] = points
    elif answer == 'no':
        continue
    else:
        print("Please answer 'yes' or 'no'.")
        continue

for name, points in scores.items():
    message = f"{name:10} {points} pts"
    if points >= 20:
        message += " (Level up!)"
    if points == max(scores.values()):
        message += " (Most EXP gained!)"
    print(f"{message}")


# --- 4. ---

songs = ["Sleepwalking", "Spectar", "Rain", "Sleepwalking"]
plays = [140, 132, 120, 140]

# Aggregate plays per song to handle duplicates
song_totals = {}
for s, p in zip(songs, plays):
    song_totals[s] = song_totals.get(s, 0) + p

# allow user to add new songs simply
print("Add songs (type 'done' to finish):")
while True:
    title = input("Song title: ")
    if title.lower() == "done":
        break
    try:
        p = int(input("Plays: "))
    except ValueError:
        print("Plays must be a whole number. Try again.")
        continue
    song_totals[title] = song_totals.get(title, 0) + p

# Unique songs (set), total and average
unique_songs = set(song_totals.keys())
total_plays = sum(song_totals.values())
average = total_plays / len(unique_songs) if unique_songs else 0

print("\nUnique songs:", unique_songs)
print("Total plays:", total_plays)
print(f"Average plays per song: {average:.2f}")

# Print each song and its total plays
for song, p in sorted(song_totals.items(), key=lambda kv: kv[1], reverse=True):
    print(f"{song}: {p} plays")


'''
song_totals = {}Creates an empty dictionary to store the total plays for each song.

for s, p in zip(songs, plays):

zip(songs, plays) pairs up elements from two lists: one with song names (songs) and one with play counts (plays).

s will take the song name, p will take the number of plays.

song_totals[s] = song_totals.get(s, 0) + p

song_totals.get(s, 0) checks if the song s is already in the dictionary.

If it is, it returns the current total; if not, it returns 0.

Then it adds the current play count p to the total and stores it back in song_totals[s].
'''