import json
from pathlib import Path

import requests

data_folder = Path("data")
yougov_folder = data_folder / "raw" / "yougov"

slug_template = "https://yougov.co.uk/_pubapis/v5/uk/trackers/{slug}/download/"


def download():

    with open(data_folder / "raw" / "yougov_industries.json", "r") as f:
        data = json.load(f)

    for slug in data:
        url = slug_template.format(slug=slug)
        print(f"Downloading {slug} from {url}")
        r = requests.get(url)
        with open(yougov_folder / f"{slug}.xlsx", "wb") as f:
            f.write(r.content)


if __name__ == "__main__":
    download()
