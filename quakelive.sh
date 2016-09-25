#!/bin/bash
# script for cron to reboot the server
#navigate to baseq3 directory
cd /home/steam/Steam/steamapps/common/Quake\ Live\ Dedicated\ Server/baseq3/

#timestamp the log and check how long the server has been up for
echo "****************************************************" >> cron.log
echo "Sytstem Timestamp" $(date) >> cron.log
echo "Total server uptime" $(ps -eo cmd,etime |grep qzeroded.x64 |awk '{print $2}') >> cron.log

#kill the server & screen
screen -X -S quakelive quit

# wait 10 seconds
sleep 10

#navigate to the qlds directory
cd ..

#reboot the server and update the log
echo "Starting quake server!" $(date) >> baseq3/cron.log
screen -dmS quakelive bash -c "./run_server_x64_minqlx.sh; exec bash"
