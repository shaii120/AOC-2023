import math
import copy


def parse_rules(workflow: str):
    workflow = workflow.splitlines()
    workflow_parsed = {}

    for rules in workflow:
        name, rules_set = rules.split("{")
        # remove colsing bracket
        rules_set = rules_set[:-1]
        rules_set = rules_set.split(",")
        rules_parsed = {}
        workflow_parsed[name] = rules_parsed
        rules_list = []
        rules_parsed["rules"] = rules_list
        rules_parsed["default"] = rules_set.pop()

        for rule in rules_set:
            rule_dict = {}
            rule_dict["part"] = rule[0]
            rule_dict["cond"] = rule[1]
            rule_dict["val"], rule_dict["result"] = rule[2:].split(":")
            rule_dict["val"] = int(rule_dict["val"])
            rules_list.append(rule_dict)

    return workflow_parsed


def divide_part(part, rule):
    part_before = copy.deepcopy(part)
    part_after = copy.deepcopy(part)

    rate = rule["part"]
    start = part[rate].start
    stop = part[rate].stop
    divide_spot = rule["val"]

    if rule["cond"] == ">":
        divide_spot += 1

    rate_before = range(start, divide_spot)
    rate_after = range(divide_spot, stop)

    part_before[rate] = rate_before
    part_after[rate] = rate_after

    return part_before, part_after


def calc_accepted(part, workflow, curr_rule="in"):
    if curr_rule == "A":
        return math.prod([len(rate) for rate in part.values()])
    elif curr_rule == "R":
        return 0

    total = 0

    rules = workflow[curr_rule]

    for rule in rules["rules"]:
        rate = rule["part"]

        part_before, part_after = divide_part(part, rule)
        if rule["cond"] == "<":
            total += calc_accepted(part_before, workflow, rule["result"])
            part = part_after
        elif rule["cond"] == ">":
            total += calc_accepted(part_after, workflow, rule["result"])
            part = part_before
        if not part[rate]:
            return total
    return total + calc_accepted(part, workflow, rules["default"])


def main():
    with open("input.txt", "r") as file:
        rules, _ = file.read().split("\n\n")
    parts = {
        "x": range(1, 4001),
        "m": range(1, 4001),
        "a": range(1, 4001),
        "s": range(1, 4001),
    }
    rules = parse_rules(rules)

    print(calc_accepted(parts, rules))


if __name__ == "__main__":
    main()
