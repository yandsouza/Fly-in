from typing import Any


def parse_map(path: str) -> Any:
    config: dict[str, str] = {}

    with open(path, "r", encoding="utf-8") as file:
        con_i = 0
        hub_i = 0
        for i, raw_line in enumerate(file, start=1):
            line = raw_line.strip()

            if not line or line.startswith("#"):
                continue

            key, value = line.split(":", maxsplit=1)
            if key == "connection":
                config["connection" + str(con_i)] = value.strip()
                con_i += 1
            elif key == "hub":
                config["hub" + str(hub_i)] = value.strip()
                hub_i += 1
            else:
                config[key.strip()] = value.strip()

    return config
