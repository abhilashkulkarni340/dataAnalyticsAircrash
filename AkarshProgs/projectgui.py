from tkinter import *
from first import *
import datetime


class AnalysisNumber(Frame):
    

    def __init__(self, master): #Function to initialize the window
        #Initialize the frame
        super(AnalysisNumber,self).__init__(master)
        self.grid()
        self.display_widgets()
        self.configure(bg="lightblue")
        self.dataset=readData()
        self.dataset=cleanData(self.dataset)
        
    def display_widgets(self):   #Function to create Widgets to take data
        
        
        """
        This section is for selecting columns to view the dataset
        """
        #Labels for setting the width of the columns
        Label(self,text="ENTER DATA TO SELECT COLUMNS ",bg="lightblue",font="times 16 bold italic").grid(row=0,column=0,columnspan=2,sticky=W)
        
        Label(self,text="   ",bg="lightblue",width=25).grid(row=0,column=2,sticky=W)
        Label(self,text="   ",bg="lightblue",width=25).grid(row=0,column=3,sticky=W)
        Label(self,text="   ",bg="lightblue",width=25).grid(row=0,column=4,sticky=W)
        Label(self,text="   ",bg="lightblue",width=25).grid(row=0,column=5,sticky=W)
#        self.close=Button(self,text="Quit",command=self.closeWindow)
#        self.close.grid(row=0,column=6,sticky=W)
        
        #Text boxes for take From and To date
        Label(self,text="From (YYYY-MM-DD) :",bg="lightblue").grid(row=1,column=0,sticky=W)
        self.frm=Entry(self)
        self.frm.grid(row=1,column=1,sticky=W)
        
        Label(self,bg="lightblue",text="To (YYYY-MM-DD) :").grid(row=1,column=2,sticky=W)
        self.to=Entry(self)
        self.to.grid(row=1,column=3,sticky=W)
        
        #Checkboxes for selecting columns from the dataset
        Label(self,bg="lightblue",text="Select Columns: *").grid(row=3,column=0,sticky=W)
        self.operator=BooleanVar()
        Checkbutton(self,bg="lightblue",text="OPERATOR",variable=self.operator).grid(row=3,column=1,sticky=W)
        self.route=BooleanVar()
        Checkbutton(self,bg="lightblue",text="ROUTE",variable=self.route).grid(row=3,column=3,sticky=W)
        self.flight=BooleanVar()
        Checkbutton(self,bg="lightblue",text="FLIGHT",variable=self.flight).grid(row=3,column=2,sticky=W)
        self.regis=BooleanVar()
        Checkbutton(self,bg="lightblue",text="REGISTRATION",variable=self.regis).grid(row=4,column=1,sticky=W)
        self.aboard=BooleanVar()
        Checkbutton(self,bg="lightblue",text="ABOARD",variable=self.aboard).grid(row=4,column=2,sticky=W)
        self.fatal=BooleanVar()
        Checkbutton(self,bg="lightblue",text="FATALITIES",variable=self.fatal).grid(row=4,column=3,sticky=W)
        
        #Text boxes to take Start and End indices of rows
        Label(self,bg="lightblue",text="Start Index:").grid(row=5,column=0,sticky=W)
        self.rowStart=Entry(self)
        self.rowStart.grid(row=5,column=1,sticky=W)
        Label(self,bg="lightblue",text="End Index:").grid(row=5,column=2,sticky=W)
        self.rowEnd=Entry(self)
        self.rowEnd.grid(row=5,column=3,sticky=W)
        
        #Entry for displaying number of entries
        Label(self,bg="lightblue",text="Number of Entries:").grid(row=6,column=0,sticky=W)
        self.num_entries=Entry(self)
        self.num_entries.grid(row=6,column=1,sticky=W)
        
        #Button to submit the data
        self.btn1=Button(self,text="SUBMIT COLUMNS",font="Georgia 10 bold ",command=self.displayCols)
        self.btn1.grid(row=7,column=2,columnspan=2,sticky=W)
        
        
        
        """
        This section is for displaying Descriptive Statistics
        """
        
        Label(self,bg="lightblue",text="*********").grid(row=49,column=0,columnspan=7,sticky=E)
        
        #Label for Descriptive Statistics section
        Label(self,bg="lightblue",text="DESCRIPTIVE STATISTICS",font="times 16 bold italic").grid(row=50,column=0,columnspan=2,sticky=W)
        
        #Radiobutton for selecting columns
        Label(self,bg="lightblue",text="Select Columns:* ").grid(row=51,column=0,sticky=W)
        self.col=StringVar()
        Radiobutton(self,bg="lightblue",text="ABOARD",variable=self.col,value='Aboard').grid(row=51,column=1,sticky=W)
        Radiobutton(self,bg="lightblue",text="FATALITIES",variable=self.col,value='Fatalities').grid(row=51,column=2,sticky=W)
        Radiobutton(self,bg="lightblue",text="GROUND",variable=self.col,value='Ground').grid(row=51,column=3,sticky=W)
        
        #Radiobutton to select particular statistic
        Label(self,bg="lightblue",text="Select Result:* ").grid(row=52,column=0,sticky=W)
        self.stat=StringVar()
        Radiobutton(self,bg="lightblue",text="COUNT",variable=self.stat,value='count').grid(row=52,column=1,sticky=W)
        Radiobutton(self,bg="lightblue",text="MEAN",variable=self.stat,value='mean').grid(row=52,column=2,sticky=W)
        Radiobutton(self,bg="lightblue",text="STANDARD DEVIATION",variable=self.stat,value='std').grid(row=52,column=3,sticky=W)
        Radiobutton(self,bg="lightblue",text="MINIMUM",variable=self.stat,value='min').grid(row=52,column=4,sticky=W)
        Radiobutton(self,bg="lightblue",text="MAXIMUM",variable=self.stat,value='max').grid(row=52,column=5,sticky=W)
        Radiobutton(self,bg="lightblue",text="ALL",variable=self.stat,value='all').grid(row=52,column=6,sticky=W)
        
        
        #Entries for displaying stats
        Label(self,bg="lightblue",text="COUNT").grid(row=53,column=0,sticky=W)
        self.count=Entry(self)
        self.count.grid(row=54,column=0,sticky=W)
        Label(self,bg="lightblue",text="MEAN").grid(row=53,column=1,sticky=W)
        self.mean=Entry(self)
        self.mean.grid(row=54,column=1,sticky=W)
        Label(self,bg="lightblue",text="STANDARD DEVIATION").grid(row=53,column=2,sticky=W)
        self.std=Entry(self)
        self.std.grid(row=54,column=2,sticky=W)
        Label(self,bg="lightblue",text="MINIMUM").grid(row=53,column=3,sticky=W)
        self.min=Entry(self)
        self.min.grid(row=54,column=3,sticky=W)
        Label(self,bg="lightblue",text="MAXIMUM").grid(row=53,column=4,sticky=W)
        self.max=Entry(self)
        self.max.grid(row=54,column=4,sticky=W)

        #Button to submit data
        Label(self,bg="lightblue",text=" ").grid(row=55,column=0,sticky=W)
        self.btn2=Button(self,text="SUBMIT STATISTICS",font="Georgia 10 bold ",command=self.descStat)
        self.btn2.grid(row=55,column=2,columnspan=2,sticky=W)
        
    def displayCols(self):  #Function to display the colum
        #initialize variables
        msg={}
        col=0
        r=70
        
        #Taking from and to data the entries
        if self.frm.get() and self.to.get():
            frm=datetime.datetime.strptime(self.frm.get(), "%Y-%m-%d").date()
            to=datetime.datetime.strptime(self.to.get(), "%Y-%m-%d").date()
        else:
            frm=datetime.datetime.strptime("1910-01-01", "%Y-%m-%d").date()
            to=datetime.datetime.strptime("1990-01-01", "%Y-%m-%d").date()
            
        
        #filtering the dataset by dates
        newds=self.dataset
        newds=filterDs(newds,frm,to)
        
        #get newds shape
        newds_shape=desDataset(newds,"shape")[0]
        self.num_entries.config(state=NORMAL)
        self.num_entries.delete(0,END)
        self.num_entries.insert(0,str(newds_shape))
        self.num_entries.config(state=DISABLED)
        
        #Taking start and end index
        if  self.rowStart.get() and self.rowEnd.get():
            rowStart=int(self.rowStart.get())
            rowEnd=int(self.rowEnd.get())
        else:
            rowStart=0
            rowEnd=desDataset(newds,"shape")[0]
        
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
            Label(self,bg="lightblue",text=x).grid(row=r,column=col,sticky=W)
            self.t=Text(self,bg="lightblue",width=25,height=rowEnd-rowStart,wrap=WORD)
            self.t.grid(row=r+2,column=col,rowspan=2,sticky=W)
            self.t.config(state=NORMAL)
            self.t.delete(0.0,END)
            self.t.insert(0.0,msg[x])
            self.t.config(state=DISABLED)
            col+=1
        
    def descStat(self): #Function to get descriptive statistics of a particular column
        #initializing dictionary to store the entry objects
        x={'count':self.count,'mean':self.mean,'std':self.std,'min':self.min,'max':self.max}
        
        #reading data from the radiobuttons
        if self.col.get() and self.stat.get():
            col=self.col.get()
            stat=self.stat.get()
        
        #fetching the statistics
        desc=desColumns(self.dataset,col)
        
        #displaying the result in the text boxes
        if self.stat.get()=='all':
            for i in x.keys():
                x[i].config(state=NORMAL)
                x[i].delete(0,END)
                x[i].insert(0,desc[i])
                x[i].config(state=DISABLED)
        else:
            x[self.stat.get()].config(state=NORMAL)
            x[self.stat.get()].delete(0,END)
            x[self.stat.get()].insert(0,desc[stat])
            x[self.stat.get()].config(state=DISABLED)
        
    def closeWindow(self):  #Function to close the window
        self.master.quit()
        self.master.destroy()

#root=Tk()
#root.title("Data analysis of Aircrash Dataset")
#root.geometry("2000x2000")
#app=Application(root)
#root.mainloop()
