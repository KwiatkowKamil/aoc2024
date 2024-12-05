with open('input.txt') as f:
    rules, updates = f.read().split("\n\n")
    rule_list = [[int(x) for x in rule.split('|')] for rule in rules.split('\n')]
    update_list = [[int(x) for x in update.split(',')] for update in updates.split('\n')]

result = [0, 0]
for i, page_list in enumerate(update_list):
    matching_rules = [[a, b] for a, b in rule_list if {a, b} <= set(page_list)]
    page_list = update_list[i]
    first_rules = [x[0] for x in matching_rules]
    ordered_rules = list(reversed(sorted(set(first_rules), key=lambda x: first_rules.count(x))))
    result[ordered_rules != page_list[:-1]] += ordered_rules[(len(page_list)) // 2]

print(*result)
