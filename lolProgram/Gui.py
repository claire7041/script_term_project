from tkinter import *
from tkinter import font
from PIL import Image, ImageTk
from io import BytesIO
from collections import OrderedDict
import championserch
import favorites
import itemserch
import json
import search_summoner
import gmail
import urllib
import urllib.request


g_Tk = Tk()
g_Tk.title('▶League Of Legends 검색 프로그램◀')
g_Tk.config(width=800, height=600, bg='pink')
g_Tk.geometry('820x550')
DataList = []
favorites_type = 1
championname = "Amumu"
starData = str()
ChampionListBox = None
starListBox = None
def setfavorites_type(s):
    global favorites_data
    favorites_data = s

newImg = None
championlabel = None
itemlabel = None
def championimage(search):
    url = "http://ddragon.leagueoflegends.com/cdn/6.24.1/img/champion/{0}.png".format(search)
    with urllib.request.urlopen(url) as u:
        global newImg
        global championlabel
        newImg = None
        raw_data = u.read()
        im = Image.open(BytesIO(raw_data))
        newImg = ImageTk.PhotoImage(im)
        championlabel = Label(g_Tk, image=newImg)
        championlabel.pack()
        championlabel.place(x=600, y=290)

def itemimage(search):
    url = "http://ddragon.leagueoflegends.com/cdn/6.24.1/img/item/{0}.png".format(search)
    with urllib.request.urlopen(url) as u:
        global newImg
        global itemlabel
        newImg = None
        raw_data = u.read()
        im = Image.open(BytesIO(raw_data))
        newImg = ImageTk.PhotoImage(im)
        itemlabel = Label(g_Tk, image=newImg)
        itemlabel.pack()
        itemlabel.place(x=550, y=100)

def SearchButtonAction():
    global starListBox
    global starList
    global DataList
    global starData
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    iSearchIndex = starListBox.curselection()[0]
    f = open('star.txt', 'r')
    starList = json.load(f)
    f.close()
    i = 0
    for k in starList.keys():
        if(iSearchIndex == i):
            starData = str(k)
            if(starList.get(k)==1):
                searchChampionList()
            elif(starList.get(k)==2):
                searchItemList()
            elif(starList.get(k)==3):
                searchsummonerList()
        i += 1

    RenderText.configure(state='disabled')

def searchChampionList():
    global RenderText
    global starData
    global DataList
    global favorites_type
    global starList
    global itemlabel
    if itemlabel != None:
        itemlabel.destroy()
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    DataList, championname = championserch.championserch(starData)

    for i in DataList:
        RenderText.insert(INSERT, i)
    RenderText.configure(state='disabled')
    favorites_type = 1

    favoritesAddButton = Button(g_Tk, font=TempFont, text="★", command=addstar)
    favoritesAddButton.pack()
    favoritesAddButton.place(x=740, y=75)
    favoritesAddButton["bg"] = 'yellow'

    championimage(championname)
    ListBoxInit()

def searchChampionButton():
    global RenderText
    global SearchPlace
    global DataList
    global favorites_type
    global starList
    global itemlabel
    global championname
    if itemlabel != None:
        itemlabel.destroy()
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    DataList, championname = championserch.championserch(SearchPlace.get())

    for i in DataList:
        RenderText.insert(INSERT, i)
    RenderText.configure(state='disabled')
    favorites_type = 1

    favoritesAddButton = Button(g_Tk, font=TempFont, text="★", command=addstar)
    favoritesAddButton.pack()
    favoritesAddButton.place(x=740, y=75)
    favoritesAddButton["bg"] = 'yellow'

    championimage(championname)
    ListBoxInit()

def searchItemList():
    global RenderText
    global SearchPlace
    global starData
    global DataList
    global favorites_type
    global starList
    global championlabel
    if championlabel != None:
        championlabel.destroy()
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    DataList, itemid = itemserch.itemsearch(starData)
    for i in DataList:
        RenderText.insert(INSERT, i)
    RenderText.configure(state='disabled')
    favorites_type=2

    favoritesAddButton = Button(g_Tk, font=TempFont, text="★", command=addstar)
    favoritesAddButton.pack()
    favoritesAddButton.place(x=740, y=75)
    favoritesAddButton["bg"] = 'yellow'

    itemimage(itemid)
    ListBoxInit()

