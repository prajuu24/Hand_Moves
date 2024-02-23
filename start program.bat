@echo off
setlocal

:: Retrieve the current user's home directory
set "user_home=%USERPROFILE%"

:: Specify the path where you want to clone the repository
set "clone_dir=%user_home%\"

:: Specify the full path to the Gesture-Controlled-Virtual-Mouse folder
set "src_dir=%clone_dir%Gesture-Controlled-Virtual-Mouse\src"

:: Step 1: Clone the repository
git clone https://github.com/xenon-19/Gesture-Controlled-Virtual-Mouse.git "%clone_dir%"

:: Step 2: Change directory to the src folder
cd /d "%src_dir%"

:: Step 3: Create and activate a conda environment
conda create --name gest python=3.8.5
conda activate gest

:: Step 4: Install Python dependencies
pip install -r requirements.txt

:: Step 5: Install additional conda packages
conda install PyAudio
conda install pywin32

:: Step 6: Run Gesture_Controller.py
python Gesture_Controller.py

:: End of script
echo "Script execution complete."
pause
