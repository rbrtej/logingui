from guizero import App, Text, PushButton, TextBox, Box, Window, info, error, yesno

f = open("userData.csv", "r")
fn = []
ln = []
usn = []
pw = []

for row in f:
    data = row.strip().split(",")
    fn.append(data[0].strip())
    ln.append(data[1].strip())
    usn.append(data[2].strip())
    pw.append(data[3].strip())
# def change_message():
#     message.value = 'ㅜ'


# def hide():
#     message.destroy()


# def introduce(first_name, last_name):
#     i = "nice to meet you "
#     message.value = i + last_name + first_name

app = App(title='help', height=300, width=500)
# box2 = Box(app, width = 'fill', align="top", height=50)
# box1 = Box(box2, width = 100,  height=50)

# message = Text(box1, text='pleese', align='left', width = 33)

# button = PushButton(box1,
#                     text='goodman',
#                     command=introduce,
#                     args=['o', 'j'],align='left', width = 33)

# tb = TextBox(box1, text='better',   align='left', width = 33)
def addtouserdata():
  x = ""
  for i in range(len(fn)):
    z = open('userData.csv', 'w')
    x = x + '{f},{l},{u},{p}'.format(f=fn[i], l=ln[i], u=usn[i],p=pw[i]) + '\n'
    z.write(x)
    z.close()

box1 = Box(app, width='fill', align='top', height=70)
box2 = Box(app, width='fill', align='top', height=100)
box3 = Box(app, width='fill', align='top', height=100)


# t1 = Text(box2, text="1")

box4 = Box(box2, width=260, align='left', height=100)
box5 = Box(box4, width=260, align='top', height=50)
box6 = Box(box4, width=260, align='bottom', height=50)
box7 = Box(box2, width=240, align='left', height=200)

wind = Window(app, title = 'fpfp',  visible=False)
box11 = Box(wind, width='fill', align='top', height=70)
box12 = Box(wind, width='fill', align='top', height=100)
box13 = Box(wind, width='fill', align='top', height=100)
box14 = Box(box12, width=260, align='left', height=100)
box15 = Box(box14, width=260, align='top', height=50)
box16 = Box(box14, width=260, align='bottom', height=50)
box17 = Box(box12, width=240, align='left', height=200)
fsn = TextBox(box15, align='right')
fff = Text(box15, text='First name:', align='right')
lsn = TextBox(box16, align='right')
lll = Text(box16, text='Last Name:', align='right')

windo = Window(app, title = 'fpfp',  visible=False)
box21 = Box(windo, width='fill', align='top', height=70)
box22 = Box(windo, width='fill', align='top', height=240)
box22_1 = Box(box22, width='200', align='right', height=240)
box22_2 = Box(box22, width='300', align='left', height=240)
box22_2_1 = Box(box22_2, width='fill', align='top', height=60)
box22_2_2 = Box(box22_2, width='fill', align='top', height=60)
box22_2_3 = Box(box22_2, width='fill', align='top', height=60)
box22_2_4 = Box(box22_2, width='fill', align='top', height=60)
ffff = Text(box22_2_1, text='First name:', align='left')
fssn = TextBox(box22_2_1, align='left')
llll = Text(box22_2_2, text='Last Name:', align='left')
lssn = TextBox(box22_2_2, align='left')
uuu = Text(box22_2_3, text='User Name:', align='left')
ussn = TextBox(box22_2_3, align='left')
ppp = Text(box22_2_4, text='Pass word:', align='left')
passn = TextBox(box22_2_4, align='left')

win = Window(app, title ='l', height=300, width=500, visible = False)
box31 = Box(win, width = 250, height = 'fill', align = 'left')
box32 = Box(win, width = 250, height = 'fill', align = 'right')
def jongjong():
  win.hide()
jong = PushButton(box31, text = 'quit',height='fill',width='fill',command=jongjong)

def deleft():
  plsdnt=win.yesno('', 'Are you sure about that?')
  if plsdnt==True:
    fn.pop(usn.index(un.value))
    ln.pop(usn.index(un.value))
    pw.pop(usn.index(un.value))
    usn.pop(usn.index(un.value))
    addtouserdata()
    win.hide()
  else:
    print('thanks')
      
  
out = PushButton(box32, text = 'delete account',height='fill',width='fill',command=deleft)

def go():
  if (fsn.value in fn):
    if (ln[fn.index(fsn.value)] == lsn.value) and (usn[fn.index(fsn.value)] == un.value):
      wind.hide()
      app.info('Password', pw[fn.index(fsn.value)])
    else:
      wind.error('error', 'last name not found')
  else:
    wind.error('error', 'first name not found')

  
    
def fpsn():
  wind.show()

def createAccount():
  if fssn.value != '' and lssn.value != '' and ussn.value != '' and passn.value != '':
    if (ussn.value not in usn):
      fn.append(fssn.value)
      ln.append(lssn.value)
      usn.append(ussn.value)
      pw.append(passn.value)
      windo.hide()
      info('sign up', 'g')
      addtouserdata()
    else:
      windo.error('error','existing username')
  else:
    windo.error('error', 'type something')
      
  
  
fidp = PushButton(box22_1, text='Create', align='left', height='fill', width='fill', command=createAccount)
# t2 = Text(box6, text="3")
# t3 = Text(box5, text="4")

un = TextBox(box5, align='right')
u = Text(box5, text='ID:', align='right')
ps = TextBox(box6, align='right')
p = Text(box6, text='PW:', align='right')
def signupu():
  windo.show()
signu = PushButton(box17, text='Find', align='left', height=6, width=6, command=go)

dsf = PushButton(box3, text='Sign up', height=1, width=23, align="top",command=signupu)

 
  
fp = PushButton(box3, text='Find Password', height=1, width=23, align="top", visible=False, command=fpsn)
def logindj():
  if (un.value not in usn):
    fp.visible=False
  else:
    if pw[usn.index(un.value)] == ps.value:
      win.show()
    else:
      fp.visible=True
      
lb = PushButton(box7, text='Login', align='left', height=3, width=6, command=logindj)


app.display()