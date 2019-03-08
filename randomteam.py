from random import choice
listofplayers = ["Chiara", "Sadman", "Ludovica", "Francesco", "Massimo", "Leander"]
teamA = []
for x in listofplayers:
    playerA = choice(listofplayers)
    teamA.append(playerA)
    listofplayers.remove(playerA)
print("Team A:")
print(teamA)
print("Team B:")
print(listofplayers)