def searchItemButton():
    global RenderText
    global SearchPlace
    global DataList
    global favorites_type
    global championlabel
    if championlabel != None:
        championlabel.destroy()
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    DataList, itemid = itemserch.itemsearch(SearchPlace.get())
    for i in DataList:
        RenderText.insert(INSERT, i)
    RenderText.configure(state='disabled')
    favorites_type=2

    favoritesAddButton = Button(g_Tk, font=TempFont, text="★", command=addstar)
    favoritesAddButton.pack()
    favoritesAddButton.place(x=740, y=75)
    favoritesAddButton["bg"] = 'yellow'

    itemimage(itemid)
    ListBoxInit()

def searchsummonerList():
    global RenderText
    global SearchPlace
    global starData
    global DataList
    global favorites_type
    global starList
    global championlabel
    global itemlabel
    if itemlabel != None:
        itemlabel.destroy()
    if championlabel != None:
        championlabel.destroy()
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)

    DataList = search_summoner.searchsummoner(starData)

    for i in DataList:
        RenderText.insert(INSERT, i)
    RenderText.configure(state='disabled')
    favorites_type=3

    favoritesAddButton = Button(g_Tk, font=TempFont, text="★", command=addstar)
    favoritesAddButton.pack()
    favoritesAddButton.place(x=740, y=75)
    favoritesAddButton["bg"] = 'yellow'

    sendMailButton = Button(g_Tk, font=TempFont, text="메일 전송", command=mailsend)
    sendMailButton.pack()
    sendMailButton.place(x=540, y=470)
    sendMailButton["bg"] = 'white'
    ListBoxInit()

def clickmail():
    global recipientAddr
    recipientAddr = mailEntry.get()

def mailsend():
    global DataList
    global favorites_type
    global championname
    global SearchPlace
    DataList = search_summoner.searchsummoner(SearchPlace.get())

    for i in DataList:
        RenderText.insert(INSERT, i)
    gmail.sendMail(DataList, favorites_type, SearchPlace.get(), championname, recipientAddr)

top = Tk()
top.title('메일입력')
top.config(width=200, height=200, bg='skyblue')
mailEntry=Entry(top, bg='white', fg='black')
mailEntry.place(x=30, y=100)
MainText = Label(top, text="메일주소 입력", bg='skyblue', fg='black', font='Consolas 12 bold')
MainText.place(x=50, y=30)
selectbutton = Button(top, text='확인', command=clickmail)
selectbutton.pack()
selectbutton.place(x=80, y=150)
selectbutton["bg"] = 'yellow'

def searchsummonerButton():
    global RenderText
    global SearchPlace
    global DataList
    global favorites_type
    global championlabel
    global itemlabel
    if itemlabel != None:
        itemlabel.destroy()
    if championlabel != None:
        championlabel.destroy()
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    DataList = search_summoner.searchsummoner(SearchPlace.get())

    for i in DataList:
        RenderText.insert(INSERT, i)
    RenderText.configure(state='disabled')
    favorites_type=3

    favoritesAddButton = Button(g_Tk, font=TempFont, text="★", command=addstar)
    favoritesAddButton.pack()
    favoritesAddButton.place(x=740, y=75)
    favoritesAddButton["bg"] = 'yellow'

    sendMailButton = Button(g_Tk, font=TempFont, text="메일 전송", command=mailsend)
    sendMailButton.pack()
    sendMailButton.place(x=540, y=470)
    sendMailButton["bg"] = 'white'
    ListBoxInit()


def addfavorites():
    global favorites_type
    favorites.favoritesinsert(SearchPlace.get(), favorites_type)
    ListBoxInit()

starList = dict()

