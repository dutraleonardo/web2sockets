# web2sockets
A simple approach to how to create a chat with Web2py + Tornado + JQuery

## Features
* Real-time chat

## TODOs
* Improve the interface
* Migrate to AngularJS

## Install
1. Download web2py: [http://web2py.com](http://web2py.com)
2. Clone this repository inside web2py applications folder: `git clone https://github.com/dutraleonardo/web2sockets.git
3. Install Tornado: 
  ```
  pip install tornado
  ```
## How to run:
Terminal:
- cd web2py
- python web2py.py -a "yourpassword"
In another terminal window:
- python gluon/contrib/websocket_messaging.py -k mykey -p 8888 (Will not show any messages after run this script)
Browser:
- http://localhost:8000/web2sockets/default/index
  
### Contribute!
Copyright (c) 2017 Leonardo Dutra & licensed under GNU General Public License v3.0
