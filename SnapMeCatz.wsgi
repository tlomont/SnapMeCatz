import sys
import os
# Change working directory so relative paths (and template lookup) work again
os.chdir(os.path.dirname(__file__))
sys.path.append('/var/www/SnapMeCatz')

import bottle
# ... build or import your bottle application here ...
from bottle import get, post, request, run, default_app
from snapchat import Snapchat
import getpass
import urllib
import pickle


#urls = pickle.load( open('urls.p', 'rb'))

@get('/')
def login():
        return '''
                <html style= "background-color: #E7E7E7;">
                <head>
                <title> SnapMeCatz! </title>
                <link href="data:image/x-icon;base64,AAABAAEAEBAQAAEABAAoAQAAFgAAACgAAAAQAAAAIAAAAAEABAAAAAAAgAAAAAAAAAAAAAAAEAAAAAAAAAAAAAAA////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEQARABEAAAEQEAABARAAARAQAAEBEAAAEQAAABEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADwDwAAwAMAAIABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIABAACBgQAAwYMAAMPDAADDwwAA5+cAAOfnAADv9wAA" rel="icon" type="image/x-icon" />        
                <meta name="description" content="Snapchat pictures of cats to you or your friends with SnapMeCatz!">
                <style type="text/css">
                body{
                        font-family:  helvetica, "Tahoma";
                        font-weight: 100
                }
                A {color:black}
                A:visited {color: black}
                A:active {text-decoration: none}
                A:hover {text-decoration: underline; color: rgb(139, 188, 190);}
                </style>
                </head>
                <body>
                <div style="margin:20px auto; text-align:center; width:400px; height: 165px; border:2px solid; border-radius:20px; background-color: white">
                <h1 style="font-weight: 200"> SnapMeCatz!</h1>
                <p><form name="input" action="/" method="post">
                Snapchat Username: 
                <input type="text" name="username" style="border: 2px solid rgb(139, 188, 190); border-radius:5px"></p>
                <input type="submit" value="SnapCat!" style="
                padding: 5px 15px 5px !important; 
                font-size: 14px !important; 
                background-color: rgb(139, 188, 190); font-weight: bold; 
                text-shadow: 1px 1px rgb(139, 188, 190); color: #ffffff; 
                border-radius: 100px; -moz-border-radius: 100px; 
                -webkit-border-radius: 100px; 
                border: 1px solid rgb(139, 188, 190); 
                cursor: pointer; 
                box-shadow: 0 1px 0 rgba(255, 255, 255, 0.5) inset; -moz-box-shadow: 0 1px 0 rgba(255, 255, 255, 0.5) inset; 
                -webkit-box-shadow: 0 1px 0 rgba(255, 255, 255, 0.5) inset;
                font: -webkit-body;"></p>
                </form>
                </div>
                <p style="text-align:center; font-size: 14px; font-weight: 100"> Make sure to accept SnapMeCatz as a friend!</p>
                <p style="text-align:center; font-weight:100; font-size: 14px;"> <a href="/about"> About</a></p>
                <script>
                (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
                (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
                m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
                })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

                ga('create', 'UA-46815699-1', 'snapmecatz.com');
                ga('send', 'pageview');

                </script>                
                </body>
                </html>
                '''

@post('/')
def do_login():
        urls = pickle.load( open('urls.p', 'rb'))
        from random import choice
        url_final = choice(urls)
        while(".gif" in url_final):
                url_final = choice(urls)
        name = 'snapmecatz'
        password = 'fuckyoni'
        recipient = request.forms.get('username')
        urllib.urlretrieve(url_final, "1.jpg")
        pic = "1.jpg"
        s = Snapchat()
        s.login(name, password)

        #add username to file
        #f = open('username.txt','a')
        #f.write(recipient+'\n')

        # Send a snapchat
        media_id = s.upload(Snapchat.MEDIA_IMAGE, pic)
        s.send(media_id, recipient)

        return '''
                <html style=" background-color: #E7E7E7;" >
                <head>
                <title> SnapMeCatz! </title>
                <link href="data:image/x-icon;base64,AAABAAEAEBAQAAEABAAoAQAAFgAAACgAAAAQAAAAIAAAAAEABAAAAAAAgAAAAAAAAAAAAAAAEAAAAAAAAAAAAAAA////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEQARABEAAAEQEAABARAAARAQAAEBEAAAEQAAABEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADwDwAAwAMAAIABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIABAACBgQAAwYMAAMPDAADDwwAA5+cAAOfnAADv9wAA" rel="icon" type="image/x-icon" />
                <style type="text/css">
                body{
                        font-family:  helvetica, "Tahoma";
                        font-weight: 100;
                }
                A {color:black}
                A:visited {color: black}
                A:active {text-decoration: none}
                A:hover {text-decoration: underline; color: rgb(139, 188, 190);}
                </style>
                </head>
                <body>
                <div style="margin:20px auto; text-align:center; width:400px; height: 165px">
                <h1 style="font-weight: 200"> SnapCat sent!</h1>
                <div>
                <p style="font-weight:100"> <a href="../">Return Home</a></p>
                <script>
                (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
                (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
                m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
                })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

                ga('create', 'UA-46815699-1', 'snapmecatz.com');
                ga('send', 'pageview');

                </script>
                </body>
                </html>
                '''

