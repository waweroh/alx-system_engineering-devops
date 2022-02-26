#!/usr/bin/env bash
# This script creates a file containing its PID, displays a string indefinitely
# It also displays a string when a SIGINT and SIGTERM signal are received

file=/var/run/holbertonscript.pid
	   echo $$ >> $file

	   trap 'echo I hate the kill command; sudo rm $file; exit' SIGTERM
	   trap 'echo Y U no love me?!' SIGINT
	   trap 'sudo rm $file; exit' SIGQUIT

	   while ((1)); do
				    echo "To infinity and beyond"
					        sleep 2
					    done
