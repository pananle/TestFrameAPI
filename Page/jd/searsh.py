from selenium.webdriver.common.by import By

page_url = 'https://search.jd.com/'

elements = [
    {'name': 'result_list', 'desc': '结果列表', 'by': (By.CLASS_NAME, u'gl-item'), 'ec': 'presence_of_all_elements_located', 'action': None},
    {'name': 'price', 'desc': '价格', 'by': (By.XPATH, u".//div[@class='p-price']/strong/i"), 'ec': 'presence_of_element_located', 'action': 'text'},
    {'name': 'pname', 'desc': '描述', 'by': (By.XPATH, u".//div[@class='p-name p-name-type-2']/a/em"), 'ec': 'presence_of_element_located', 'action': 'text'}
]
