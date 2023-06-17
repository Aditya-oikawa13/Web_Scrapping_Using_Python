from bs4 import BeautifulSoup
with open('home.html', 'r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content,'lxml')
    course_cards = soup.find_all('div',class_ = 'card')
    for course in course_cards:
        course = course_cards.h5.text
        course_price = course_cards.a.text.split()[-1]
        print(f'{course} costs {course_price}')
    
