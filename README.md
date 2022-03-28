## Automated Attendance SI-AKAD SMK Telkom Malang

[SIAKAD SMK TELKOM MALANG](https://siswa.smktelkom-mlg.sch.id)

Automatic scripts attendance for SMK Telkom Malang, since the pandemic the students attendance are through siAkad, and these scripts will attendance the student automatically without login to siAkad.

### Installation

1. Clone these scripts to your machine
  
  ![image1](https://github.com/lleans/auto-absen-siakad/blob/master/image/image1.png?raw=true)

2. Create apps in heroku, tutorial [here](https://youtu.be/rfdNIOYGYVI)

3. Do not change the procfile file, otherwise these scripts will not run

4. Change values.py with  your Email Si-Akad and Password  

![image2](https://github.com/lleans/auto-absen-siakad/blob/master/image/image2.png?raw=true)

5. Push these scripts to heroku apps, same tutorial with steps 2

6. After that go to heroku Resources tab, and edit worker python main.py, and turn it on

![image3](https://github.com/lleans/auto-absen-siakad/blob/master/image/1.gif?raw=true)

7. Enjoy the scripts

### Note: these scripts will not run in Saturday and Monday, these scripst couldn't detect National Holiday so you still absent in that day, if you want turn off this scripts just do steps 6 and change to turn off
