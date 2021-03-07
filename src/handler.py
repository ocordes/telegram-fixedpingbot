import telegram
import socket
import sys
import os
import time

from dotenv import load_dotenv
load_dotenv()

# read the environment variables
TOKEN       = os.environ.get('TELEGRAM_TOKEN') or None
CHAT_ID     = os.environ.get('CHAT_ID') or None
SERVERS     = os.environ.get('SERVERS') or None
TIMEOUT     = os.environ.get('TIMEOUT') or 10         # default 10 seconds
CHECK_TIME  = os.environ.get('CHECK_TIME') or 300     # do a check every 300 seconds

# send a message to the telegram bot
#
# msg: message to send
def send_message(msg):
    bot = telegram.Bot(token=TOKEN)
    bot.sendMessage(chat_id=CHAT_ID, text=msg)


# check if the bot a configured
def check():
    if (TOKEN is None) or (CHAT_ID is None):
        return False
    return True


# check a server
#
# server: name or IP of the server
# port  : port number for the check
def check_server(server, port):
    try:
        socket.create_connection((server, port), timeout=TIMEOUT)
        return True
    except:
        return False



# main_aws entry point
#
# event: ??
# conext: ??
def main_aws(event, context):
    main()


# main routine
def main():
    # do only if the bot is configured
    if check():
        # do only if servers are specified
        if SERVERS:
            for i in SERVERS.split(','):
                # split in server:port
                s = i.split(':')
                if len(s) == 2:
                    server, port = s
                    if check_server(server, port) == False:
                        send_message(f'PORT-CHECK: Server {server} is not reachable on port {port}!')
                else:
                    print(f'Entry {i} is not matching server:port rule!')
        else:
            print('No servers are specified!')
            return False
    else:
        print('No telegram bot is specified!')
        return False

    return True


# run with from the command line
if __name__ == '__main__':
    looping = True
    try:  # waiting for keyboard interruption
        while looping:
            looping = main()
            if looping and (CHECK_TIME > 0):
                print('Wait for the next check ...')
                time.sleep(CHECK_TIME)
    except:
        pass
