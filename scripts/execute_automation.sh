#!/bin/bash
pip3 install selenium
apt-get install -y xvfb
xvfb-run python3 ./src/test_script.py

