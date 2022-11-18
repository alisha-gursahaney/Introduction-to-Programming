player = input("What player would you like to calculate statistics for? ")
opponent = input("What team was the opponent in the game you would like to calculate statistics for? ")
pa3 = input(f"How many 3's did {player} attempt this game? ")  # pa3 = player attempted 3's
pm3 = input(f"How many 3's did {player} make this game? ")  # pm3 = player made 3's
pa2 = input(f"How many 2's did {player} attempt this game? ")  # pa2 = player attempted 2's
pm2 = input(f"How many 2's did {player} make this game? ")  # pm2 = player made 2's
paf = input(f"How many free throws did {player} attempt this game? ")  # paf = player attempted free throws
pmf = input(f"How many free throws did {player} make this game? ")  # pmf = player made free throws
fgp = (int(pm3) + int(pm2)) / (int(pa3) + int(pa2)) * 100  # calculating field goal percentage
ftp = (int(pmf) / int(paf)) * 100  # calculating free throw percentage
print(f"{player} had a {fgp}% field goal percentage and a {ftp}% free throw percentage")
print(f"{player} scored {(int(pm3) * 3) + (int(pm2) * 2 )+int(pmf)} points against {opponent}. Wahoowa! ")
