#!/usr/bin/python -tt

from tkinter import *
from tkinter import ttk, Scrollbar
import requests
from tkinter import messagebox
import time
from win10toast import ToastNotifier
import json


root = Tk()
root.title("Stocker")
root.resizable(False, False)
root.iconbitmap('icon.ico')


l = ('World', 'USA', 'Brazil', 'India', 'Russia', 'Peru', 'Chile', 'Mexico', 'South Africa', 'Spain', 'UK', 'Iran', 'Pakistan', 'Italy', 'Saudi Arabia', 'Turkey', 'Germany', 'Bangladesh', 'France', 'Colombia', 'Argentina', 'Canada', 'Qatar', 'Iraq', 'Egypt', 'Indonesia', 'Sweden', 'Ecuador', 'Belarus', 'Kazakhstan', 'Belgium', 'Oman', 'Philippines', 'Kuwait', 'Ukraine', 'UAE', 'Bolivia', 'Netherlands', 'Panama', 'Portugal', 'Dominican Republic', 'Singapore', 'Israel', 'Poland', 'Afghanistan', 'Romania', 'Bahrain', 'Nigeria', 'Armenia', 'Switzerland', 'Guatemala', 'Honduras', 'Azerbaijan', 'Ireland', 'Ghana', 'Japan', 'Algeria', 'Moldova', 'Serbia', 'Austria', 'Nepal', 'Morocco', 'Cameroon', 'Uzbekistan', 'S. Korea', 'Czechia', 'Ivory Coast', 'Denmark', 'Kyrgyzstan', 'Kenya', 'El Salvador', 'Australia', 'Sudan', 'Venezuela',
'Norway', 'Costa Rica', 'Malaysia', 'North Macedonia', 'Senegal', 'DRC', 'Ethiopia', 'Bulgaria', 'Bosnia and Herzegovina', 'Palestine', 'Finland', 'Haiti', 'Tajikistan', 'French Guiana', 'Guinea', 'Gabon', 'Madagascar', 'Mauritania', 'Luxembourg', 'Djibouti', 'CAR', 'Hungary', 'Croatia', 'Greece', 'Albania', 'Thailand', 'Paraguay', 'Nicaragua', 'Somalia', 'Equatorial Guinea', 'Maldives', 'Mayotte', 'Sri Lanka', 'Malawi', 'Lebanon', 'Cuba', 'Mali', 'Congo', 'South Sudan', 'Estonia', 'Slovakia', 'Iceland', 'Lithuania', 'Guinea-Bissau', 'Slovenia', 'Zambia', 'Cabo Verde', 'Sierra Leone', 'Hong Kong', 'Libya', 'New Zealand', 'Yemen', 'Eswatini', 'Rwanda', 'Mozambique', 'Benin', 'Tunisia', 'Montenegro', 'Jordan', 'Latvia', 'Niger', 'Zimbabwe', 'Liberia', 'Uganda', 'Burkina Faso', 'Namibia', 'Cyprus', 'Uruguay', 'Georgia', 'Chad', 'Andorra', 'Suriname', 'Jamaica', 'Togo', 'Sao Tome and Principe', 'Diamond Princess', 'San Marino', 'Malta', 'Réunion', 'Channel Islands', 'Angola', 'Tanzania', 'Syria', 'Taiwan', 'Botswana', 'Vietnam', 'Mauritius', 'Myanmar', 'Isle of Man', 'Comoros', 'Guyana', 'Burundi', 'Mongolia', 'Lesotho', 'Martinique', 'Eritrea', 'Cayman Islands', 'Guadeloupe', 'Faeroe Islands', 'Gibraltar', 'Cambodia', 'Bermuda', 'Brunei', 'Trinidad and Tobago', 'Bahamas', 'Monaco', 'Aruba', 'Barbados', 'Seychelles', 'Liechtenstein', 'Bhutan', 'Sint Maarten', 'Antigua and Barbuda', 'Turks and Caicos', 'Gambia', 'French Polynesia', 'Macao', 'Saint Martin', 'Belize', 'St. Vincent Grenadines', 'Curaçao', 'Fiji', 'Timor-Leste', 'Grenada', 'New Caledonia', 'Saint Lucia', 'Laos', 'Dominica', 'Saint Kitts and Nevis', 'Falkland Islands', 'Greenland', 'Montserrat', 'Vatican City', 'Papua New Guinea', 'Western Sahara', 'MS Zaandam', 'Caribbean Netherlands', 'British Virgin Islands', 'St. Barth', 'Anguilla', 'Saint Pierre Miquelon', 'China')

