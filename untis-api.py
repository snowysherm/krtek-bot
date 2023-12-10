import webuntis
import datetime

s = webuntis.Session(
    server='kephiso.webuntis.com',
    username='Fi22',
    password='BszWsw11#',
    school='bszwsw',
    useragent='WebUntis Test'
)

s.login()

# for klasse in s.klassen():
#     print(klasse.name)


today = datetime.date.today()
monday = today - datetime.timedelta(days=today.weekday())
friday = monday + datetime.timedelta(days=4)

klasse = s.klassen().filter(id=1188)[0]
tt = s.timetable(klasse=klasse, start=monday, end=friday)

print(tt)

s.logout()
