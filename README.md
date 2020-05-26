## Requirements
- Python (3.x)
- Docker-CE (Not required for all search-engine, just few of them)

## How to install

- You need to install all requirements :
```shell-script
pip3 install -r requirements.txt
```
- Install geckodriver :
```shell-script
# For linux users

# cd /home/your-user-name
wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz
# Unzip the file
tar -xvzf geckodriver*
chmod +x geckodriver
# Add it to PATH
export PATH=$PATH:/path-to-extracted-file/.

# For other OS's users, please check releases on https://github.com/mozilla/geckodriver/releases
```
Put the geckodriver binary file in the root of this directory

## Author

- Sanix-darker
