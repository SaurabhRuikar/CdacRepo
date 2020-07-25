#!/bin/bash

sudo git init
sudo git add .
sudo git commit -m "commit"
sudo git config --global user.email ""
sudo git config --global user.name ""

sudo git remote add origin https://github.com/SaurabhRuikar/CdacRepo.git
sudo git push origin master
