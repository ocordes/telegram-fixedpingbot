# telegram-fixedpingbot
A telegram bot which pings computers and if fails send a message to telegram.

Unfortunately AWS lambda is not supporting ICMP packets, so the check is done
via TCP healthy checks. 

You can use this package via:

git clone https://github.com/ocordes/telegram-fixedpingbot.git
cd telegram-fixedpingbot
python src/handler.py

The parameters can be set via environment variables or via .env:

```
TELEGRAM_TOKEN=<token id from your bot>
CHAT_ID=<ID from a group or private chat>
SERVERS=<CSV list: server:port[,server2:port2] ...>
TIMEOUT=<timeout of the connection check in seconds, default: 10 seconds>
CHECK_TIME=<delay between two checks if tunning from the command line, default: 300 seconds>
```

Have fun!

