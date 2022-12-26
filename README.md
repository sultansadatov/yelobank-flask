# yelo-project-eagle-1

_mysql is not defined error solve -> export DYLD_LIBRARY_PATH=/usr/local/mysql/lib/

Cannot start service db: Ports are not available: listen tcp 0.0.0.0:3306: bind: address already in use -> sudo kill `sudo lsof -t -i:3306`