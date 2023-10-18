import prettytable
from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ["Character", "Trait"]
table.add_row(["Harry Potter", "Cool"])

print(table)