#Assign. 1
#my_games = {"cricket", "football", "tennis"}
#friend_games = {"badminton", "cricket", "chess"}
#combine both sets so that you have all unique games between two sets
#print final set

# my_games = {"cricket", "football", "tennis"}
# friend_games = {"badminton", "cricket", "chess"}
# combination = my_games | friend_games
# print(combination)

#Assign. 2
#games = {"badminton", "cricket", "chess"}
# Try removing "throwball" without throwing any error
# Try removing "throwball" with throwing error if it doesnt exist

# games = {"badminton", "cricket", "chess"}
# games.remove("throw ball")
# games.discard("throw ball")
# print(games)

#Assign 3
#my_games = {"cricket", "football", "tennis"}
#friend_games = {"badminton", "cricket", "chess"}
# Find the games that are in first set but not in second set
# print result

# my_games = {"cricket", "football", "tennis"}
# friend_games = {"badminton", "cricket", "chess"}
# final = my_games.difference(friend_games)
# print(final)


#Assign 4
#my_games = {"cricket", "football", "tennis"}
# use clear() to empty set
# Then using update(), add items - baseball, golf, tennis
# copy it to another set
# print it

my_games = {"cricket", "football", "tennis"}
my_games.clear()
my_games.update({"baseball","golf","tennis"})
games =()
my_games == games

print(games)