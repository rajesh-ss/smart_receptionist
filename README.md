
# Project Title

Smart receptionist
## Acknowledgements

 - [Django-code](https://github.com/nikhil24min/mcarrapi-v01/tree/master)
 - [reference](https://github.com/opencv/opencv/)
 - [haar-classifier-download](https://github.com/opencv/opencv/tree/master/data/haarcascades)



## Authors

- [@nikhil24min](https://github.com/nikhil24min/)


- [@harshitha]()

## Installation

DJANGO on ec2 instance


sudo apt-get update
sudo apt-get install python3-pip apache2 libapache2-mod-wsgi-py3
sudo pip3 install virtualenv
mkdir myproject
cd myproject
virtualenv myprojectenv
git clone -b <branchname> "https://github.com/<username>/<repository name>.git"
source myprojectenv/bin/activate
cd badgerepo-v1
sudo nano badgeapp/settings.py
change ALLOWED_HOSTS = ["*","ec2 public DNS"]
pip install -r requirements.txt
if this doesnt work install each and one pacakeg one by one. best is install django first and then run migration command, it will tell which packages are missing and then install them quickly.
if everything works
sudo apt-get install libpq-dev
use the above command if problem installing psycopg2
python manage.py runserver 0.0.0.0:8000
Then copy the [ublic instance dns and paste in the browser like this
http://<ec2 public DNS >:8000/

deactivate
sudo nano  /etc/apache2/sites-available/000-default.conf
<VirtualHost *:80>
ServerAdmin webmaster@example.com
DocumentRoot /home/ubuntu/myproject/badgerepo-v1
ErrorLog ${APACHE_LOG_DIR}/error.log
CustomLog ${APACHE_LOG_DIR}/access.log combined
Alias /static /home/ubuntu/myproject/badgerepo-v1/static
<Directory /home/ubuntu/myproject/badgerepo-v1/static>
Require all granted
</Directory>
<Directory /home/ubuntu/myproject/badgerepo-v1/badgeapp>
<Files wsgi.py>
Require all granted
</Files>
</Directory>
WSGIDaemonProcess myproject python-path=/home/ubuntu/myproject/badgerepo-v1 python-home=/home/ubuntu/myproject/myprojectenv
WSGIProcessGroup myproject
WSGIScriptAlias / /home/ubuntu/myproject/badgerepo-v1/badgeapp/wsgi.py
</VirtualHost>

cd /home/ubuntu/django/myproject
chmod 664 db.sqlite3
sudo chown :www-data db.sqlite3
sudo chown :www-data ~/myproject
sudo chmod 755 /home/ubuntu

sudo service apache2 restart
    
## Screenshots

![App Screenshot](https://github.com/rajesh-ss/smart_receptionist/blob/main/screenshots-and-video/1.jpg)
![App Screenshot](https://github.com/rajesh-ss/smart_receptionist/blob/main/screenshots-and-video/2.jpg)
![App Screenshot](https://github.com/rajesh-ss/smart_receptionist/blob/main/screenshots-and-video/3.jpg)
![App Screenshot](https://github.com/rajesh-ss/smart_receptionist/blob/main/screenshots-and-video/4.jpg)
![App Screenshot](https://github.com/rajesh-ss/smart_receptionist/blob/main/screenshots-and-video/5.jpg)
![App Screenshot](https://github.com/rajesh-ss/smart_receptionist/blob/main/screenshots-and-video/6.png)
![App Screenshot](https://github.com/rajesh-ss/smart_receptionist/blob/main/screenshots-and-video/7.png)
![App Screenshot](https://github.com/rajesh-ss/smart_receptionist/blob/main/screenshots-and-video/8.jpg)
![App Screenshot](https://github.com/rajesh-ss/smart_receptionist/blob/main/screenshots-and-video/9.jpeg)
![video](https://github.com/rajesh-ss/smart_receptionist/blob/main/screenshots-and-video/video1.mp4)
