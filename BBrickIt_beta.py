
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 21:59:46 2018

@author: Admin
"""

from tkinter import *
from tkinter import scrolledtext
window=Tk()
window.title("Welcome to Bio-Bricking software")
window.geometry('760x860')

lbl_title=Label(window, text="BBrickIt!", font=("Helvetica", 20))
lbl_title.place(x = 30, y = 30)


lbl1=Label(window,text="Enter coding sequence here", font=("Helvetica", 12))
lbl1.place(x = 250, y = 70 , width=300, height=25)

lbl3=Label(window,text="Bio-Bricked Sequence", font=("Helvetica", 12))
lbl3.place(x = 300, y = 310)

lbla=Label(window,text="")
lbla.place(x = 70, y = 570)

lbl3=Label(window,text="")
lbl3.place(x = 70, y = 590)

lbl4=Label(window,text="")
lbl4.place(x = 140, y = 590)

lbl5=Label(window,text="")
lbl5.place(x = 210, y = 590)

lbl6=Label(window,text="")
lbl6.place(x = 280, y = 590)

lbl7=Label(window,text="")
lbl7.place(x = 350, y = 590)

txt1=scrolledtext.ScrolledText(window,width=30, height=10)
txt1.place(x = 30, y = 100 , width=700, height=160)



txt3=scrolledtext.ScrolledText(window,width=60, height=10)
txt3.place(x = 30, y = 340 , width=700, height=200)

#cagcagcaagaacagcagcaaggcggcatgaaagtgaaagtgcaacgctttgggagttatttgagcggaatgatcatgccgaatatcggcgcgtttatcgcgtggggtatcattaccgcgctgtttattccggcaggatggtttccgaatgaacagctgaacacgctggtcagcccgatgattacgtatttattgccgcttttgatagcgtatacaggcggaaaaatgatctacgaccaccgcggcggagttgtcggagcgacagcggcaattggggtgattgtaggatcggatattccaatgtttttaggcgcaatgattatgggtccgcttggcggatacctcattaaacagactgataaattattcaaggataaagtcaagcaaggcttt
def reverse(string):
    string = "".join(reversed(string))
    return string

def GetStringWithoutNumbers(dna1):
    line=dna1
    line1=[]
    for i in range (0,len(line)):
        base=line[i]
        if base == 'a' or base=='A':
            line1+=['a']
        elif base == 't' or base=='T':
            line1+=['t']
        elif base == 'c' or base=='C':
            line1+=['c']
        elif base == 'g' or base=='G':
            line1+=['g']
    str1=''.join(line1)
    return str1

def GetComplement(dna1):
    dna1=GetStringWithoutNumbers(dna1)
    line=dna1
    line1=[]
    for i in range (0,len(line)):
        base=line[i]
        if base == 'a':
            line1+=['t']
        elif base == 't':
            line1+=['a']
        elif base == 'c':
            line1+=['g']
        elif base == 'g':
            line1+=['c']
    str1=''.join(line1)
    return str1

def Complement():
    
    dna1=txt1.get("1.0","end")
    str1=GetComplement(dna1)
    
    
def ReverseComplement():
    
    dna1=txt1.get("1.0","end")
    str1=reverse(GetComplement(dna1))
    
    
def clear1():
    txt1.delete("1.0","end")
    
    txt3.delete("1.0","end")
    lbla.configure(text="")
    lbl3.configure(text="")
    lbl4.configure(text="")
    lbl5.configure(text="")
    lbl6.configure(text="")
    lbl7.configure(text="")


def positions(target, source):

   pos = -1
   try:
       while True:
           pos = source.index(target, pos + 1)
           yield pos
   except ValueError:
         pass

def BB():
    lbla.configure(text="")
    lbl3.configure(text="")
    lbl4.configure(text="")
    lbl5.configure(text="")
    lbl6.configure(text="")
    lbl7.configure(text="")
    txt3.delete("1.0","end")
    dna1=txt1.get("1.0","end")
    
    line=dna1
    txt3.delete("1.0","end")
    dna1=txt1.get("1.0","end")
    str1=GetStringWithoutNumbers(dna1)

    prefix1='GAATTCGCGGCCGCTTCTAG'
    suffix='TACTAGTAGCGGCCGCTGCAG'
    prefix2='GAATTCGCGGCCGCTTCTAGAG'
    
    if [line[0],line[1],line[2]]==['a','t','g']:
        part=prefix1+str1+suffix
    else:
        part=prefix2+str1+suffix
        
    EcorI=line.count('gaattc')    
    XbaI=line.count('tctaga')    
    SpeI=line.count('actagt')
    PstI=line.count('ctgcag')
    NotI=line.count('gcggccgc')

    Cutters=['EcorI','XbaI','SpeI','PstI','NotI']
    CuttersStatus=[EcorI,XbaI,SpeI,PstI,NotI]

    cutters0=[]
    cutters1=[]
    cutters2=[]
    for i in range(5):
        if CuttersStatus[i]==0:
            cutters0+=[Cutters[i]]
        elif CuttersStatus[i]==1:
            cutters1+=[Cutters[i]]
        elif CuttersStatus[i]==2:
            cutters2+=[Cutters[i]]
      
    if CuttersStatus==[0,0,0,0,0]:
        txt3.insert(INSERT,part) 
        if [str1[0],str1[1],str1[2]]==['a','t','g']:
            txt3.tag_add('tag1','1.0','1.0 + 20 chars')
            txt3.tag_config('tag1',foreground="Blue")
        else:
            txt3.tag_add('tag1','1.0','1.0 + 22 chars')
            txt3.tag_config('tag1',foreground="Blue")
        
        txt3.tag_add('tag2','end - 22 chars','end')
        txt3.tag_config('tag2',foreground="red")
        
    else:
        res="Your coding sequence cannot be biobricked as it has the following cutters!\n\n\n"
        txt3.insert(INSERT,res)
        txt3.insert(INSERT,str1)
        
        lbla.configure(text='Legend')
        lbl3.configure(text='EcorI: %d'%EcorI, foreground='red')
        lbl4.configure(text='XbaI: %d'%XbaI, foreground='blue')
        lbl5.configure(text='SpeI: %d'%SpeI, foreground='cyan')
        lbl6.configure(text='PstI: %d'%PstI, foreground='green')
        lbl7.configure(text='NotI: %d'%NotI, foreground='purple')
    
    
    txt3.insert('1.0','d')
    
    pos=1.0
    pos1='1.0'
    while(pos1!=''):
        pos1 = txt3.search('gaattc', '%s + 1 chars'%pos1, stopindex=END)
        if(pos1!=''):
            txt3.tag_add(pos1,pos1,'%s + 6 chars'%pos1)
            txt3.tag_config(pos1,foreground="red")
        
        
    pos=1.0
    pos1='1.0'
    while(pos1!=''):
        pos1 = txt3.search('tctaga', '%s + 1 chars'%pos1, stopindex=END)
        if(pos1!=''):
            txt3.tag_add(pos1,pos1,'%s + 6 chars'%pos1)
            txt3.tag_config(pos1,foreground="blue")
    
    pos=1.0
    pos1='1.0'
    while(pos1!=''):
        pos1 = txt3.search('actagt', '%s + 1 chars'%pos1, stopindex=END)
        if(pos1!=''):
            txt3.tag_add(pos1,pos1,'%s + 6 chars'%pos1)
            txt3.tag_config(pos1,foreground="cyan")
            
    pos=1.0
    pos1='1.0'
    while(pos1!=''):
        pos1 = txt3.search('ctgcag', '%s + 1 chars'%pos1, stopindex=END)
        if(pos1!=''):
            txt3.tag_add(pos1,pos1,'%s + 6 chars'%pos1)
            txt3.tag_config(pos1,foreground="green")
            
    pos=1.0
    pos1='1.0'
    while(pos1!=''):
        pos1 = txt3.search('gcggccgc', '%s + 1 chars'%pos1, stopindex=END)
        if(pos1!=''):
            txt3.tag_add(pos1,pos1,'%s + 8 chars'%pos1)
            txt3.tag_config(pos1,foreground="purple")
    
    txt3.delete('1.0')           
    


def BBRC():
    lbla.configure(text="")
    lbl3.configure(text="")
    lbl4.configure(text="")
    lbl5.configure(text="")
    lbl6.configure(text="")
    lbl7.configure(text="")
    txt3.delete("1.0","end")
    str1=reverse(GetComplement(txt1.get("1.0","end")))

    prefix1='GAATTCGCGGCCGCTTCTAG'
    suffix='TACTAGTAGCGGCCGCTGCAG'
    prefix2='GAATTCGCGGCCGCTTCTAGAG'
    
    if [str1[0],str1[1],str1[2]]==['a','t','g']:
        part=prefix1+str1+suffix
    else:
        part=prefix2+str1+suffix
        
    EcorI=str1.count('gaattc')    
    XbaI=str1.count('tctaga')    
    SpeI=str1.count('actagt')
    PstI=str1.count('ctgcag')
    NotI=str1.count('gcggccgc')

    Cutters=['EcorI','XbaI','SpeI','PstI','NotI']
    CuttersStatus=[EcorI,XbaI,SpeI,PstI,NotI]

    cutters0=[]
    cutters1=[]
    cutters2=[]
    for i in range(5):
        if CuttersStatus[i]==0:
            cutters0+=[Cutters[i]]
        elif CuttersStatus[i]==1:
            cutters1+=[Cutters[i]]
        elif CuttersStatus[i]==2:
            cutters2+=[Cutters[i]]
      
    if CuttersStatus==[0,0,0,0,0]:
        txt3.insert(INSERT,part) 
        if [str1[0],str1[1],str1[2]]==['a','t','g']:
            txt3.tag_add('tag1','1.0','1.0 + 20 chars')
            txt3.tag_config('tag1',foreground="Blue")
        else:
            txt3.tag_add('tag1','1.0','1.0 + 22 chars')
            txt3.tag_config('tag1',foreground="Blue")
        
        txt3.tag_add('tag2','end - 22 chars','end')
        txt3.tag_config('tag2',foreground="red")
    else:
        res="Your coding sequence cannot be biobricked as it has the following cutters!\n\n\n"
        txt3.insert(INSERT,res)
        txt3.insert(INSERT,str1)
        
        lbla.configure(text='Legend')
        lbl3.configure(text='EcorI: %d'%EcorI, foreground='red')
        lbl4.configure(text='XbaI: %d'%XbaI, foreground='blue')
        lbl5.configure(text='SpeI: %d'%SpeI, foreground='cyan')
        lbl6.configure(text='PstI: %d'%PstI, foreground='green')
        lbl7.configure(text='NotI: %d'%NotI, foreground='purple')
    
    txt3.insert('1.0','d')
    
    pos=1.0
    pos1='1.0'
    while(pos1!=''):
        pos1 = txt3.search('gaattc', '%s + 1 chars'%pos1, stopindex=END)
        if(pos1!=''):
            txt3.tag_add(pos1,pos1,'%s + 6 chars'%pos1)
            txt3.tag_config(pos1,foreground="red")
        
        
    pos=1.0
    pos1='1.0'
    while(pos1!=''):
        pos1 = txt3.search('tctaga', '%s + 1 chars'%pos1, stopindex=END)
        if(pos1!=''):
            txt3.tag_add(pos1,pos1,'%s + 6 chars'%pos1)
            txt3.tag_config(pos1,foreground="blue")
    
    pos=1.0
    pos1='1.0'
    while(pos1!=''):
        pos1 = txt3.search('actagt', '%s + 1 chars'%pos1, stopindex=END)
        if(pos1!=''):
            txt3.tag_add(pos1,pos1,'%s + 6 chars'%pos1)
            txt3.tag_config(pos1,foreground="cyan")
            
    pos=1.0
    pos1='1.0'
    while(pos1!=''):
        pos1 = txt3.search('ctgcag', '%s + 1 chars'%pos1, stopindex=END)
        if(pos1!=''):
            txt3.tag_add(pos1,pos1,'%s + 6 chars'%pos1)
            txt3.tag_config(pos1,foreground="green")
            
    pos=1.0
    pos1='1.0'
    while(pos1!=''):
        pos1 = txt3.search('gcggccgc', '%s + 1 chars'%pos1, stopindex=END)
        if(pos1!=''):
            txt3.tag_add(pos1,pos1,'%s + 8 chars'%pos1)
            txt3.tag_config(pos1,foreground="purple")
            
    txt3.delete('1.0')   
    

btn1=Button(window, text="Clear", bg="white", fg="blue", command=clear1)
btn1.place(x = 620, y = 550, width = 80)

btn3=Button(window, text="BioBrick", bg="white", fg="blue", command=BB)
btn3.place(x = 190, y = 265, width = 200)

btn3=Button(window, text="BioBrick Reverse Complement", bg="white", fg="blue", command=BBRC)
btn3.place(x = 400, y = 265, width = 200)
window.mainloop()
