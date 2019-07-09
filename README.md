# nitjsr-notice
Since I am too lazy to open the institute's website to see the new notices so I created a script that does it for me.
First clone the project:
```bash
git clone https://github.com/piyush072/nitjsr-notice.git
```
now install the requirements by entering the following line
```bash
pip install -r requirements.txt
```
now open crontab 
```bash
crontab -e
```
Add the following line to the crontab
```bash
* * * * * cd /path/to/cloned/directory && /usr/local/bin/python3 notice.py #enter the path of the cloned project
```
Do edit the path in the notice.py file.
```python
my_path = '/home/username/Downloads/NITJSR_NOTICES' #add your own username
```

This will run the code every minute and checks for the new notice updated and will download the notice in the Downloads directory.

Since the notification function is not working with crontab(though it works if you directly run the notice.py file from the terminal), I will update it soon so that it will show the notifications whenever a new notice is published.
