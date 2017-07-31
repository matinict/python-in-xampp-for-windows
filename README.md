# python-in-xampp-for-windows:

Run python in xampp for windows
18.09.12, 01:45
The setup takes nearly 2 min.

Assuming that you have already installed xammp in your windows PC, 
You can follow the below steps to run python in your localhost

STEP 1:

Download & install the latest version of python from here Download Python click on the windows installer of any version

STEP 2:

Install in any directory of your harddrive

STEP 3:

Open the directory where xammp was installed
Go to apache >> conf

You'll see a file named httpd.conf
Open it in any text editor & put the below codes in the end of that file

Code:
AddHandler cgi-script .py
ScriptInterpreterSource Registry-Strict
The next step is optional

STEP 4:
In same file search for <IfModule dir_module>
When you've found it put index.py in the end
It will look something like this
Code:
<IfModule dir_module>
    DirectoryIndex index.php index.pl index.cgi index.asp index.shtml index.html index.htm \
                   default.php default.pl default.cgi default.asp default.shtml default.html default.htm \
                   home.php home.pl home.cgi home.asp home.shtml home.html home.htm index.py
</IfModule>
STEP 5:
That's all for editing, now restart apache from your xampp control panel

STEP 6:

Open a text editor & test python now

But wait at the beginning of your script you need to specify the path where you've installed python

In my case its C:/python27/python.exe
In your case it may be different, depending up on the version you've installed python & the directory of your hard drive

PHP Code:
#!D:/Python27/python.exe 
print "Content-Type: text/html\n" 
print "This is cool"  
save the file as test.py in htdocs & open http://localhost/test.py
If everything goes well, You'll see the text This is cool

Now, who the hell is gonna install python just to see the stupid text "This is cool" ?!

Here's the code to grab a web page w/ python 

PHP Code:
#!C:/Python27/python.exe 
print "Content-Type: text/html\n" 
import urllib2 
response = urllib2.urlopen('http://python.org/') 
html = response.read() 
print html  
LOL

-------------------



Ref#
http://coding-talk.com/forum/main-forums/coding-forum/13986-run-python-in-xampp-for-windows
