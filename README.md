#Budgie 420 Stats
I know there exists some applets do display stats like CPU, but they all didnt work for me. 
You can only display CPU and RAM at the time, but i will expand the functionality soon.

##Installation
I use Solus 1.2.0.5, so i dont know how to install it on other systems. [Here](https://docs.google.com/spreadsheets/d/1DphSjZA4lK0tGNCOp9AWNwHPayvu31VXABXTrI9Ic08/edit#gid=0) is a list of other applets, maybe it can help you.

###Solus:
```
sudo eopkg install python-psutil git curl
mkdir -p ~/.local/share/budgie-desktop/modules
cd ~/.local/share/budgie-desktop/modules
git clone https://github.com/v1nc/budgie-420stats.git
nohup budgie-panel --replace >/dev/null & 
```
Close the terminal and add the applet to your desktop.
