from models.news import Content
 

def create(item):
    img = item.find('.//rbc_news:image/rbc_news:url', namespaces={'rbc_news': 'https://www.rbc.ru'})
    if img == None:
        img = ''
    else:
        img = img.text
    try:
        return Content(
                title=item.find('title').text,
                link=item.find('link').text,
                img=img,
                pub_date=item.find('pubDate').text,
                description=item.find('description').text.strip('\n'),
                category=item.find('category').text,
                text=item.find('.//rbc_news:full-text', namespaces={'rbc_news': 'https://www.rbc.ru'}).text.strip('\n')
                ).dict()
    except:
        return None
                         