import requests
from bs4 import BeautifulSoup
import lxml
import os


def generate_files():
    html_dir = '/home/deji/Desktop/deji/PycharmProjects/pythonProject/code_proj/site_scrape/html_dir/'
    os.makedirs(html_dir, exist_ok=True)

    # Define file paths
    html_file = os.path.join(html_dir, 'file.html')
    js_file = os.path.join(html_dir, 'file.js')
    css_file = os.path.join(html_dir, 'file.css')
    source=requests.get('https://personal-blog-trx3.onrender.com').content

    soup=BeautifulSoup(source,'lxml')

    with open(html_file,'w') as f:
        data=soup.prettify()
        f.write(data)
        f.close()


    find_script_tag=soup.find_all('script')
    change_tag=str(find_script_tag)
    with open(js_file,'w') as f:
        f.write(change_tag)
        f.close()

        
    find_css_tag=soup.find_all('link')
    css_style=find_css_tag[1]

    css_style_link='https://personal-blog-trx3.onrender.com' + css_style['href']


    new_request=requests.get(css_style_link).content
    soup=BeautifulSoup(new_request,'lxml')
    css_style=soup.prettify()
    with open(css_file,'w') as f:
        f.write(css_style)
        f.close()
        
    print('Done....')

generate_files()