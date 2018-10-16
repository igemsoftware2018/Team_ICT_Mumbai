# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 12:44:52 2018

@author: Admin
"""
import tkinter
from tkinter import *
from tkinter import scrolledtext
window=Tk()
window.title("Welcome to Bio-Bricking software")
window.geometry('760x860')

global txt4
global lbl_warn
global lbl_help
global string_global

txt4=scrolledtext.ScrolledText(window,width=60, height=10)


lbl_warn=Label(window,text="")



lbl_help=Label(window,text="")

lbl_title=Label(window, text="BBrickIt!", font=("Helvetica", 20))
lbl_title.place(x = 30, y = 30)


lbl_dev=Label(window,text="Developed by iGEM Team - ICT Mumbai 2018", foreground='gray', font=("Arial", 8))
lbl_dev.place(x = 480, y = 5 , width=300, height=25)

lbl1=Label(window,text="Enter sequence", font=("Helvetica", 12))
lbl1.place(x = 180, y = 70 , width=300, height=25)

lbl_org=Label(window,text="Select Chassis", font=("Helvetica", 12))
lbl_org.place(x = 520, y = 70 , width=300, height=25)

lbl3=Label(window,text="Bio-Bricked Sequence", font=("Helvetica", 12))
lbl3.place(x = 300, y = 310)

lbla=Label(window,text="")
lbla.place(x = 45, y = 510)

lbl3=Label(window,text="")
lbl3.place(x = 100, y = 510)

lbl4=Label(window,text="")
lbl4.place(x = 170, y = 510)

lbl5=Label(window,text="")
lbl5.place(x = 240, y = 510)

lbl6=Label(window,text="")
lbl6.place(x = 310, y = 510)

lbl7=Label(window,text="")
lbl7.place(x = 380, y = 510)

lbl_com=Label(window,text="", justify= tkinter.LEFT)
lbl_com.place(x = 5, y = 530, width=700 )

lbl_com2=Label(window,text="", justify= tkinter.LEFT)
lbl_com2.place(x = 0, y = 580, width=700)

chks_ecoli=BooleanVar()
chks_sub=BooleanVar()
chks_sac=BooleanVar()
var=IntVar()
var1=IntVar()

chk_ecoli=Radiobutton(window, text='E. coli',variable=var, value=1, font='arial 10 italic', anchor=W)
chk_ecoli.place(x = 600, y = 100, width = 130)

chk_sub=Radiobutton(window, text='B. subtilis',variable=var, value=2, font='arial 10 italic', anchor=W)
chk_sub.place(x = 600, y = 140, width = 130)

chk_sac=Radiobutton(window, text='S. cervisiae',variable=var, value=3, font='arial 10 italic', anchor=W)
chk_sac.place(x = 600, y = 180, width = 130)

lbl_cod=Label(window,text="Is this a Coding Sequence?")
lbl_cod.place(x = 30, y = 265)

chk_yes=Radiobutton(window, text='YES',variable=var1, value=1)
chk_yes.place(x = 40, y = 290)

chk_no=Radiobutton(window, text='NO',variable=var1, value=0)
chk_no.place(x = 90, y = 290)


txt1=scrolledtext.ScrolledText(window,width=30, height=10)
txt1.place(x = 30, y = 100 , width=550, height=160)

txt3=scrolledtext.ScrolledText(window,width=60, height=10)
txt3.place(x = 30, y = 340 , width=700, height=150)

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
    
    global txt4
    global lbl_warn
    global lbl_help
    
    txt1.delete("1.0","end")
        
    lbl_warn.pack()
    lbl_warn.pack_forget()
    lbl_help.pack()
    lbl_help.pack_forget()
    
    txt4.pack()
    txt4.pack_forget()
    
    txt3.place(x = 30, y = 340 , width=700, height=150)
    

    txt3.delete("1.0","end")
    lbla.configure(text="")
    lbl3.configure(text="")
    lbl4.configure(text="")
    lbl5.configure(text="")
    lbl6.configure(text="")
    lbl7.configure(text="")
    lbl_com.configure(text="")
    lbl_com2.configure(text="")


def positions(target, source):

   pos = -1
   try:
       while True:
           pos = source.index(target, pos + 1)
           yield pos
   except ValueError:
         pass
def Help_window():
    window=Tk()
    window.title("Help for Bio-Bricking software")
    window.geometry('800x190')
    lbl_body=Label(window,text="", justify= tkinter.LEFT)
    lbl_body.place(x = 15, y = 15)
    lbl_body.config(text="1. Paste your sequence in box at the top.\n2. Select your Organism/Chassis. \n3. Select whether your sequence is a coding sequence or not using the radio buttons on the left hand bottom corner of the input box.\n4. Click <BioBrick>!\n5. If you wish to take the reverse complement of the sequence and then BioBrick it, click <Reverse Complement and BioBrick>\n \nIf your part contains any illegal restriction enzyme binding sites, two boxes will appear.\nThe left box will display the highlighted restriction sites with a legend at the bottom.\nThe right box will suggest the new, optimised sequence for selected organism.\nIf you wish to proceed with that sequence, copy it into top box and hit <BioBrick> again!", font=("Helvetica", 10), anchor=W)
    window.mainloop()
    
def About_window():
    window=Tk()
    window.title("About Bio-Bricking software")
    window.geometry('900x610')
    lbl_body=Label(window,text="", justify= tkinter.LEFT)
    lbl_body.place(x = 15, y = 15)
    lbl_body.config(text="This is a software that produces complete BioBricked part for you with just a click of a single button!\n\n\nIf you have any sequence that you want to BioBrick, just paste it into the box at the top, and hit <BioBrick>! \n\nIf your sequence contains any of the illegal restriction sites (EcoRI, XbaI, SpeI, PstI and NotI) then it cannot be BioBricked \n according to the protocols. Such sites will be highlighted and colour coded, and furthermore, the software will suggest \n another sequence, by changing a base or two in your input sequence. The new sequence will not retain the identity \n and the sequence of Amino acids in the resulting translated polypeptide.\n\nThe most exciting feature of this application is that it takes into account the codon preferences for your chassis organisms.\n The frequency and efficiency of usage of  codons in different organisms might be different for producing the same amino acid.\n BBrickIt takes that into account and then suggests a new sequence that is optimised for your own chassis organism!\n\n\nIn short, this application performs following operations on input sequence:\n1. BioBrick Prefix, either GAATTCGCGGCCGCTTCTAG or GAATTCGCGGCCGCTTCTAGAG is added to the sequence according to the conditions \n mentioned in Reference 1 which contains EcoRI and XbaI restriction sites.\n2. BioBrick Suffix TACTAGTAGCGGCCGCTGCAG is added to the sequence, which contains SpeI and PstI restriction sites.\n3. An additional 8 nt sequence, GTTTCTTC, as obtained from the Reference 2, is added to both flanks of the BioBricked part, to allow cleavage\n by restriction endonuclease close to the end of linear DNA Fragments.\n4. If the sequence is not BioBrickable, i.e. if it contains any of the restriction sites mentioned above, those sites are highlighted and colour coded.\n A legend at the bottom of the window shows the number of those sites individually.\n5. As a replacement for such sequences, a new sequence is suggested, with restriction sites tweaked based on the\n initial choice of the chassis organism.\n6. If the sequence is a coding sequence (CDS), the in-frame stop codon will be changed to TAA and one more TAA codon will be added,\n following the protocol given in Reference 3.\n\n\nReferences:\n1. http://parts.igem.org/Help:BioBrick_Prefix_and_Suffix\n2. Engineering BioBrick Vectors from BioBrick Parts; Shetty RP et. al.;J Biol Eng. 2008; 2: 5; DOI: 10.1186/1754-1611-2-5 \n3. http://parts.igem.org/Help:Primers/Design\n\nSoftware developed by: iGEM Team ICT Mumbai 2018.", font=("Helvetica", 10), anchor=W)
    window.mainloop()
    
btn_help=Button(window, text="Help", bg="white", fg="black", command=Help_window)
btn_help.place(x = 600, y = 265, width = 60)

btn_about=Button(window, text="About", bg="white", fg="black", command=About_window)
btn_about.place(x = 680, y = 265, width = 60)


def BB():
        
    global txt4
    global lbl_warn
    global lbl_help
    global string_global
    
    lbla.configure(text="")
    lbl3.configure(text="")
    lbl4.configure(text="")
    lbl5.configure(text="")
    lbl6.configure(text="")
    lbl7.configure(text="")
    lbl_com.configure(text="")
    lbl_com2.configure(text="")
    txt3.delete("1.0","end")
    dna1=txt1.get("1.0","end")
    
    
    txt3.delete("1.0","end")
    
    
    
    str1=GetStringWithoutNumbers(dna1)
    line=str1
    prefix1='GTTTCTTCGAATTCGCGGCCGCTTCTAG'
    suffix='TACTAGTAGCGGCCGCTGCAGGTTTCTTC'
    prefix2='GTTTCTTCGAATTCGCGGCCGCTTCTAGAG'
    
    
        
    EcorI=line.count('gaattc')    
    XbaI=line.count('tctaga')    
    SpeI=line.count('actagt')
    PstI=line.count('ctgcag')
    NotI=line.count('gcggccgc')
    
    EcorI_a=line.count('gaattc')    
    XbaI_a=line.count('tctaga')    
    SpeI_a=line.count('actagt')
    PstI_a=line.count('ctgcag')
    NotI_a=line.count('gcggccgc')
    
    

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
            
    string_global=line        
      
    if CuttersStatus==[0,0,0,0,0] and var.get()!=0:
        
        string=line
        
        lbl_warn.pack()
        lbl_warn.pack_forget()
        lbl_help.pack()
        lbl_help.pack_forget()
            
        txt4.pack()
        txt4.pack_forget()
        
        txt3.place(x = 30, y = 340 , width=700, height=150)
        
        txt3.delete("1.0","end")
        lbla.configure(text="")
        lbl3.configure(text="")
        lbl4.configure(text="")
        lbl5.configure(text="")
        lbl6.configure(text="")
        lbl7.configure(text="")
        lbl_com.configure(text="")
        
        if (var1.get()==1):
           
            if[str1[0],str1[1],str1[2]]==['a','t','g'] or [str1[0],str1[1],str1[2]]==['g','t','g']:
                list_stop=[]
                
                in_tag=0     
                while in_tag>=0:    
                    in_tag=int(string.find("tag",(in_tag+1)))
                    list_stop+=[in_tag]
                
                in_tga=0     
                while in_tga>=0:    
                    in_tga=int(string.find("tga",(in_tga+1)))
                    list_stop+=[in_tga]
                    
                in_taa=0     
                while in_taa>=0:    
                    in_taa=int(string.find("taa",(in_taa+1)))
                    list_stop+=[in_taa]
                    
                print(list_stop)
                
                list_stop_divbythree=[]
                for i in range(len(list_stop)):
                    if list_stop[i]%3==0:
                        list_stop_divbythree+=[list_stop[i]]
                        
                print(list_stop_divbythree)
                
                if len(list_stop_divbythree)!=0:
                    in_min_stop=min(list_stop_divbythree)
                    
                    string_old=string
                    string = string[:in_min_stop] + 'taataa'
                    
                    print(len(string_old))
                    print(in_min_stop)
                    
                    if in_min_stop==(len(string_old)-3):
                        lbl_com2.config(text='3. In frame stop codon was changed to the 6bp sequence TAATAA to ensure effective termination of transcription.')
                    else:
                        lbl_com2.config(text='3. In frame stop codon was changed to the 6bp sequence TAATAA to ensure effective termination of transcription. \n Further sequence was removed')
                        
                
                    
                elif len(list_stop_divbythree)==0:
                    window=Tk()
                    window.title("Warning!")
                    window.geometry('800x190')
                    lbl_body=Label(window,text="", justify= tkinter.LEFT)
                    lbl_body.place(x = 15, y = 15)
                    lbl_body.config(text="Your Coding Sequence does not have an in frame stop codon!\n If you still want to Bio-Brick it: \n1. Close this window \n2. Select 'No' under 'Is this a coding sequence?' \n3. Click <Bio-Brick> again", font=("Helvetica", 10), anchor=W)
                    window.mainloop()
                    string=string
            
            else:
                window=Tk()
                window.title("Warning!")
                window.geometry('500x150')
                lbl_body=Label(window,text="", justify= tkinter.LEFT)
                lbl_body.place(x = 15, y = 15)
                lbl_body.config(text="Your Coding Sequence does not start with the start codons 'atg' or 'gtg'\n If you still want to Bio-Brick it: \n1. Close this window \n2. Select 'No' under 'Is this a coding sequence?' \n3. Click <Bio-Brick> again", font=("Helvetica", 10), anchor=W)
                window.mainloop()
                
            
                
        if [str1[0],str1[1],str1[2]]==['a','t','g']:
            part=prefix1+string+suffix
        else:
            part=prefix2+string+suffix
            
        txt3.insert(INSERT,part) 
        
        if [str1[0],str1[1],str1[2]]==['a','t','g']:
            txt3.tag_add('tag1','1.0 + 8 chars','1.0 + 14 chars')
            txt3.tag_config('tag1',foreground="red")
            
            txt3.tag_add('tag3','1.0 + 23 chars','1.0 + 28 chars')
            txt3.tag_config('tag3',foreground="blue")
        else:
            txt3.tag_add('tag1','1.0 + 8 chars','1.0 + 14 chars')
            txt3.tag_config('tag1',foreground="red")
            
            txt3.tag_add('tag3','1.0 + 23 chars','1.0 + 29 chars')
            txt3.tag_config('tag3',foreground="blue")
        
        txt3.tag_add('tag6','end - 29 chars','end- 23 chars')
        txt3.tag_config('tag6',foreground="cyan")
        
        txt3.tag_add('tag7','end - 15 chars','end- 9 chars')
        txt3.tag_config('tag7',foreground="green")
        
        txt3.tag_add('tag8','1.0','1.0 + 8 chars')
        txt3.tag_config('tag8',foreground="Orange")
        
        txt3.tag_add('tag9','end - 9 chars','end')
        txt3.tag_config('tag9',foreground="Orange")
        
        
        
        lbla.configure(text='Legend:')
        lbl3.configure(text='EcoRI', foreground='red')
        lbl4.configure(text='XbaI', foreground='blue')
        lbl5.configure(text='SpeI', foreground='cyan')
        lbl6.configure(text='PstI', foreground='green')
        lbl7.configure(text='8 nt sequence', foreground='orange')
        
        lbl_com.config(text='1. EcoRI and XbaI sites are added as prefix. SpeI and PstI sites are added as suffix. \n 2. Also, an extra 8 nucleotide sequence GTTTCTTC was added to both the prefix and suffix to allow cleavage close to the \n end of linear DNA')
        #lbl_com.config(text='Also, 8 nucleotide sequence GTTTCTTC was added to both flangs of BioBrick part to make space for Restriction Enzyme to operate.')
        
        
        
    elif CuttersStatus!=[0,0,0,0,0] and var.get()!=0:
        string=str1
        noEcoRI=string.count("gaattc")
        noXbaI=string.count("tctaga")
        noPstI=string.count("ctgcag")
        noSpeI=string.count("actagt")
        noNotI=string.count("gcggccgc")
        
#E. Coli
        
        if(var.get()==1):
            while noEcoRI>0:
                EcorI=string.find("gaattc")
                y=EcorI+1
                if y%3==0:       #AAT changes to AAC
                    list1=list(string)
                    list1[EcorI+3]='c'
                    string="".join(list1)
                    
                elif y%3==2:      #ATT changes to ATC
                    list1=list(string)
                    list1[EcorI+4]='c'
                    string="".join(list1)
                    
                elif y%3==1:      #TTC changes to TTT
                    list1=list(string)
                    list1[EcorI+5]='t'
                    string="".join(list1)
                noEcoRI=string.count("gaattc")
            
            
            
            while noXbaI>0:
                XbaI=int(string.find("tctaga"))
                y=XbaI+1
                if y%3==0:       #CTA changes to CTG
                    list1=list(string)
                    list1[XbaI+3]='g'
                    string="".join(list1)
                    
                elif y%3==2:      #TAG changes to TAA
                    list1=list(string)
                    list1[XbaI+4]='a'
                    string="".join(list1)
                    
                elif y%3==1:      #AGA changes to CGT
                    list1=list(string)
                    list1[XbaI+5]='t'
                    list1[XbaI+3]='c'
                    string="".join(list1)
                noXbaI=string.count("tctaga")
                
                
            
            while noPstI>0:
                PstI=int(string.find("ctgcag"))
                y=PstI+1
                if y%3==0:       #TGC changes to TGT; although TGC is preferred by E Coli, the there is marginal difference between the two fractions.
                    list1=list(string)
                    list1[PstI+3]='t'
                    string="".join(list1)
                    
                elif y%3==2:      #GCA changes to GCG
                    list1=list(string)
                    list1[PstI+4]='g'
                    string="".join(list1)
                    
                elif y%3==1:      #CAG changes to CAA; both are dominant codons for respective AAs in E Coli, we chose the one that would have least effect.
                    list1=list(string)
                    list1[PstI+5]='a'
                    string="".join(list1)
                noPstI=string.count("ctgcag")
                    
            
            while noSpeI>0:
                SpeI=int(string.find("actagt"))
                y=SpeI+1
                if y%3==0:       #CTA changes to CTG
                    list1=list(string)
                    list1[SpeI+3]='g'
                    string="".join(list1)
                    
                elif y%3==2:      #TAG changes to TAA
                    list1=list(string)
                    list1[SpeI+4]='a'
                    string="".join(list1)
                    
                elif y%3==1:      #AGT changes to AGC
                    list1=list(string)
                    list1[SpeI+5]='c'
                    string="".join(list1)
                noSpeI=string.count("actagt")
                
            
            while noNotI>0:
                NotI=int(string.find("gcggccgc"))
                y=NotI+1
                if y%3==0:       #CGG changes to CGT
                    list1=list(string)
                    list1[NotI+3]='t'
                    string="".join(list1)
                    
                elif y%3==2:      #CGC changes to CGT
                    list1=list(string)
                    list1[NotI+7]='t'
                    string="".join(list1)
                    
                elif y%3==1:      #GCC changes to GCG
                    list1=list(string)
                    list1[NotI+5]='g'
                    string="".join(list1)
                noNotI=string.count("gcggccgc")
#B. Subtilis
        elif(var.get()==2):
            
            while noEcoRI>0:
                EcorI=string.find("gaattc")
                y=EcorI+1
                if y%3==0:       #AAT changes to AAC
                    list1=list(string)
                    list1[EcorI+3]='c'
                    string="".join(list1)
                    
                elif y%3==2:      #ATT changes to ATC; No Other option Available.
                    list1=list(string)
                    list1[EcorI+4]='c'
                    string="".join(list1)
                    
                elif y%3==1:      #TTC changes to TTT
                    list1=list(string)
                    list1[EcorI+5]='t'
                    string="".join(list1)
                noEcoRI=string.count("gaattc")
            
            
            
            while noXbaI>0:
                XbaI=int(string.find("tctaga"))
                y=XbaI+1
                if y%3==0:       #CTA changes to CTG
                    list1=list(string)
                    list1[XbaI+3]='g'
                    string="".join(list1)
                    
                elif y%3==2:      #TAG changes to TAA
                    list1=list(string)
                    list1[XbaI+4]='a'
                    string="".join(list1)
                    
                elif y%3==1:      #TCT changes to TCA
                    list1=list(string)
                    list1[XbaI+2]='a'
                    string="".join(list1)
                noXbaI=string.count("tctaga")
                
                
            
            while noPstI>0:
                PstI=int(string.find("ctgcag"))
                y=PstI+1
                if y%3==0:       #TGC changes to TGT;
                    list1=list(string)
                    list1[PstI+3]='t'
                    string="".join(list1)
                    
                elif y%3==2:      #GCA changes to GCG
                    list1=list(string)
                    list1[PstI+4]='g'
                    string="".join(list1)
                    
                elif y%3==1:      #CAG changes to CAA
                    list1=list(string)
                    list1[PstI+5]='a'
                    string="".join(list1)
                noPstI=string.count("ctgcag")
                    
            
            while noSpeI>0:
                SpeI=int(string.find("actagt"))
                y=SpeI+1
                if y%3==0:       #CTA changes to TTG
                    list1=list(string)
                    list1[SpeI+3]='g'
                    list1[SpeI+1]='t'
                    string="".join(list1)
                    
                elif y%3==2:      #TAG changes to TAA
                    list1=list(string)
                    list1[SpeI+4]='a'
                    string="".join(list1)
                    
                elif y%3==1:      #AGT changes to TCA
                    list1=list(string)
                    list1[SpeI+3]='t'
                    list1[SpeI+4]='c'
                    list1[SpeI+5]='a'
                    string="".join(list1)
                noSpeI=string.count("actagt")
                
            
            while noNotI>0:
                NotI=int(string.find("gcggccgc"))
                y=NotI+1
                if y%3==0:       #CGG changes to AGA
                    list1=list(string)
                    list1[NotI+1]='a'
                    list1[NotI+3]='a'
                    string="".join(list1)
                    
                elif y%3==2:      #CGC changes to AGA
                    list1=list(string)
                    list1[NotI+5]='a'
                    list1[NotI+7]='a'
                    string="".join(list1)
                    
                elif y%3==1:      #GCC changes to GCG
                    list1=list(string)
                    list1[NotI+5]='g'
                    string="".join(list1)
                noNotI=string.count("gcggccgc")
               
#S. Cervisiae
        elif(var.get()==3):
            
            while noEcoRI>0:
                EcorI=string.find("gaattc")
                y=EcorI+1
                if y%3==0:       #AAT changes to AAC only if other option is not valid.
                    list1=list(string)
                    if list1[EcorI+6]!='t':
                        list1[EcorI+6]='t'
                    elif list1[EcorI+6]=='t':
                        list1[EcorI+3]='c'
                    string="".join(list1)
                    
                elif y%3==2:      #ATT changes to ATA; No Other option Available.
                    list1=list(string)
                    list1[EcorI+4]='a'
                    string="".join(list1)
                    
                elif y%3==1:      #TTC changes to TTT
                    list1=list(string)
                    list1[EcorI+5]='t'
                    string="".join(list1)
                noEcoRI=string.count("gaattc")
            
            
            
            while noXbaI>0:
                XbaI=int(string.find("tctaga"))
                y=XbaI+1
                if y%3==0:       #CTA changes to TTG
                    list1=list(string)
                    list1[XbaI+3]='g'
                    list1[XbaI+1]='t'
                    string="".join(list1)
                    
                elif y%3==2:      #TAG changes to TAA
                    list1=list(string)
                    list1[XbaI+4]='a'
                    string="".join(list1)
                    
                elif y%3==1:      #TCT changes to TCA; not the most ideal option, but best choice of remaining. 
                    list1=list(string)
                    list1[XbaI+3]='a'
                    string="".join(list1)
                noXbaI=string.count("tctaga")
                
                
          
            while noPstI>0:
                PstI=int(string.find("ctgcag"))
                y=PstI+1
                if y%3==0:       #TGC changes to TGT;
                    list1=list(string)
                    list1[PstI+3]='t'
                    string="".join(list1)
                    
                elif y%3==2:      #GCA changes to GCT
                    list1=list(string)
                    list1[PstI+4]='t'
                    string="".join(list1)
                    
                elif y%3==1:      #CAG changes to CAA
                    list1=list(string)
                    list1[PstI+5]='a'
                    string="".join(list1)
                noPstI=string.count("ctgcag")
                    
           
            while noSpeI>0:
                SpeI=int(string.find("actagt"))
                y=SpeI+1
                if y%3==0:       #CTA changes to TTG
                    list1=list(string)
                    list1[SpeI+3]='g'
                    list1[SpeI+1]='t'
                    string="".join(list1)
                    
                elif y%3==2:      #TAG changes to TAA
                    list1=list(string)
                    list1[SpeI+4]='a'
                    string="".join(list1)
                    
                elif y%3==1:      #AGT changes to TCT
                    list1=list(string)
                    list1[SpeI+3]='t'
                    list1[SpeI+4]='c'
                    list1[SpeI+5]='t'
                    string="".join(list1)
                noSpeI=string.count("actagt")
                
            
            while noNotI>0:
                NotI=int(string.find("gcggccgc"))
                y=NotI+1
                if y%3==0:       #CGG changes to AGA
                    list1=list(string)
                    list1[NotI+1]='a'
                    list1[NotI+3]='a'
                    string="".join(list1)
                    
                elif y%3==2:      #CGC changes to AGA
                    list1=list(string)
                    list1[NotI+5]='a'
                    list1[NotI+7]='a'
                    string="".join(list1)
                    
                elif y%3==1:      #GCC changes to GCT
                    list1=list(string)
                    list1[NotI+5]='t'
                    string="".join(list1)
                noNotI=string.count("gcggccgc")
        
        
        
        res="Your coding sequence cannot be biobricked \n as it contains illegal restriction site(s)!"
        
        lbl_warn.pack()
        lbl_warn.pack_forget()
        lbl_help.pack()
        lbl_help.pack_forget()
            
        txt4.pack()
        txt4.pack_forget()
        
        txt3.place(x = 30, y = 340 , width=700, height=150)
        
        txt3.insert(INSERT,str1)
            
        txt4=scrolledtext.ScrolledText(window,width=60, height=10)
        txt4.place(x = 390, y = 400 , width=320, height=100)
            
        lbl_warn=Label(window,text="")
        lbl_warn.place(x = 30, y = 350)
        lbl_warn.configure(text=res)
        
        lbl_help=Label(window,text="")
        lbl_help.place(x = 390, y = 350)
        lbl_help.configure(text='Use the following sequence instead!')
        
        txt3.place(x = 30, y = 400 , width=320, height=100)
        
        
        txt4.insert(INSERT,string)
        
        lbl_com.configure(text='')
        lbl_com2.configure(text='')
        lbla.configure(text='Legend:')
        lbl3.configure(text='EcoRI: %d'%EcorI_a, foreground='red')
        lbl4.configure(text='XbaI: %d'%XbaI_a, foreground='blue')
        lbl5.configure(text='SpeI: %d'%SpeI_a, foreground='cyan')
        lbl6.configure(text='PstI: %d'%PstI_a, foreground='green')
        lbl7.configure(text='NotI: %d'%NotI_a, foreground='purple')
    
        
        txt3.insert('1.0','d')
        txt4.insert('1.0','d')
        
        
        pos=1.0
        pos1='1.0'
        while(pos1!=''):
            pos1 = txt3.search('gaattc', '%s + 1 chars'%pos1, stopindex=END)
            if(pos1!=''):
                txt3.tag_add(pos1,pos1,'%s + 6 chars'%pos1)
                txt3.tag_config(pos1,foreground="red")
                txt4.tag_add(pos1,pos1,'%s + 6 chars'%pos1)
                txt4.tag_config(pos1,foreground="red")
            
            
        pos=1.0
        pos1='1.0'
        while(pos1!=''):
            pos1 = txt3.search('tctaga', '%s + 1 chars'%pos1, stopindex=END)
            if(pos1!=''):
                txt3.tag_add(pos1,pos1,'%s + 6 chars'%pos1)
                txt3.tag_config(pos1,foreground="blue")
                txt4.tag_add(pos1,pos1,'%s + 6 chars'%pos1)
                txt4.tag_config(pos1,foreground="blue")
        
        pos=1.0
        pos1='1.0'
        while(pos1!=''):
            pos1 = txt3.search('actagt', '%s + 1 chars'%pos1, stopindex=END)
            if(pos1!=''):
                txt3.tag_add(pos1,pos1,'%s + 6 chars'%pos1)
                txt3.tag_config(pos1,foreground="cyan")
                txt4.tag_add(pos1,pos1,'%s + 6 chars'%pos1)
                txt4.tag_config(pos1,foreground="cyan")
                
        pos=1.0
        pos1='1.0'
        while(pos1!=''):
            pos1 = txt3.search('ctgcag', '%s + 1 chars'%pos1, stopindex=END)
            if(pos1!=''):
                txt3.tag_add(pos1,pos1,'%s + 6 chars'%pos1)
                txt3.tag_config(pos1,foreground="green")
                txt4.tag_add(pos1,pos1,'%s + 6 chars'%pos1)
                txt4.tag_config(pos1,foreground="green")
                
        pos=1.0
        pos1='1.0'
        while(pos1!=''):
            pos1 = txt3.search('gcggccgc', '%s + 1 chars'%pos1, stopindex=END)
            if(pos1!=''):
                txt3.tag_add(pos1,pos1,'%s + 8 chars'%pos1)
                txt3.tag_config(pos1,foreground="purple")
                txt4.tag_add(pos1,pos1,'%s + 8 chars'%pos1)
                txt4.tag_config(pos1,foreground="purple")
        
        txt3.delete('1.0')  
        txt4.delete('1.0')           
    

    else:
        txt3.insert(INSERT,'Please select an organism')
  
#********************************************************************************************      
        
# rev complement'
        
def BBRC():
    global txt4
    global lbl_warn
    global lbl_help
    
    lbla.configure(text="")
    lbl3.configure(text="")
    lbl4.configure(text="")
    lbl5.configure(text="")
    lbl6.configure(text="")
    lbl7.configure(text="")
    txt3.delete("1.0","end")
    dna1=txt1.get("1.0","end")
    
    
    txt3.delete("1.0","end")
    
    
    str1=reverse(GetComplement(txt1.get("1.0","end")))
    
    line=str1
    prefix1='GTTTCTTCGAATTCGCGGCCGCTTCTAG'
    suffix='TACTAGTAGCGGCCGCTGCAGGTTTCTTC'
    prefix2='GTTTCTTCGAATTCGCGGCCGCTTCTAGAG'
    
        
    EcorI=line.count('gaattc')    
    XbaI=line.count('tctaga')    
    SpeI=line.count('actagt')
    PstI=line.count('ctgcag')
    NotI=line.count('gcggccgc')
    
    EcorI_a=line.count('gaattc')    
    XbaI_a=line.count('tctaga')    
    SpeI_a=line.count('actagt')
    PstI_a=line.count('ctgcag')
    NotI_a=line.count('gcggccgc')
    
    

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
      
    if CuttersStatus==[0,0,0,0,0] and var.get()!=0: 
        
        string=line
        
        lbl_warn.pack()
        lbl_warn.pack_forget()
        lbl_help.pack()
        lbl_help.pack_forget()
            
        txt4.pack()
        txt4.pack_forget()
        
        txt3.place(x = 30, y = 340 , width=700, height=150)
        
        txt3.delete("1.0","end")
        lbla.configure(text="")
        lbl3.configure(text="")
        lbl4.configure(text="")
        lbl5.configure(text="")
        lbl6.configure(text="")
        lbl7.configure(text="")
        lbl_com.configure(text="")
        
        if (var1.get()==1):
            
            list_stop=[]
                
            in_tag=0     
            while in_tag>=0:    
                in_tag=int(string.find("tag",(in_tag+1)))
                list_stop+=[in_tag]
            
            in_tga=0     
            while in_tga>=0:    
                in_tga=int(string.find("tga",(in_tga+1)))
                list_stop+=[in_tga]
                
            in_taa=0     
            while in_taa>=0:    
                in_taa=int(string.find("taa",(in_taa+1)))
                list_stop+=[in_taa]
                
            print(list_stop)
            
            list_stop_divbythree=[]
            for i in range(len(list_stop)):
                if list_stop[i]%3==0:
                    list_stop_divbythree+=[list_stop[i]]
                    
            print(list_stop_divbythree)
            
            if len(list_stop_divbythree)!=0:
                in_min_stop=min(list_stop_divbythree)
                
                string_old=string
                string = string[:in_min_stop] + 'taataa'
                
                print(len(string_old))
                print(in_min_stop)
                
                if in_min_stop==(len(string_old)-3):
                    lbl_com2.config(text='3. In frame stop codon was changed to the 6bp sequence TAATAA to ensure effective termination of transcription.')
                else:
                    lbl_com2.config(text='3. In frame stop codon was changed to the 6bp sequence TAATAA to ensure effective termination of transcription. \n Further sequence was removed')
            
            
                
            elif len(list_stop_divbythree)==0:
                string=string
                
                
                
        if [str1[0],str1[1],str1[2]]==['a','t','g']:
            part=prefix1+string+suffix
        else:
            part=prefix2+string+suffix
            
        txt3.insert(INSERT,part) 
        
        if [str1[0],str1[1],str1[2]]==['a','t','g']:
            txt3.tag_add('tag1','1.0 + 8 chars','1.0 + 14 chars')
            txt3.tag_config('tag1',foreground="red")
            
            txt3.tag_add('tag3','1.0 + 23 chars','1.0 + 28 chars')
            txt3.tag_config('tag3',foreground="blue")
        else:
            txt3.tag_add('tag1','1.0 + 8 chars','1.0 + 14 chars')
            txt3.tag_config('tag1',foreground="red")
            
            txt3.tag_add('tag3','1.0 + 23 chars','1.0 + 29 chars')
            txt3.tag_config('tag3',foreground="blue")
        
        txt3.tag_add('tag6','end - 29 chars','end- 23 chars')
        txt3.tag_config('tag6',foreground="cyan")
        
        txt3.tag_add('tag7','end - 15 chars','end- 9 chars')
        txt3.tag_config('tag7',foreground="green")
        
        txt3.tag_add('tag8','1.0','1.0 + 8 chars')
        txt3.tag_config('tag8',foreground="Orange")
        
        txt3.tag_add('tag9','end - 9 chars','end')
        txt3.tag_config('tag9',foreground="Orange")
        
        
        
        lbla.configure(text='Legend:')
        lbl3.configure(text='EcoRI', foreground='red')
        lbl4.configure(text='XbaI', foreground='blue')
        lbl5.configure(text='SpeI', foreground='cyan')
        lbl6.configure(text='PstI', foreground='green')
        lbl7.configure(text='8 nt sequence', foreground='orange')
        
        lbl_com.config(text='1. EcoRI and XbaI sites are added as prefix. SpeI and PstI sites are added as suffix. \n 2. Also, an extra 8 nucleotide sequence GTTTCTTC was added to both the prefix and suffix to allow cleavage close to the \n end of linear DNA')
        #lbl_com.config(text='Also, 8 nucleotide sequence GTTTCTTC was added to both flangs of BioBrick part to make space for Restriction Enzyme to operate.')
        
        
        
    elif CuttersStatus!=[0,0,0,0,0] and var.get()!=0:
        string=str1
        noEcoRI=string.count("gaattc")
        noXbaI=string.count("tctaga")
        noPstI=string.count("ctgcag")
        noSpeI=string.count("actagt")
        noNotI=string.count("gcggccgc")
        
#E. Coli
        
        if(var.get()==1):
            while noEcoRI>0:
                EcorI=string.find("gaattc")
                y=EcorI+1
                if y%3==0:       #AAT changes to AAC
                    list1=list(string)
                    list1[EcorI+3]='c'
                    string="".join(list1)
                    
                elif y%3==2:      #ATT changes to ATC
                    list1=list(string)
                    list1[EcorI+4]='c'
                    string="".join(list1)
                    
                elif y%3==1:      #TTC changes to TTT
                    list1=list(string)
                    list1[EcorI+5]='t'
                    string="".join(list1)
                noEcoRI=string.count("gaattc")
            
            
            
            while noXbaI>0:
                XbaI=int(string.find("tctaga"))
                y=XbaI+1
                if y%3==0:       #CTA changes to CTG
                    list1=list(string)
                    list1[XbaI+3]='g'
                    string="".join(list1)
                    
                elif y%3==2:      #TAG changes to TAA
                    list1=list(string)
                    list1[XbaI+4]='a'
                    string="".join(list1)
                    
                elif y%3==1:      #AGA changes to CGT
                    list1=list(string)
                    list1[XbaI+5]='t'
                    list1[XbaI+3]='c'
                    string="".join(list1)
                noXbaI=string.count("tctaga")
                
                
            
            while noPstI>0:
                PstI=int(string.find("ctgcag"))
                y=PstI+1
                if y%3==0:       #TGC changes to TGT; although TGC is preferred by E Coli, the there is marginal difference between the two fractions.
                    list1=list(string)
                    list1[PstI+3]='t'
                    string="".join(list1)
                    
                elif y%3==2:      #GCA changes to GCG
                    list1=list(string)
                    list1[PstI+4]='g'
                    string="".join(list1)
                    
                elif y%3==1:      #CAG changes to CAA; both are dominant codons for respective AAs in E Coli, we chose the one that would have least effect.
                    list1=list(string)
                    list1[PstI+5]='a'
                    string="".join(list1)
                noPstI=string.count("ctgcag")
                    
            
            while noSpeI>0:
                SpeI=int(string.find("actagt"))
                y=SpeI+1
                if y%3==0:       #CTA changes to CTG
                    list1=list(string)
                    list1[SpeI+3]='g'
                    string="".join(list1)
                    
                elif y%3==2:      #TAG changes to TAA
                    list1=list(string)
                    list1[SpeI+4]='a'
                    string="".join(list1)
                    
                elif y%3==1:      #AGT changes to AGC
                    list1=list(string)
                    list1[SpeI+5]='c'
                    string="".join(list1)
                noSpeI=string.count("actagt")
                
            
            while noNotI>0:
                NotI=int(string.find("gcggccgc"))
                y=NotI+1
                if y%3==0:       #CGG changes to CGT
                    list1=list(string)
                    list1[NotI+3]='t'
                    string="".join(list1)
                    
                elif y%3==2:      #CGC changes to CGT
                    list1=list(string)
                    list1[NotI+7]='t'
                    string="".join(list1)
                    
                elif y%3==1:      #GCC changes to GCG
                    list1=list(string)
                    list1[NotI+5]='g'
                    string="".join(list1)
                noNotI=string.count("gcggccgc")
#B. Subtilis
        elif(var.get()==2):
            
            while noEcoRI>0:
                EcorI=string.find("gaattc")
                y=EcorI+1
                if y%3==0:       #AAT changes to AAC
                    list1=list(string)
                    list1[EcorI+3]='c'
                    string="".join(list1)
                    
                elif y%3==2:      #ATT changes to ATC; No Other option Available.
                    list1=list(string)
                    list1[EcorI+4]='c'
                    string="".join(list1)
                    
                elif y%3==1:      #TTC changes to TTT
                    list1=list(string)
                    list1[EcorI+5]='t'
                    string="".join(list1)
                noEcoRI=string.count("gaattc")
            
            
            
            while noXbaI>0:
                XbaI=int(string.find("tctaga"))
                y=XbaI+1
                if y%3==0:       #CTA changes to CTG
                    list1=list(string)
                    list1[XbaI+3]='g'
                    string="".join(list1)
                    
                elif y%3==2:      #TAG changes to TAA
                    list1=list(string)
                    list1[XbaI+4]='a'
                    string="".join(list1)
                    
                elif y%3==1:      #TCT changes to TCA
                    list1=list(string)
                    list1[XbaI+2]='a'
                    string="".join(list1)
                noXbaI=string.count("tctaga")
                
                
            
            while noPstI>0:
                PstI=int(string.find("ctgcag"))
                y=PstI+1
                if y%3==0:       #TGC changes to TGT;
                    list1=list(string)
                    list1[PstI+3]='t'
                    string="".join(list1)
                    
                elif y%3==2:      #GCA changes to GCG
                    list1=list(string)
                    list1[PstI+4]='g'
                    string="".join(list1)
                    
                elif y%3==1:      #CAG changes to CAA
                    list1=list(string)
                    list1[PstI+5]='a'
                    string="".join(list1)
                noPstI=string.count("ctgcag")
                    
            
            while noSpeI>0:
                SpeI=int(string.find("actagt"))
                y=SpeI+1
                if y%3==0:       #CTA changes to TTG
                    list1=list(string)
                    list1[SpeI+3]='g'
                    list1[SpeI+1]='t'
                    string="".join(list1)
                    
                elif y%3==2:      #TAG changes to TAA
                    list1=list(string)
                    list1[SpeI+4]='a'
                    string="".join(list1)
                    
                elif y%3==1:      #AGT changes to TCA
                    list1=list(string)
                    list1[SpeI+3]='t'
                    list1[SpeI+4]='c'
                    list1[SpeI+5]='a'
                    string="".join(list1)
                noSpeI=string.count("actagt")
                
            
            while noNotI>0:
                NotI=int(string.find("gcggccgc"))
                y=NotI+1
                if y%3==0:       #CGG changes to AGA
                    list1=list(string)
                    list1[NotI+1]='a'
                    list1[NotI+3]='a'
                    string="".join(list1)
                    
                elif y%3==2:      #CGC changes to AGA
                    list1=list(string)
                    list1[NotI+5]='a'
                    list1[NotI+7]='a'
                    string="".join(list1)
                    
                elif y%3==1:      #GCC changes to GCG
                    list1=list(string)
                    list1[NotI+5]='g'
                    string="".join(list1)
                noNotI=string.count("gcggccgc")
               
#S. Cervisiae
        elif(var.get()==3):
            
            while noEcoRI>0:
                EcorI=string.find("gaattc")
                y=EcorI+1
                if y%3==0:       #AAT changes to AAC only if other option is not valid.
                    list1=list(string)
                    if list1[EcorI+6]!='t':
                        list1[EcorI+6]='t'
                    elif list1[EcorI+6]=='t':
                        list1[EcorI+3]='c'
                    string="".join(list1)
                    
                elif y%3==2:      #ATT changes to ATA; No Other option Available.
                    list1=list(string)
                    list1[EcorI+4]='a'
                    string="".join(list1)
                    
                elif y%3==1:      #TTC changes to TTT
                    list1=list(string)
                    list1[EcorI+5]='t'
                    string="".join(list1)
                noEcoRI=string.count("gaattc")
            
            
            
            while noXbaI>0:
                XbaI=int(string.find("tctaga"))
                y=XbaI+1
                if y%3==0:       #CTA changes to TTG
                    list1=list(string)
                    list1[XbaI+3]='g'
                    list1[XbaI+1]='t'
                    string="".join(list1)
                    
                elif y%3==2:      #TAG changes to TAA
                    list1=list(string)
                    list1[XbaI+4]='a'
                    string="".join(list1)
                    
                elif y%3==1:      #TCT changes to TCA; not the most ideal option, but best choice of remaining. 
                    list1=list(string)
                    list1[XbaI+3]='a'
                    string="".join(list1)
                noXbaI=string.count("tctaga")
                
                
          
            while noPstI>0:
                PstI=int(string.find("ctgcag"))
                y=PstI+1
                if y%3==0:       #TGC changes to TGT;
                    list1=list(string)
                    list1[PstI+3]='t'
                    string="".join(list1)
                    
                elif y%3==2:      #GCA changes to GCT
                    list1=list(string)
                    list1[PstI+4]='t'
                    string="".join(list1)
                    
                elif y%3==1:      #CAG changes to CAA
                    list1=list(string)
                    list1[PstI+5]='a'
                    string="".join(list1)
                noPstI=string.count("ctgcag")
                    
           
            while noSpeI>0:
                SpeI=int(string.find("actagt"))
                y=SpeI+1
                if y%3==0:       #CTA changes to TTG
                    list1=list(string)
                    list1[SpeI+3]='g'
                    list1[SpeI+1]='t'
                    string="".join(list1)
                    
                elif y%3==2:      #TAG changes to TAA
                    list1=list(string)
                    list1[SpeI+4]='a'
                    string="".join(list1)
                    
                elif y%3==1:      #AGT changes to TCT
                    list1=list(string)
                    list1[SpeI+3]='t'
                    list1[SpeI+4]='c'
                    list1[SpeI+5]='t'
                    string="".join(list1)
                noSpeI=string.count("actagt")
                
            
            while noNotI>0:
                NotI=int(string.find("gcggccgc"))
                y=NotI+1
                if y%3==0:       #CGG changes to AGA
                    list1=list(string)
                    list1[NotI+1]='a'
                    list1[NotI+3]='a'
                    string="".join(list1)
                    
                elif y%3==2:      #CGC changes to AGA
                    list1=list(string)
                    list1[NotI+5]='a'
                    list1[NotI+7]='a'
                    string="".join(list1)
                    
                elif y%3==1:      #GCC changes to GCT
                    list1=list(string)
                    list1[NotI+5]='t'
                    string="".join(list1)
                noNotI=string.count("gcggccgc")
        
        
        
        res="Your coding sequence cannot be biobricked \n as it contains illegal restriction site(s)!"
        
        lbl_warn.pack()
        lbl_warn.pack_forget()
        lbl_help.pack()
        lbl_help.pack_forget()
            
        txt4.pack()
        txt4.pack_forget()
        
        txt3.place(x = 30, y = 340 , width=700, height=150)
        
        txt3.insert(INSERT,str1)
            
        txt4=scrolledtext.ScrolledText(window,width=60, height=10)
        txt4.place(x = 390, y = 400 , width=320, height=100)
            
        lbl_warn=Label(window,text="")
        lbl_warn.place(x = 30, y = 350)
        lbl_warn.configure(text=res)
        
        lbl_help=Label(window,text="")
        lbl_help.place(x = 390, y = 350)
        lbl_help.configure(text='Use the following sequence instead!')
        
        txt3.place(x = 30, y = 400 , width=320, height=100)
        
        
        txt4.insert(INSERT,string)
        
        lbl_com.configure(text='')
        lbl_com2.configure(text='')
        lbla.configure(text='Legend:')
        lbl3.configure(text='EcoRI: %d'%EcorI_a, foreground='red')
        lbl4.configure(text='XbaI: %d'%XbaI_a, foreground='blue')
        lbl5.configure(text='SpeI: %d'%SpeI_a, foreground='cyan')
        lbl6.configure(text='PstI: %d'%PstI_a, foreground='green')
        lbl7.configure(text='NotI: %d'%NotI_a, foreground='purple')
    
        
        txt3.insert('1.0','d')
        txt4.insert('1.0','d')
        
        
        pos=1.0
        pos1='1.0'
        while(pos1!=''):
            pos1 = txt3.search('gaattc', '%s + 1 chars'%pos1, stopindex=END)
            if(pos1!=''):
                txt3.tag_add(pos1,pos1,'%s + 6 chars'%pos1)
                txt3.tag_config(pos1,foreground="red")
                txt4.tag_add(pos1,pos1,'%s + 6 chars'%pos1)
                txt4.tag_config(pos1,foreground="red")
            
            
        pos=1.0
        pos1='1.0'
        while(pos1!=''):
            pos1 = txt3.search('tctaga', '%s + 1 chars'%pos1, stopindex=END)
            if(pos1!=''):
                txt3.tag_add(pos1,pos1,'%s + 6 chars'%pos1)
                txt3.tag_config(pos1,foreground="blue")
                txt4.tag_add(pos1,pos1,'%s + 6 chars'%pos1)
                txt4.tag_config(pos1,foreground="blue")
        
        pos=1.0
        pos1='1.0'
        while(pos1!=''):
            pos1 = txt3.search('actagt', '%s + 1 chars'%pos1, stopindex=END)
            if(pos1!=''):
                txt3.tag_add(pos1,pos1,'%s + 6 chars'%pos1)
                txt3.tag_config(pos1,foreground="cyan")
                txt4.tag_add(pos1,pos1,'%s + 6 chars'%pos1)
                txt4.tag_config(pos1,foreground="cyan")
                
        pos=1.0
        pos1='1.0'
        while(pos1!=''):
            pos1 = txt3.search('ctgcag', '%s + 1 chars'%pos1, stopindex=END)
            if(pos1!=''):
                txt3.tag_add(pos1,pos1,'%s + 6 chars'%pos1)
                txt3.tag_config(pos1,foreground="green")
                txt4.tag_add(pos1,pos1,'%s + 6 chars'%pos1)
                txt4.tag_config(pos1,foreground="green")
                
        pos=1.0
        pos1='1.0'
        while(pos1!=''):
            pos1 = txt3.search('gcggccgc', '%s + 1 chars'%pos1, stopindex=END)
            if(pos1!=''):
                txt3.tag_add(pos1,pos1,'%s + 8 chars'%pos1)
                txt3.tag_config(pos1,foreground="purple")
                txt4.tag_add(pos1,pos1,'%s + 8 chars'%pos1)
                txt4.tag_config(pos1,foreground="purple")
        
        txt3.delete('1.0')  
        txt4.delete('1.0')           
    

    else:
        txt3.insert(INSERT,'Please select an organism')

btn1=Button(window, text="Clear", bg="white", fg="black", command=clear1)
btn1.place(x = 620, y = 510, width = 80)

btn3=Button(window, text="BioBrick", bg="white", fg="blue", command=BB)
btn3.place(x = 190, y = 265, width = 150)

btn4=Button(window, text="Reverse Complement and BioBrick", bg="white", fg="blue", command=BBRC)
btn4.place(x = 360, y = 265, width = 200)
window.mainloop()


