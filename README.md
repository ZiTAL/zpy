zpy
===

zpy simple framework using python's web.py

requirements:
```
pip install flup
pip install Jinja2
pip install web.py
```

archlinux users
if you have both version of python installed (2.x and 3.x) use pip for python2:
```
pip2 install flup
pip2 install Jinja2
pip2 install web.py
```

sessions in sqlite3:
```
aptitude install sqlite3
sqlite3 private/config/session.db
```
create sessions table in sqlite file:

```
create table sessions (
   session_id char(128) UNIQUE NOT NULL,
   atime timestamp NOT NULL default current_timestamp,
   data text
);
```
WARNING: does not work with sqlite2

running
=======
```
cd /home/projects/zpy/private
python2 zpy.py
```

LICENSE
=======
AGPL