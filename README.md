  1 #!/bin/sh
  2
  3 ### BEGIN INIT INFO
  4 # Provides:          murmur
  5 # Required-Start:    $remote_fs
  6 # Required-Stop:     $remote_fs
  7 # Default-Start:     2 3 4 5
  8 # Default-Stop:      0 1 6
  9 # Short-Description: Murmur - Mumble Server
 10 # Description:       Starts a Murmur - Mumble Server
 11 ### END INIT INFO
 12
 13 PATH=/sbin:/bin:/usr/sbin:/usr/bin:/usr/local/sbin:/usr/local/bin
 14
 15 NAME="Murmur - Mumble Server"
 16 USER="murmur"
 17 SCREENREF="murmur"
 18 BINARYPATH="/opt/murmur-static_x86-1.2.9"
 19 BINARYNAME="murmur.x86"
 20 PIDFILE="murmur.pid"
 21
 22 OPTS="-fg -ini /opt/murmur-static_x86-1.2.9/murmur.ini"
 23
 24 cd "$BINARYPATH"
 25
 26 running() {
 27     if [ -n "`pgrep -f $BINARYNAME`" ]; then
 28         return 0
 29     else
 30         return 1
 31     fi
 32 }
 33
 34 start() {
 35     if ! running; then
 36         echo -n "Starting the $NAME server... "
 37         start-stop-daemon --start --chuid $USER --user $USER --chdir $BINARYPATH --exec "/usr/bin/screen" -- -dmS $SCREENREF $BINARYPATH/$BINARYNAME $OPTS
 38         sleep 3
 39         pgrep -f $BINARYNAME > $PIDFILE
 40         if [ -s $PIDFILE ]; then
 41             echo "Done"
 42         else
 43             echo "Failed"
 44             rm $PIDFILE
 45         fi
 46     else
 47         echo "The $NAME server is already started."
 48     fi
 49 }
 50
 51 stop() {
 52     if running; then
 53         echo -n "Stopping the $NAME server... "
 54         kill `cat $PIDFILE`
 55         while running; do
 56             sleep 1
 57         done
 58         rm $PIDFILE
 59         echo "Done"
 60     else
 61         echo "The $NAME server is already stopped."
 62     fi
 63 }
 64
 65 case "$1" in
 66     start)
 67         start
 68     ;;
 69     stop)
 70         stop
 71     ;;
 72     restart)
 73     stop
 74         start
 75     ;;
 76     status)
 77         if running; then
 78             echo "The $NAME server is started."
 79         else
 80             echo "The $NAME server is stopped."
 81         fi
 82     ;;
 83     *)
 84         echo "Usage: $0 (start|stop|restart|status)"
 85         exit 1
 86 esac
 87 exit 0
                           
