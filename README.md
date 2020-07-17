# Covid19-app-tkitner
## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [py to exe](#py-to-exe)
* [License](#license)

## General info
A simple python GUI showing the live Covid-19 cases and deaths of selected countries.

![Screenshot (20)](https://user-images.githubusercontent.com/67178624/87791427-d6d5b700-c85f-11ea-9d03-6e308fdab6d3.png)

![Screenshot (21)](https://user-images.githubusercontent.com/67178624/87791432-d806e400-c85f-11ea-8cdd-3ee4e19f84cb.png)
## Technologies
Project is created with:
* Python version: 3.8.3
* Tkinter version: 8.5
* requests package version: 2.24.0
* win10toast library version: 0.9
	
## Setup
### To run this project,
#### Install Tkinter
```
pip install tkinter
```
#### Install requests package
```
pip install requests
```
* Click [here](https://pypi.org/project/requests/) for more details about requests.
#### Install win10toast library
```
pip install win10toast
```
* Click [here](https://pypi.org/project/win10toast/) for more details about win10toast
## Customization
### Customize the App according to your desire.
* Change the notification time. Currently set to 1 minute.
* Add various field to the notification toast.
## .py to .exe
### Convert .py file to .exe file
#### Install the pyinstaller module
* ```pip install pyinstaller```
#### Instructions
* Open your cmd and change your directory to the .py file.
* Choose an Icon. Icon must be in .ico format.
* Type ```pyinstaller -w -F -i (Your icon directory with file name) (filename.py)``` and hit enter.
* Open the directory and go to Dist folder where you can find the App.

## License
* MIT licensed. See the [License](LICENSE) file for full details. 