def addstar():
    global favorites_type
    global starList

    f = open('star.txt', 'r')
    starList = json.load(f)
    f.close()

    if(SearchPlace.get() in starList):
        del(starList[SearchPlace.get()])
    else:
        starList.setdefault(SearchPlace.get(), favorites_type)

    f = open('star.txt', 'w')
    json.dump(starList, f)
    f.close()
    ListBoxInit()


#newImg = None
#def evInser(search):

MainText = Label(g_Tk, text="▶League Of Legends 검색 프로그램◀", bg='pink', fg='black', font='Consolas 16 bold')
MainText.place(x=230, y=10)

TempFont = font.Font(g_Tk, size=12, weight='bold', family='Consolas')

def ButtonInit():
    championbutton = Button(g_Tk, font=TempFont, text='챔피언 검색', command=searchChampionButton)
    championbutton.pack()
    championbutton.place(x=40, y=100)
    championbutton["bg"] = 'skyblue'

    itembutton = Button(g_Tk, font=TempFont, text='아이템 검색', command=searchItemButton)
    itembutton.pack()
    itembutton.place(x=160, y=100)
    itembutton["bg"] = 'yellow'

    searchPlButton = Button(g_Tk, font=TempFont, text="소환사 검색", command=searchsummonerButton)
    searchPlButton.pack()
    searchPlButton.place(x=280, y=100)
    searchPlButton["bg"] = 'yellow green'

    GOButton = Button(g_Tk, font=TempFont, text=" GO ", command=SearchButtonAction)
    GOButton.pack()
    GOButton.place(x=80, y=360)
    GOButton["bg"] = 'gray'



# search place
starpush = 0
SearchPlace = Entry(g_Tk, bg='white', fg='black', font=TempFont)
SearchPlace.place(x=120, y=170)


def ListBoxInit():
    global starListBox
    if starListBox != None:
        starListBox.destroy()
    MainText = Label(g_Tk, text="[즐겨찾기]", bg='pink', fg='black', font='Consolas 16 bold')
    MainText.place(x=60, y=220)

    f = open('star.txt', 'r')
    starList = json.load(f)
    f.close()
    starListBoxScrollbar = Scrollbar(g_Tk)
    starListBoxScrollbar.pack()
    starListBoxScrollbar.place(x=190, y=290)
    starListBox = Listbox(g_Tk, font=TempFont, activestyle='none',
                              width=15, height=3, borderwidth=12, relief='ridge',
                              yscrollcommand=starListBoxScrollbar.set)
    i = 0
    for key in starList.keys():
        starListBox.insert(i, key)
        i += 1

    starListBox.pack()
    starListBox.place(x=30, y=270)
    starListBoxScrollbar.config(command=starListBox.yview)
    starListBoxScrollbar.pack()
    starListBoxScrollbar.place(x=190, y=290)

    # player
    MainText = Label(g_Tk, text="[최근검색]", bg='pink', fg='black', font='Consolas 16 bold')
    MainText.place(x=243, y=220)
    RecentPlayerListBox = Listbox(g_Tk, font=TempFont, activestyle='none',
                            width=15, height=5, borderwidth=12, relief='ridge')
    f = open('recent_data.txt', 'r')
    recently_ID = json.load(f)
    f.close()
    cnt = 0
    for l in recently_ID:
        cnt += 1
        RecentPlayerListBox.insert(cnt, l)

    RecentPlayerListBox.pack()
    RecentPlayerListBox.place(x=215, y=270)



RenderTextScrollbar = Scrollbar(g_Tk)
RenderTextScrollbar.pack()
RenderTextScrollbar.place(x=550, y=100)

RenderText = Text(g_Tk, width=50, height=25, borderwidth=12, relief='ridge', yscrollcommand=RenderTextScrollbar.set, bg='gray', fg='white')
RenderText.pack()
RenderText.place(x=400, y=80)

RenderTextScrollbar.config(command=RenderText.yview)
RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)
RenderText.configure(state='disabled')

ButtonInit()
ListBoxInit()
g_Tk.mainloop()

