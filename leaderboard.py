#Create the dictionary
leaderboard = {}

#Take the input values of a name, anda score
Name = input("Name: ")
Score = input("Score: ") 

# Assign the name a score, and append it to the dictionary
leaderboard[Name.upper()] = Score

#Print the leaderboard data
print(leaderboard)

