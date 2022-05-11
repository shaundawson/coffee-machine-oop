from prettytable import PrettyTable

# TODO Create a PrettyTable object and save it to a variable called table
table = PrettyTable()
print(table)

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Pokemon Type", ["Electric", "Water", "Fire"])

print(table)