def checkkey(event):
    value = event.widget.get()
    if value == '':
        data = l
    else:
        data = []
        for item in l:
            if value.lower() in item.lower():
                data.append(item)
    update(data)

def update(data):
    lb.delete(0, 'end')
    for item in data:
        lb.insert('end', item)


frame = LabelFrame(root, padx=10, pady=10)
frame.grid(row=0, column=0, padx=5, pady=5)
entry = Entry(frame, font = ("Calibri", 12), borderwidth=2, width = 30)

entry.grid(row=0, column=0, columnspan=2)
entry.bind('<KeyRelease>', checkkey)


vscrollbar = Scrollbar(frame,  orient=VERTICAL)
vscrollbar.grid(row=1, column=2, sticky=N+S)
lb = Listbox(frame, font = ("Calibri", 12), borderwidth=2, height=20, width=30)
lb.grid(row=1, column=0, columnspan=2, pady=8)
update(l)
lb.config(yscrollcommand=vscrollbar.set)
vscrollbar.config(command=lb.yview)

sframe = LabelFrame(root, padx=10, pady=10)
sframe.grid(row=0, column=1, padx=5, pady=5)

Label(sframe, text = "Cases", font = ("Calibri", 12)).grid(row=0, column=0, padx = 10, pady = 10, sticky = W)
Label(sframe, text = "TodayCases", font = ("Calibri", 12)).grid(row=1, column=0, padx = 10, pady = 10, sticky = W)
Label(sframe, text = "Deaths", font = ("Calibri", 12)).grid(row=2, column=0, padx = 10, pady = 10, sticky = W)
Label(sframe, text = "TodayDeaths", font = ("Calibri", 12)).grid(row=3, column=0, padx = 10, pady = 10, sticky = W)
Label(sframe, text = "Recovered", font = ("Calibri", 12)).grid(row=4, column=0, padx = 10, pady = 10, sticky = W)
Label(sframe, text = "Active", font = ("Calibri", 12)).grid(row=5, column=0, padx = 10, pady = 10, sticky = W)
Label(sframe, text = "Critical", font = ("Calibri", 12)).grid(row=6, column=0, padx = 10, pady = 10, sticky = W)
Label(sframe, text = "CasesPerOneMillion", font = ("Calibri", 12)).grid(row=7, column=0, padx = 10, pady = 10, sticky = W)
Label(sframe, text = "DeathsPerOneMillion", font = ("Calibri", 12)).grid(row=8, column=0, padx = 10, pady = 10, sticky = W)
Label(sframe, text = "TotalTests", font = ("Calibri", 12)).grid(row=9, column=0, padx = 10, pady = 10, sticky = W)
Label(sframe, text = "TestsPerOneMillion", font = ("Calibri", 12)).grid(row=10, column=0, padx = 10, pady = 10, sticky = W)



Cases = Text(sframe, height=1, width=20, borderwidth = 2, font = ("Calibri", 12))
Cases.grid(row=0, column = 1)
TodayCases = Text(sframe, height=1, width=20, borderwidth = 2, font = ("Calibri", 12))
TodayCases.grid(row=1, column = 1)
Deaths = Text(sframe, height=1, width=20, borderwidth = 2, font = ("Calibri", 12))
Deaths.grid(row=2, column = 1)
TodayDeaths = Text(sframe, height=1, width=20, borderwidth = 2, font = ("Calibri", 12))
TodayDeaths.grid(row=3, column = 1)
Recovered = Text(sframe, height=1, width=20, borderwidth = 2, font = ("Calibri", 12))
Recovered.grid(row=4, column = 1)
Active = Text(sframe, height=1, width=20, borderwidth = 2, font = ("Calibri", 12))
Active.grid(row=5, column = 1)
Critical = Text(sframe, height=1, width=20, borderwidth = 2, font = ("Calibri", 12))
Critical.grid(row=6, column = 1)
CasesPerOneMillion = Text(sframe, height=1, width=20, borderwidth = 2, font = ("Calibri", 12))
CasesPerOneMillion.grid(row=7, column = 1)
DeathsPerOneMillion = Text(sframe, height=1, width=20, borderwidth = 2, font = ("Calibri", 12))
DeathsPerOneMillion.grid(row=8, column = 1)
TotalTests = Text(sframe, height=1, width=20, borderwidth = 2, font = ("Calibri", 12))
TotalTests.grid(row=9, column = 1)
TestsPerOneMillion = Text(sframe, height=1, width=20, borderwidth = 2, font = ("Calibri", 12))
TestsPerOneMillion.grid(row=10, column = 1)


