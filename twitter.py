import os
import json

from twarc import Twarc

try:
    consumer_key = os.getenv("TWITTER_CONSUMER_KEY")
    consumer_secret = os.getenv("TWITTER_CONSUMER_SECRET")
    access_token_key = os.getenv("TWITTER_ACCESS_TOKEN_KEY")
    access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
except KeyError:
    print("Please set the environment variables for the Twitter API.")
    exit(1)


def get_status(users: list):
    client = Twarc(
        consumer_key,
        consumer_secret,
        access_token_key,
        access_token_secret,
    )
    lookup = client.user_lookup(users)
    for i, page in enumerate(lookup):
        try:
            with open(users[i] + ".json", "r") as f:
                old = json.load(f)
            if old["id"] == page["status"]["id"]:
                return None
        except FileNotFoundError:
            pass
        with open(users[i] + ".json", "w") as f:
            json.dump(page["status"], f)
    return page["status"]


if __name__ == "__main__":
    print(get_status())
