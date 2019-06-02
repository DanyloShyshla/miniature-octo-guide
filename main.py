import re

# test = '212.73.193.250 - - [23/Mar/2009:09:00:23 +0100] "GET /popup.php?choix=2 HTTP/1.1" 200 1692 "http://www.facades.fr/exemples.php"'
with open("access.log.txt") as file:
    result = re.findall(r"21\d\.\d*\.\d*\.\d*.*\.php.*", file.read())
    for i in result:
        print(i)

