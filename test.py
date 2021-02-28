import webbrowser as web
import sys
import pyperclip
if len(sys.argv) > 1:
    address=' '.join(sys.argv[1:])
else:
    address= pyperclip.paste()
web.open('https://www.google.pl/maps/place/' + address )