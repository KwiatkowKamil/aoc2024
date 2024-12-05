with open('input.txt') as f:
    rules, updates = f.read().split("\n\n")
    rule_list = [[int(x) for x in rule.split('|')] for rule in rules.split('\n')]
    update_list = [[int(x) for x in update.split(',')] for update in updates.split('\n')]

used_rules_per_update = []

for i, page_list in enumerate(update_list):
    used_rules_per_update.append([])
    for a, b in rule_list:
        if {a, b} <= set(page_list):
            used_rules_per_update[i].append([a, b])
result = [0, 0]
for i, rule in enumerate(used_rules_per_update):
    page_list = update_list[i]
    first_rules = [x[0] for x in rule]
    ordered_rules = list(reversed(sorted(set(first_rules), key=lambda x: first_rules.count(x))))
    result[ordered_rules != page_list[:-1]] += ordered_rules[(len(page_list)) // 2]

print(*result)
