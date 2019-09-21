# install MySQL in Ubuntu

download APT repository
https://dev.mysql.com/downloads/mysql/5.7.html#downloads

install .deb package with 
```bash
sudo dpkg -i .deb
```
then use

sudo apt-get install mysql-server

# install python library
mysqlclient==1.3.13
https://stackoverflow.com/questions/7475223/mysql-config-not-found-when-installing-mysqldb-python-interface

fix with
sudo apt-get install libmysqlclient-dev

# PyAudio install
https://gist.github.com/diegopacheco/d5d4507988eff995da297344751b095e
sudo apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0
sudo apt-get install ffmpeg

then install with python

# In case use virtualenv
sudo apt-get install python3-tk