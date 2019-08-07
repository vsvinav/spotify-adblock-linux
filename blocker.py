import mpris2
import dbus
import os
import subprocess, signal, time
open_spotify = "setsid spotify &>/dev/null"
uri = dbus.String('org.mpris.MediaPlayer2.spotify')
player = mpris2.Player(dbus_interface_info={'dbus_uri': uri})
run_command = "ps -ef | grep \'spotify\' | grep -v grep | awk \'{print $2}\' | xargs -r kill -9"
while True:
    try:
        if str(dict(player.Metadata).get(dbus.String('xesam:title'))) == 'Advertisement':
            print('Initiating now')
            os.system(run_command)
            print('Killed Spotify')
            os.system(open_spotify)
            player.Next()
    except:
        time.sleep(3)
        uri = dbus.String('org.mpris.MediaPlayer2.spotify')
        player = mpris2.Player(dbus_interface_info={'dbus_uri': uri})
        player.Next()
        
    # else:
        # print("Currently Playing:" + str(dict(player.Metadata).get(dbus.String('xesam:title'))))
  

