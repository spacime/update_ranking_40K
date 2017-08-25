#Read Me

### Intruduction
This script is used to connect to the server and run the scritp so as to change the configuration and restart the server. In this case the designer can operate at his working enviroment and restart his server by himself.

This script is run on python 2.7 at Debain 8

### Required Package
When you come up with the Traceback you need to install execstack and run the following command
"ImportError: /usr/local/lib/python2.7/dist-packages/cryptography/hazmat/bindings/_openssl.so: cannot enable executable stack as shared object requires: Invalid argument"

```
sudo apt-get install execstack
execstack -c /usr/local/lib/python2.7/dist-packages/cryptography/hazmat/bindings/_openssl.so
```

### How to run

python testssh.py

### When you have any problem please free to connect Alex Liu(alex.liu@netease-na.com)