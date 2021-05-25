import requests
import pyttsx3
from bs4 import BeautifulSoup
from rich.console import Console
from rich.progress import track
from rich.progress import Progress
from time import sleep
from rich import print
from rich.panel import Panel
from rich.padding import Padding
from rich import box
import sys
import random


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
newVoiceRate = 145
engine.setProperty('rate',newVoiceRate)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    try:

        engine.say(audio)
        engine.runAndWait()
    except KeyboardInterrupt:
        quit()
        exit(0)    


console=Console()
console.rule("[bold red]Python Quote Generator")


with Progress() as progress:

    task1 = progress.add_task("[bold cyan]Fetching Beautiful Quote for You.....", total=100)
    while not progress.finished:
        progress.update(task1, advance=0.5)
        sleep(0.02)

def getQuote(pg):
    page = requests.get(
            "http://quotes.toscrape.com/page/"+str(pg)+"/")
    soup = BeautifulSoup(page.content, 'html.parser')
    quote = soup.find_all(class_='quote')
    try:

        for q in quote:
                quote_text=q.find('span',class_='text')
                authors=q.find('small',class_='author')
                quote=quote_text.text
                author=authors.text
                print(Panel.fit("[bold]"+quote+"[cyan] By ~[/cyan] "+"[italic yellow]"+author))
                speak(quote)
                speak("this quote was said by"+author);
    except KeyboardInterrupt:
        exit(0)
        



def main():
    pg=random.randint(1,5)
    getQuote(pg)
    op=''

    while op!="N":
        print("[bold cyan]More Quote ? Y/N")
        op=input();
        if(op=="Y"or op=="y"):
                
            pg+=1
            if(pg>10):
                print("Thanks ! Thats all for today");
            getQuote(pg)
        else:
                break;
    tk=("Thanks for using Quote CLI. If You Like this tool please Give star on https://github.com/kRavi07/python-quote-cli ")
    print(Panel("[bold green]"+tk))
    print("[bold yellow]Created By Ravi Kant Kumar ")     
    
    

main()

