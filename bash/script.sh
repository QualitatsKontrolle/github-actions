#!/usr/bin/bash -x

#sysinfo - script to produce an html file
# $title$number

# Constants
TITLE="system information"
RIGHT_NOW="$(date +"%x %r")"
TIMESTAMP="Updated on $RIGHT_NOW by $USER"

set -x
# Functions
system_info() {
	if [ "$(id -u)" != "0" ]; then
		echo "Superuser privilege required to run script" >&2
		exit 1
	else
		echo
	fi
}
show_uptime() {
	echo "<h2>System Uptime</h2>"
	echo "<pre>"
		uptime -p
	echo "</pre>"
}
drive_space() {
	echo "<h2>Filesystem space</h2>"
	echo "<pre>"
	df -hH
	echo "<pre>"
}
home_space() {
	if [ "$(id)" = "0" ]; then
		echo "<h2>Home dir space by user"
		echo "<pre>"
		echo "Bytes dir"
		cd
			sudo du -s /home/* | sort -nr
		echo "</pre>"
	fi
}
set +x

# main exec
cat << _EOF_
	<html>
	<head>
		<title>
		User: $USER
		</title>
	</head>

	<body>
	<h1>My $TITLE: $HOSTNAME</h1>
	<p>Updated on $(date +"%x %r %Z") by $USER</p>
	
	<h2>$(system_info)</h2>
	<h2>$(show_uptime)</h2>
	<h2>$(drive_space)</h2>
	<h2>$(home_space)</h2>
	</body>
	</html>
_EOF_