# TwASAP - Twitter All newest Status Auto Push to Discord Channel Bot

[![](https://img.shields.io/docker/v/jim137/twasap) ![](https://img.shields.io/docker/image-size/jim137/twasap) ![](https://img.shields.io/docker/pulls/jim137/twasap)](https://hub.docker.com/r/jim137/twasap) [![](https://img.shields.io/github/stars/jim137/twasap)](https://github.com/Jim137/TwASAP)

自動推送推特所有最新狀態到Discord頻道機器人

Help you to push the newest status of people you want to follow on Twitter to a Discord channel.

## Description

As Twitter changed its API policy, most of the Twitter bots are dead or turn to paid service. This bot is a simple solution to push the newest status of a Twitter user to a Discord channel with GitHub Actions or Docker.

## Usage

### From GitHub Actions

1. Fork this repository.
2. Create a Discord Bot and get the token.
3. Create a Twitter app and get the consumer key, consumer secret, access token, and access token secret.
4. Add the above secrets to your repository's secrets. `DISCORD_BOT_TOKEN`, `TWITTER_CONSUMER_KEY`, `TWITTER_CONSUMER_SECRET`, `TWITTER_ACCESS_TOKEN`, `TWITTER_ACCESS_TOKEN_SECRET`.
5. Allow Workflow permissions to have access to read and write permissions for the repository.
6. Edit the `.github/workflows/main.yml` file to change the schedule time. Default is `*/30 * * *` which means run every 30 minutes. We recommend you that do not set the time less than default.
7. Edit the `id.csv` file to add the Twitter account you want to push and the Discord channel ID you want to push to (Remember to make your bot join the server). Then commit the changes.
8. Done.

### From Docker Local Run

1. Create a Discord Bot and get the token.
2. Create a Twitter app and get the consumer key, consumer secret, access token, and access token secret.
3. Pull the image from Docker Hub.

    ```bash
    docker pull jim137/twasap
    ```
4. Run the image with the following startup script.

    ```bash
    docker run -e DISCORD_BOT_TOKEN=[Your DISCORD_BOT_TOKEN] \
    -e TWITTER_CONSUMER_KEY=[Your TWITTER_CONSUMER_KEY] \
    -e TWITTER_CONSUMER_SECRET=[Your TWITTER_CONSUMER_SECRET] \
    -e TWITTER_ACCESS_TOKEN_KEY=[Your TWITTER_ACCESS_TOKEN_KEY] \
    -e TWITTER_ACCESS_TOKEN_SECRET=[Your TWITTER_ACCESS_TOKEN_SECRET] \
    -e TWITTER_ID=[TWITTER_ID] \
    -e DISCORD_CHANNEL_ID=[DISCORD_CHANNEL_ID] \
    [(optional) -e TWITTER_ID1= -e DISCORD_CHANNEL_ID1= -e TWITTER_ID2= -e DISCORD_CHANNEL_ID2= \ ]
    jim137/twasap
    ```
5. Done. But if you want to re-start the container, you can use the following command.

    ```bash
    docker container ls -a # Get CONTAINER_ID
    docker start -a CONTAINER_ID # Start the container
    ```
6. If you want to run the container as scheduled, you can set up a cron job.
    
    ```bash
    crontab -e
    ```
    
    Then add the following line to the file.

    ```bash
    */30 * * * * docker container start CONTAINER_ID
    ```

    This will run the container every half an hour.

## Features

* Scheduled run on GitHub Actions.
* Push the newest status of a Twitter user to a specific Discord channel.
* Support multiple Twitter users and Discord channels.

## License

[MIT](LICENSE)
