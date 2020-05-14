import tkinter as tk
from tkinter.filedialog import askopenfilename
import requests
from bs4 import BeautifulSoup

def find():
	types=entry1.get()
	name=entry.get()
	URL = 'https://www.monster.com/jobs/search/?q=%s&where=%s'%(types,name)
	page = requests.get(URL)
	soup = BeautifulSoup(page.content, 'html.parser')
	results = soup.find(id='ResultsContainer')
	job_elems = results.find_all('section', class_='card-content')
	btn_open = tk.Button(text="All Results",command=open_file)
	btn_open.pack()
	
	file = open("all_results.txt","r+")
	file.truncate(0)
	file.close()
	file = open("all_results.txt","w")
	
	for job_elem in job_elems:
		title_elem = job_elem.find('h2', class_='title')
		company_elem = job_elem.find('div', class_='company')
		location_elem = job_elem.find('div', class_='location')
		if None in (title_elem, company_elem, location_elem):
			continue 
		file.write(title_elem.text.strip()+"\n")
		file.write(company_elem.text.strip()+"\n")
		file.write(location_elem.text.strip()+"\n\n")
			
	file.close()	

def open_file():
    """Open file"""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
		
m = tk.Tk()
m.iconbitmap('job_finder_icon.ico')
m.title("Job Finder")

frame = tk.Frame(master=m,relief=tk.RAISED ,borderwidth=5)
label = tk.Label(text="Search for Jobs:")
label.pack()
entry1 = tk.Entry(fg="black", bg="#D3D3D3", width=40)
entry1.pack()
label1 = tk.Label(text="Enter Location:")
label1.pack()
entry = tk.Entry(fg="black", bg="#D3D3D3", width=40)
entry.pack()
button = tk.Button(
    text="Search",
    master=frame,
    width=25,
    height=2,
	command=find,
)

button.pack()
frame.pack()   
m.mainloop()
