#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 19:14:31 2017

@author: abhilashsk
"""

from tkinter import *
from first import *
import datetime
class Application(Frame):
    
    """ GUI application """

    def __init__(self, master): #Function to initialize the Application
        """ Initialize the frame. """
        super(Application,self).__init__(master)
        self.grid()
        self.create_widgets()
        self.dataset=readData()
        self.dataset=cleanData(self.dataset)
        
    def create_widgets(self):   #Function to create Widgets to take data
        #Labels for setting the width of the columns
        Label(self,text="Enter data to selects Columns.",width=40).grid(row=0,column=0,sticky=W)
        Label(self,text="   ",width=40).grid(row=0,column=1,sticky=W)
        Label(self,text="   ",width=20).grid(row=0,column=2,sticky=W)
        Label(self,text="   ",width=20).grid(row=0,column=3,sticky=W)
        Label(self,text="   ",width=20).grid(row=0,column=4,sticky=W)
        Label(self,text="   ",width=20).grid(row=0,column=4,sticky=W)
        
        #Text boxes for take From and To date
        Label(self,text="From (YYYY-MM-DD) :").grid(row=1,column=0,sticky=W)
        self.frm=Entry(self)
        self.frm.grid(row=1,column=1,sticky=W)
        
        Label(self,text="To (YYYY-MM-DD) :").grid(row=2,column=0,sticky=W)
        self.to=Entry(self)
        self.to.grid(row=2,column=1,sticky=W)
        
        #Checkboxes for selecting columns from the dataset
        Label(self,text="Select Columns: ").grid(row=3,column=0,sticky=W)
        self.operator=BooleanVar()
        Checkbutton(self,text="OPERATOR",variable=self.operator).grid(row=3,column=1,sticky=W)
        self.route=BooleanVar()
        Checkbutton(self,text="ROUTE",variable=self.route).grid(row=3,column=3,sticky=W)
        self.flight=BooleanVar()
        Checkbutton(self,text="FLIGHT",variable=self.flight).grid(row=3,column=2,sticky=W)
        self.regis=BooleanVar()
        Checkbutton(self,text="REGISTRATION",variable=self.regis).grid(row=4,column=1,sticky=W)
        self.aboard=BooleanVar()
        Checkbutton(self,text="ABOARD",variable=self.aboard).grid(row=4,column=2,sticky=W)
        self.fatal=BooleanVar()
        Checkbutton(self,text="FATALITIES",variable=self.fatal).grid(row=4,column=3,sticky=W)
        
        #Text boxes to take Start and End indices of rows
        Label(self,text="Start Index:").grid(row=5,column=0,sticky=W)
        self.rowStart=Entry(self)
        self.rowStart.grid(row=5,column=1,sticky=W)
        Label(self,text="End Index:").grid(row=5,column=2,sticky=W)
        self.rowEnd=Entry(self)
        self.rowEnd.grid(row=5,column=3,sticky=W)
        
        #Button to submit the data
        self.btn=Button(self,text="SUBMIT",command=self.displayCols)
        self.btn.grid(row=6,column=2,columnspan=2,sticky=W)
        
        #Label for Discriptive Statistics section
        #Label(self,text="Discriptive Statistics.",width=40).grid(row=0,column=0,sticky=W)
        
        
        
    def displayCols(self):  #Function to display the columns
        #initialize variables
        msg={}
        col=0
        r=20
        w=40
        
        #Taking data from the entries
        if self.frm.get() and self.frm.get():
            frm=datetime.datetime.strptime(self.frm.get(), "%Y-%m-%d").date()
            to=datetime.datetime.strptime(self.to.get(), "%Y-%m-%d").date()
        rowStart=int(self.rowStart.get())
        rowEnd=int(self.rowEnd.get())
        newds=self.dataset
        newds=filterDs(newds,frm,to)
        
        
        #Checking for selected checkboxes
        if self.operator.get():
            msg['OPERATOR']=getColumns(newds,'Operator',rowStart,rowEnd)
        if self.route.get():
            msg['ROUTE']=getColumns(newds,'Route',rowStart,rowEnd)
        if self.flight.get():
            msg['FLIGHT NUMBER']=getColumns(newds,'Flight #',rowStart,rowEnd)
        if self.regis.get():
            msg['REGISTRATION']=getColumns(newds,'Registration',rowStart,rowEnd)
        if self.aboard.get():
            msg['ABOARD']=getColumns(newds,'Aboard',rowStart,rowEnd)
        if self.fatal.get():
            msg['FATALITIES']=getColumns(newds,'Fatalities',rowStart,rowEnd)
        
        #Displaying the columns in textareas
        for x in msg.keys():
            if col>1:
                w=20
            Label(self,text=x).grid(row=r,column=col,sticky=W)
            self.t=Text(self,width=w,height=rowEnd-rowStart,wrap=WORD)
            self.t.grid(row=r+2,column=col,rowspan=2,sticky=W)
            self.t.delete(0.0,END)
            self.t.insert(0.0,msg[x])
            self.t.config(state=DISABLED)
            col+=1
        
    
        

root=Tk()
root.title("Data analysis of Aircrash Dataset")
root.geometry("2000x2000")
app=Application(root)
root.mainloop()
