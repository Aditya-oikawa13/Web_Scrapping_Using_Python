from bs4 import BeautifulSoup
import requests
html_text = requests.get('https://website.nitrkl.ac.in/Academics/AcademicDepartments/CurriculaDetails.aspx?d=Q0g6Q2hlbWljYWwgRW5naW5lZXJpbmc=-dmhpvpMkqIU=&di=Ng==-dYSTlPCIpzE=&c=Q2hlbWljYWwgRW5naW5lZXJpbmcgKEIuVGVjaC4gLSA0eXJzKQ==-Qpv4BN16nww=&t=VUc=-/CGGPdtU1IU=').text
soup = BeautifulSoup(html_text, 'lxml')
fifth_sem = soup.find('div', id = 'collapse5')
links = fifth_sem.find_all('a')
for subject in links:
    link = subject.get('href')
    link = " https://website.nitrkl.ac.in/Academics/AcademicDepartments/"  + link
    link_text = requests.get(link).text
    soup1 = BeautifulSoup(link_text, 'lxml')
    subject_info = soup1.find('div', class_ = 'col-md-12',style="text-align: justify; padding-bottom: 10px;").text
    syllabus = soup1.find('div', class_ = 'col-md-12 text-justify').text
    coordinator = soup1.find('div', class_ = 'col-md-12', style="text-align: justify;").text
    print(subject_info)
    print(coordinator)
    print(syllabus)
   