with open('input.txt') as f:
    rules, updates = f.read().split("\n\n")
    rule_list = [[int(x) for x in rule.split('|')] for rule in rules.split('\n')]
    update_list = [[int(x) for x in update.split(',')] for update in updates.split('\n')]

result = [0, 0]
for page_list in update_list:
    matching_rules = [a for a, b in rule_list if {a, b} <= set(page_list)]
    ordered_rules = sorted(set(matching_rules), key=lambda x: matching_rules.count(x))[::-1]
    result[ordered_rules != page_list[:-1]] += ordered_rules[(len(page_list)) // 2]

print(*result)