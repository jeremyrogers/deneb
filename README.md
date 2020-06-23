# deneb Discord Bot

This is just a simple discord bot to display counts and lists of users based on discord roles

## Usage

Create env file with these entries:

```
DISCORD_TOKEN=<your bot token>
DISCORD_SERVER=<server ID>
DISCORD_CHANNEL=<name of the channel to watch>
```

With docker:
```
docker build . --tag deneb:latest
docker run --env-file /path/to/your/env-file.env deneb:latest
```

Or docker-compose:
```
  deneb:
    image: deneb:latest
    container_name: deneb
    restart: unless-stopped
    env_file:
      - /path/to/your/env-file.env
```