def select():

    global entry
    global Cases
    global TodayCases
    global Deaths
    global TodayDeaths
    global Recovered
    global Active
    global Critical
    global CasesPerOneMillion
    global DeathsPerOneMillion
    global TotalTests
    global TestsPerOneMillion



    entry.delete(0, END)
    entry.insert(0, lb.get(ANCHOR))



    cname = str(lb.get(ANCHOR))

    url = f'https://coronavirus-19-api.herokuapp.com/countries/{cname}'
    r = requests.get(url)
    data = r.json()

    Cases.configure(state='normal')
    TodayCases.configure(state='normal')
    Deaths.configure(state='normal')
    TodayDeaths.configure(state='normal')
    Recovered.configure(state='normal')
    Active.configure(state='normal')
    Critical.configure(state='normal')
    CasesPerOneMillion.configure(state='normal')
    DeathsPerOneMillion.configure(state='normal')
    TotalTests.configure(state='normal')
    TestsPerOneMillion.configure(state='normal')

    Cases.delete(1.0, END)
    TodayCases.delete(1.0, END)
    Deaths.delete(1.0, END)
    TodayDeaths.delete(1.0, END)
    Recovered.delete(1.0, END)
    Active.delete(1.0, END)
    Critical.delete(1.0, END)
    CasesPerOneMillion.delete(1.0, END)
    DeathsPerOneMillion.delete(1.0, END)
    TotalTests.delete(1.0, END)
    TestsPerOneMillion.delete(1.0, END)

    Cases.insert(END, str(data["cases"]))
    TodayCases.insert(END, str(data["todayCases"]))
    Deaths.insert(END, str(data["deaths"]))
    TodayDeaths.insert(END, str(data["todayDeaths"]))
    Recovered.insert(END, str(data["recovered"]))
    Active.insert(END, str(data["active"]))
    Critical.insert(END, str(data["critical"]))
    CasesPerOneMillion.insert(END, str(data["casesPerOneMillion"]))
    DeathsPerOneMillion.insert(END, str(data["deathsPerOneMillion"]))
    TotalTests.insert(END, str(data["totalTests"]))
    TestsPerOneMillion.insert(END, str(data["testsPerOneMillion"]))



    Cases.configure(state='disabled')
    TodayCases.configure(state='disabled')
    Deaths.configure(state='disabled')
    TodayDeaths.configure(state='disabled')
    Recovered.configure(state='disabled')
    Active.configure(state='disabled')
    Critical.configure(state='disabled')
    CasesPerOneMillion.configure(state='disabled')
    DeathsPerOneMillion.configure(state='disabled')
    TotalTests.configure(state='disabled')
    TestsPerOneMillion.configure(state='disabled')
def notify():
    global notify
    ncname = str(lb.get(ANCHOR))
    if len(ncname) == 0:
        messagebox.showerror('Country', 'Select your Country')
    else:
        res = messagebox.askquestion('Country', 'Notify for every minute?')
        root.withdraw()
        if res == 'yes':
            nurl = f'https://coronavirus-19-api.herokuapp.com/countries/{ncname}'
            nr = requests.get(nurl)
            ndata = nr.json()
            ntext = f"Confirmed Cases : {ndata['cases']} \nDeaths : {ndata['deaths']} \nRecovered : {ndata['recovered']}"
            while True:
                toast = ToastNotifier()
                toast.show_toast(f'{ncname} Covid-19 Updates', ntext, duration=10, icon_path ="icon.ico")
                time.sleep(60)

search = Button(frame, text="Show", width=10, fg='white', bg='black', command=select)
search.grid(row=3, column=0, pady=10, columnspan=1)
notify = Button(frame, text="Notify", width=10, fg='white', bg='black', command=notify)
notify.grid(row=3, column=1, pady=10, columnspan=1)

Label(root, text = "Project by Subareesh", fg='red').grid(row=1, column=0, columnspan=2)
root.mainloop()