@get('/about')
def about():
        return '''
                <html style=" background-color: #E7E7E7;" >
                <head>
                <title> SnapMeCatz! | About </title>
                <link href="data:image/x-icon;base64,AAABAAEAEBAQAAEABAAoAQAAFgAAACgAAAAQAAAAIAAAAAEABAAAAAAAgAAAAAAAAAAAAAAAEAAAAAAAAAAAAAAA////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEQARABEAAAEQEAABARAAARAQAAEBEAAAEQAAABEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADwDwAAwAMAAIABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIABAACBgQAAwYMAAMPDAADDwwAA5+cAAOfnAADv9wAA" rel="icon" type="image/x-icon" />
                <style type="text/css">
                body{
                        font-weight: 100;
                        font-family:  helvetica, "Tahoma"
                }
                A {color:black}
                A:visited {color: black}
                A:active {text-decoration: none}
                A:hover {text-decoration: underline; color: rgb(139, 188, 190);}
                </style>
                </head>
                <body>
                <div style="margin:20px auto; text-align:center; width:400px; height: 165px; border:2px solid; border-radius:20px; background-color: white">
                <h1 style="font-weight:200"> About </h1>
                <p> Send snapchats of random cats to you or your friends! </p>
                <p style="font-size: 12px; margin-top: 10px; font-weight:100"> Created by Ben Haines, Tommy Lomont, and Waleed Malik </P>

                </div>
                <p style= "text-align: center; font-weight: 100"> <a href="../">Return Home</a></p>

                <script>
                  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
                  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
                  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
                  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

                  ga('create', 'UA-46815699-1', 'snapmecatz.com');
                  ga('send', 'pageview');

                </script>
                </body>
                </html>

                '''

from bottle import error
@error(404)
def error404(error):
    return '''
	<html style= "background-color: #E7E7E7;">
<head>
<title> SnapMeCatz! | Uh-Oh! </title>
<link href="data:image/x-icon;base64,AAABAAEAEBAQAAEABAAoAQAAFgAAACgAAAAQAAAAIAAAAAEABAAAAAAAgAAAAAAAAAAAAAAAEAAAAAAAAAAAAAAA////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEQARABEAAAEQEAABARAAARAQAAEBEAAAEQAAABEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADwDwAAwAMAAIABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIABAACBgQAAwYMAAMPDAADDwwAA5+cAAOfnAADv9wAA" rel="icon" type="image/x-icon" />        
<meta name="description" content="Snapchat pictures of cats to you or your friends with SnapMeCatz!">
<style type="text/css">
body{
        font-family:  helvetica, "Tahoma";
        font-weight: 100;
        text-align: center;
}
A {color:black}
A:visited {color: black}
A:active {text-decoration: none}
A:hover {text-decoration: underline; color: rgb(139, 188, 190);}
</style>
</head>
<body>
<h1 style="font-weight:200"> Uh-oh! </h1>
<h3 style="font-weight:100"> Looks like you've got the wrong page </h3>
<img src="http://www.thepetproductguru.com/wp-content/uploads/2013/03/scared-cat.jpeg" height="300px">
<p style="text-align:center; font-weight:100; font-size: 18px;"> <a href="/"> Return Home</a></p>              
</body>
</html>
'''


# Do NOT use bottle.run() with mod_wsgi
application = bottle.default_app()
