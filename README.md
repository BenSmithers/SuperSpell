# SuperSpell

## Linux Distros

To run this, you need pyqt5: 

`sudo apt-get install python3-pyqt5`

or 

`sudo apt-get install python-pyqt5`

If you're using Windows or Mac, eeeeh you're on your own. 


To run, call `python3 main_window`. 


## Installing on MacOS

### Downloading the Source
The first step is to just download the source code! 
Navigate to the release page, https://github.com/BenSmithers/SuperSpell/releases and download the latest `Source code (zip)` folder you see. 
Once done, go to your local downloads folder and unzip the "SuperSpell-1.##.zip" folder that was just added.

### Prepping Python
The rest of the process requires the usage of the Terminal application. 
To launch it, open the Utilities folder in Applications, and double click on Terminal. 
You should see a plain black box. 

The next step is to use the terminal to verify that "python" is installed. 
In the terminal, type 
```
python --version
```
and hit enter.
You should see a message similar to "Python 2.7.6" or "Python 3.6.9", though the exact numbers may vary.
If you see a message like "Command 'python' not found," Python may not be installed: in that case type
```
brew install python
```
in the Terminal and hit enter.

Next, we'll use the python service `pip` to install the packages used by SuperSpell. 
The problem is `pip` doesn't come pre-installed. 
But, this is easy enough to fix.
Type 
```
sudo easy_install pip
``` 
in the Terminal and hit enter.
It will probably ask for your password; that's okay.
It just needs to install some system pacakges, and for that it needs your permission. 

### Python Modules
Now, with `pip` installed, we can install the packages! 
You will need to enter the following lines, one at at a time.
```
pip install --user PyQt5
pip install --user numpy
pip install --user httplib2
```
Once the last is done, congratulations!
You're almost done. 

### Running SuperSpell
In the terminal, type `clear` and hit enter. 
Then, type `ls` and hit enter. 
The terminal will provide a list of files and folders; all of them are in your "Home" directory.
You should see folders for your Desktop, Documents, Downloads, and more. 

We need to enter your Downloads folder, and to do so we'll use the change directory, or `cd`, command.
Type 
```
cd Downloads
``` 
and hit enter, then type 
`ls` and hit enter.
You should see a list of the files and folders in your Downloads directory. 
From here, we can `cd` into the SuperSpell directory you downloaded and extracted earlier. 

Type 
```
cd SuperSpell-1.##
```
where the ## corresponds to the version number you downloaded, and hit enter. 
At the time of writing, it would be `1a`. 
Type `ls` and hit enter. 
You should several files, one of which named `main_window.py`. 
If instead you see a single entry `SuperSpell-1.##`, again type `cd SuperSpell-1.##` and hit enter. 
After entering `ls` again, you should see several files. 
Among them would be the file `main_window.py`

Now you're ready to launch!
From here in the terminal, type 
```
python main_window.py
```
and hit enter. 
SuperSpell should launch - note that the first time it is launched it may take a minute or two to download all the spells. 
Be patient! 

In the future, you only need to repeat the "Running SuperSpell" section to launch SuperSpell. 

If you run into an issue anywhere along these steps, feel free to contact me here, my email, or however else you know how to contact me. 
