## Tools for Marketing update the ranking team

This tool is for the marketing to update the ranking data. What I do is write a script in the server to upload the data to website port. Than I write this tool to upload newest data and call the server script to update.

### Step 1 : Create ssh key to access the server
ssh-keygen -t rsa -b 4096 -C your_email@example.com
to create the private and public key. Transfer the public key to the mail so that I can authorized you to access the server. Please keep your private server key.

### Step 2 : Install Python Packages
In order to make the environment clean enough, you can run the code on python virtualenv.
paramiko: access to the remote server with ssh
scp: upload local file to the server through ssh port
cement: a default command line application framework

### Step 3 : Configuration
We need configure so as to set the files which are need to uploaded.

``` python
configuration = {
    'name_server' : "./mkt_name.txt",
    'ranking_40k' : "./mkt_40.txt"
}
```

### Contact me
If you have any problem please free contact me(alex.liu@netease-na.com)
