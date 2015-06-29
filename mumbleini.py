import time
import datetime
import os

filenameini = "C:\\Program Files (x86)\\Mumble\\murmur_OTE_oneg.ini"
filenamemotd = "C:\\Program Files (x86)\\Mumble\\mumble_motd.html"
filenamenew = "C:\\Program Files (x86)\\Mumble\\murmur_OTE.ini"

def quote():
    import urllib.parse
    import urllib.request
    import re

    url = 'http://www.brainyquote.com/quotes_of_the_day.html'
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    values = {'name' : 'Michael Foord',
              'location' : 'Northampton',
              'language' : 'English' }
    headers = { 'User-Agent' : user_agent }

    data  = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data, headers)
    with urllib.request.urlopen(req) as response:
       the_page = str(response.read())


    match = re.search(r'<a title="view image" href=".*?" .*? alt="(.*?)"><\/a>', the_page)

    return match.group(1)

def main():
    # The defualt ini for the server in string form
    f = open(filenameini, 'r')
    inifile = f.read()
    f.close()
    
    f = open(filenamemotd, 'r')
    motd = f.read()
    f.close()
    
    # Get date info
    partnow = time.strftime("%A, %B the ")
    nowdaynum = time.strftime("%d")

    if int(nowdaynum) < 10:
        nowdaynum = nowdaynum[1:]
    if int(nowdaynum[-1:]) < 4 and int(nowdaynum[:-1]) is not 1:
        if int(nowdaynum[-1:]) == 3:
            nowdaynum = nowdaynum + 'rd'
        elif int(nowdaynum[-1:]) == 2:
            nowdaynum = nowdaynum + 'nd'
        else:
            nowdaynum = nowdaynum + 'st'
    else:
        nowdaynum = nowdaynum + 'th'
    # make date line - Weekday, Mounthe the day-th. -
    date = partnow + nowdaynum + '.'
	
    motd = motd.replace('$$DATE$$', date)
    motd = motd.replace('$$QUOTE$$', quote())
    inifile = inifile.replace('$$MOTD$$', '\n' + motd)
    
    newinifile = open(filenamenew, 'w')
    newinifile.write(inifile)
    newinifile.close()

if __name__ == "__main__":
    main()
