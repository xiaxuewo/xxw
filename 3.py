import  requests
from lxml import etree

urls = ['https://www.jb51.net/article/{}.htm'.format(i) for i in range(195411,195625)]

path = r"D:\xxw\py\shu"

def get_text(url):
    r = requests.get(url)
    r.encoding = 'utf-8'

    selector = etree.HTML(r.text)
    title = selector.xpath('//*[@id="article"]/h1/text()')

    with open(path+title(0),'w',encoding='utf-8') as f:
        for i in text:
            f.write[i]

if __name__ == '__main__':
    for url in urls:
        get_text(url)
