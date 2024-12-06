from collections import defaultdict


def get_rules(rules: str) -> defaultdict[int, list[int]]:
    rules_: defaultdict[int, list[int]] = defaultdict(list)
    
    pair_rules = rules.strip().split("\n")
    for rule in pair_rules:
        a, b = map(int, rule.split("|"))
        rules_[a].append(b)

    return rules_


def get_updates(updates: str) -> list[list[int]]:
    return list(map(lambda l: list(map(int, l)), (map(lambda s: s.split(","), updates.strip().split("\n")))))


def check_page_ordering(data: str) -> int:
    rules_str, updates_str = data.split("\n\n")
    rules = get_rules(rules_str)
    updates = get_updates(updates_str)
    result = 0

    for update in updates:
        is_ordered = True

        for i in range(len(update)):
            n_rule = rules[update[i]]

            for j in range(len(update)):
                if not n_rule:
                    break

                if (update[j] in n_rule) and j < i:
                    is_ordered = False
                    break
            
            if not is_ordered:
                break
        
        if is_ordered:
            result += update[len(update) // 2]
    return result


def fix_page_ordering(data: str) -> int:
    rules_str, updates_str = data.split("\n\n")
    rules = get_rules(rules_str)
    updates = get_updates(updates_str)
    result = 0
    fixed_updates: list[list[int]] = []

    for update in updates:
        is_ordered = True

        for i in range(len(update)):
            n_rule = rules[update[i]]

            for j in range(len(update)):
                if not n_rule:
                    break

                if (update[j] in n_rule) and j < i:
                    is_ordered = False
                    temp = update[i]
                    update[i] = update[j]
                    update[j] = temp

        if not is_ordered:
            fixed_updates.append(update)


    for update in fixed_updates:
        result += update[len(update) // 2]

    return result
