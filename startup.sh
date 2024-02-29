#!/bin/bash
gnome-terminal -- bash -c "cd api && python app.py; exec bash" &
gnome-terminal -- bash -c "cd front && ng serve -o; exec bash" &
