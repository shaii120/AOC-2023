def parse_parts(parts: str):
    parts = parts.splitlines()
    parsed = []

    for part in parts:
        # remove brackets
        part = part[1:-1]
        part = part.split(",")
        rates = {}
        parsed.append(rates)

        for rate in part:
            category, val = rate.split("=")
            rates[category] = int(val)

    return parsed


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


def is_accepted(part, workflow, curr_rule="in"):
    if curr_rule == "A":
        return True
    elif curr_rule == "R":
        return False

    rules = workflow[curr_rule]

    for rule in rules["rules"]:
        rate = rule["part"]

        if (rule["cond"] == "<" and part[rate] < rule["val"]) or (
            rule["cond"] == ">" and part[rate] > rule["val"]
        ):
            return is_accepted(part, workflow, rule["result"])
    return is_accepted(part, workflow, rules["default"])


def count_accepted_parts(parts, rules):
    total = 0

    for part in parts:
        if is_accepted(part, rules):
            total += sum(part.values())

    return total


def main():
    with open("input.txt", "r") as file:
        rules, parts = file.read().split("\n\n")
    parts = parse_parts(parts)
    rules = parse_rules(rules)

    print(count_accepted_parts(parts, rules))


if __name__ == "__main__":
    main()
