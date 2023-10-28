# TwASAP - Twitter All newest Status Auto Push to Discord Channel Bot

自動推送推特所有最新狀態到Discord頻道機器人

Help you to push the newest status of people you want to follow on Twitter to a Discord channel.

## Description

As Twitter changed its API policy, most of the Twitter bots are dead or turn to paid service. This bot is a simple solution to push the newest status of a Twitter user to a Discord channel with GitHub Actions.

## Usage

1. Fork this repository.
2. Create a Discord Bot and get the token.
3. Create a Twitter app and get the consumer key, consumer secret, access token, and access token secret.
4. Add the above secrets to your repository's secrets. `DISCORD_BOT_TOKEN`, `TWITTER_CONSUMER_KEY`, `TWITTER_CONSUMER_SECRET`, `TWITTER_ACCESS_TOKEN`, `TWITTER_ACCESS_TOKEN_SECRET`.
5. Allow Workflow permissions to have access to read and write permissions for the repository.
6. Edit the `.github/workflows/main.yml` file to change the schedule time. Default is `*/30 * * *` which means run every 30 minutes. We recommend you that do not set the time less than default.
7. Edit the `id.csv` file to add the Twitter account you want to push and the Discord channel ID you want to push to (Remember to make your bot join the server). Then commit the changes.
8. Done.

## Features

* Scheduled run on GitHub Actions.
* Push the newest status of a Twitter user to a specific Discord channel.
* Support multiple Twitter users and Discord channels.

## License

[MIT](LICENSE)
