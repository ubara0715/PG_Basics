import bs4
soup = bs4.BeautifulSoup(open('example.html'), 'html.parser')
span_elem = soup.select('span')[0]
print(str(span_elem))
print(span_elem.get('id'))
print(span_elem.get('som_nonexistent_addr') == None)
print(span_elem.attrs)

