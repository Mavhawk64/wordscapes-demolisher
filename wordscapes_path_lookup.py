import re


def build_level_path_map(raw_text):
    lines = raw_text.strip().split("\n")
    path_map = {}

    groups = []
    stages = []

    for i in range(0, len(lines), 2):
        name = lines[i].strip()
        range_line = lines[i + 1].strip()
        match = re.search(r"(?:Levels|Lvl) (\d+)-(\d+)", range_line)
        if not match:
            continue

        start, end = int(match.group(1)), int(match.group(2))

        # Save all ranges for now
        entry = (name, start, end)
        if not groups or start < groups[-1][1] or end > groups[-1][2]:
            groups.append(entry)
        else:
            stages.append(entry)

    # Handle edge case: some entries like 'master' cover up to level 100000
    groups.sort(key=lambda x: x[1])  # sort by start level
    stages.sort(key=lambda x: x[1])

    # Build level -> path map
    for stage_name, s_start, s_end in stages:
        for lvl in range(s_start, s_end + 1):
            group_name = next(
                (
                    g
                    for g, g_start, g_end in reversed(groups)
                    if g_start <= lvl <= g_end
                ),
                None,
            )
            if group_name:
                encoded_stage = stage_name.replace(" ", "%20")
                encoded_group = group_name.replace(" ", "%20")
                path_map[lvl] = f"/{encoded_group}/{encoded_stage}/{lvl}"

    return path_map


def get_path_from_path_map(level_number, path_map):
    return path_map.get(level_number, f"Level {level_number} not found")


def get_path(level_number):
    with open("wordscapes_levels.txt", "r") as file:
        raw_data = file.read()
    level_paths = build_level_path_map(raw_data)
    return get_path_from_path_map(level_number, level_paths)


if __name__ == "__main__":
    # Try a few example levels
    for test_level in [80, 6000, 100000]:
        print(f"Level {test_level} => {get_path(test_level)}")
