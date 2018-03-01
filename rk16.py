#coding=utf-8


from selenium import webdriver


path = 'C:\Users\LENOVO-\AppData\Local\Google\Chrome\Application\chromedriver.exe'
web = webdriver.Chrome(executable_path=path)
web.get('https://www.taobao.com/')
web.find_element_by_id('q').send_keys(u'美食')
web.find_element_by_class_name('btn-search').click()
print web.page_source