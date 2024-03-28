# git-hooks auto-ufw-mod
Simple script for add Git-hub hooks-API IP-address  to UFW
## Usage
Download script and add in crontab
```bash
wget -O /usr/local/bin/git-hooks.py https://raw.githubusercontent.com/FarSetV/git-hooks/master/git-hooks.py
echo "0 2 * * * /usr/bin/python3 /usr/local/bin/git-hooks.py" | crontab -
```
