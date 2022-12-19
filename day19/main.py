from collections import deque


def nextState(
    state,
    costOre,
    costClay,
    costObsidianOre,
    costObsidianClay,
    costGeodeOre,
    costGeodeClay,
):
    ore, cly, obs, geo, p1, p2, p3, p4, time = state
    next_states = []

    # add production to resources
    next_states.append(
        (ore + p1, cly + p2, obs + p3, geo + p4, p1, p2, p3, p4, time - 1)
    )

    # resources are used to buy
    if ore >= costOre:
        next_states.append(
            (
                ore - costOre + p1,
                cly + p2,
                obs + p3,
                geo + p4,
                p1 + 1,
                p2,
                p3,
                p4,
                time - 1,
            )
        )
    if ore >= costClay:
        next_states.append(
            (
                ore - costClay + p1,
                cly + p2,
                obs + p3,
                geo + p4,
                p1,
                p2 + 1,
                p3,
                p4,
                time - 1,
            )
        )
    if ore >= costObsidianOre and cly >= costObsidianClay:
        next_states.append(
            (
                ore - costObsidianOre + p1,
                cly - costObsidianClay + p2,
                obs + p3,
                geo + p4,
                p1,
                p2,
                p3 + 1,
                p4,
                time - 1,
            )
        )
    if ore >= costGeodeOre and obs >= costGeodeClay:
        next_states.append(
            (
                ore - costGeodeOre + p1,
                cly + p2,
                obs - costGeodeClay + p3,
                geo + p4,
                p1,
                p2,
                p3,
                p4 + 1,
                time - 1,
            )
        )

    return next_states


def solve(
    costOre,
    costClay,
    costObsidianOre,
    costObsidianClay,
    costGeodeOre,
    costGeodeClay,
    time,
):
    best = 0
    state = (0, 0, 0, 0, 1, 0, 0, 0, time)
    queue = deque([state])
    visited = set()
    while queue:
        state = queue.popleft()
        ore, cly, obs, geo, prod1, prod2, prod3, prod4, t = state

        best = max(best, geo)
        if t == 0:
            continue

        # Set the production rate of each resource to the cost of the most expensive resource that can be obtained with that resource
        max_ore_cost = max([costOre, costClay, costObsidianOre, costGeodeOre])
        prod1 = min(prod1, max_ore_cost)
        prod2 = min(prod2, costObsidianClay)
        prod3 = min(prod3, costGeodeClay)

        # Set the number of each resource to the maximum number that can be obtained in the remaining time, given the current production rate
        ore = min(ore, t * max_ore_cost - prod1 * (t - 1))
        cly = min(cly, t * costObsidianClay - prod2 * (t - 1))
        obs = min(obs, t * costGeodeClay - prod3 * (t - 1))

        state = (ore, cly, obs, geo, prod1, prod2, prod3, prod4, t)

        if state in visited:
            continue
        visited.add(state)

        next_states = nextState(
            state,
            costOre,
            costClay,
            costObsidianOre,
            costObsidianClay,
            costGeodeOre,
            costGeodeClay,
        )
        for next_state in next_states:
            queue.append(next_state)

    return best


def parseBlueprint(lines):
    costs = {}
    for line in lines:
        words = line.split()
        item_id = int(words[1][:-1])
        ore_cost = int(words[6])
        clay_cost = int(words[12])
        obsidian_ore_cost = int(words[18])
        obsidian_clay_cost = int(words[21])
        geode_ore_cost = int(words[27])
        geode_clay_cost = int(words[30])
        costs[item_id] = {
            "id": item_id,
            "ore": ore_cost,
            "clay": clay_cost,
            "obsidian_ore": obsidian_ore_cost,
            "obsidian_clay": obsidian_clay_cost,
            "geode_ore": geode_ore_cost,
            "geode_clay": geode_clay_cost,
        }
    return costs


def main(inp):
    result1 = 0
    result2 = 1
    cost = parseBlueprint(inp)
    for id, cost in cost.items():
        s1 = solve(
            cost["ore"],
            cost["clay"],
            cost["obsidian_ore"],
            cost["obsidian_clay"],
            cost["geode_ore"],
            cost["geode_clay"],
            time=24,
        )
        result1 += id * s1
        if id <= 3:
            s2 = solve(
                cost["ore"],
                cost["clay"],
                cost["obsidian_ore"],
                cost["obsidian_clay"],
                cost["geode_ore"],
                cost["geode_clay"],
                time=32,
            )
            result2 *= s2
    print("Result 1: ", result1)
    print("Result 2: ", result2)


if __name__ == "__main__":
    with open("day19/input.txt", "r", encoding="utf-8") as f:
        inp = f.read().splitlines()
    main(inp)
