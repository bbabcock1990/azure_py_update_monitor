    #Import Libraries
import PySimpleGUI as gui
import feedparser
import webbrowser


   #Grab Azure RSS Feed
def newsUpdate():
    newsFeed = feedparser.parse("https://azurecomcdn.azureedge.net/en-us/updates/feed/")
    return newsFeed
    #Grab News Count
def newsCount(newsFeed):
    count=len(newsFeed.entries)
    return count
    #Grab Instance Update
def grabUpdate(instance,newsFeed):
    entry = newsFeed.entries[instance]
    window['-TITLE-'].update(entry.title)
    link=window['-LINK-'].update(entry.link)


    #Create GUI Labels
title = gui.Text('Grabbing Updates', key='-TITLE-', auto_size_text=False)
link = gui.Text('', key='-LINK-',enable_events=True, auto_size_text=False, text_color='lightblue')

    #Pull Intial Feed
nf=newsUpdate();
ct=newsCount(nf);


    #Create GUI Layout
layout=[
    [title],
    [link],
    [gui.Button("Exit")]]

window = gui.Window("Azure RSS Feed",layout,keep_on_top=True)

while True:
    event, values = window.read(timeout=5000)
    if event == "Exit" or event == gui.WIN_CLOSED:
        break
    if event=='-LINK-':
        print(link.DisplayText)
        webbrowser.open_new(link.DisplayText)
    elif ct >= -1:
        grabUpdate(ct-1,nf);
        ct=ct-1
        print(ct)
    else:
        nf=newsUpdate();
        ct=newsCount(nf);
window.close()