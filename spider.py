import numpy as np
import requests
from lxml import etree
from bs4 import BeautifulSoup
import csv
import pandas as pd


class WeatherSpider:
    def __init__(self):
        self.url = 'https://lishi.tianqi.com/zhengzhou/202401.html'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
        }

    def get_html(self):
        # response = requests.get(self.url, headers=self.headers)
        # if response.status_code == 200:
        #     tree = etree.HTML(response.text)
        #     xpath_expr = '//ul/li/div/[@class="th200"]/text()'  # 举例，解析网页的标题
        #
        #     # 使用etree.xpath()方法执行XPath查询
        #     result = tree.xpath(xpath_expr)

        month_list = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        date_list = []
        tmp1_list = []
        tmp2_list = []
        weather_list = []
        wind_list = []
        for year in range(2020, 2025):
            for month in month_list:
                url = f'https://lishi.tianqi.com/zhengzhou/{year}{month}.html'
                html = requests.get(url, headers=self.headers)
                soup = BeautifulSoup(html.text, 'html.parser')
                try:
                    grandparent = soup.find(class_='thrui').find_all('div')
                    for index in range(0, len(grandparent), 5):
                        # print(grandparent[index].text)
                        if index == len(grandparent) - 1:
                            continue
                        date_list.append(grandparent[index].text[:10])
                    for htmp in range(1, len(grandparent), 5):
                        tmp1_list.append(grandparent[htmp].text[:-1])
                    for ltmp in range(2, len(grandparent), 5):
                        tmp2_list.append(grandparent[ltmp].text[:-1])
                    for i in range(3, len(grandparent), 5):
                        weather_list.append(grandparent[i].text)
                    for j in range(4, len(grandparent), 5):
                        wind_list.append(grandparent[j].text)
                    print(year, month)
                except Exception as e:
                    print(e)
            data = {
                '日期': date_list,
                '最高气温': tmp1_list,
                '最低气温': tmp2_list,
                '天气': weather_list,
                '风向': wind_list,
            }

            df = pd.DataFrame(data)
            print(df.shape)
            filename = './data/data.csv'
            df.to_csv(filename, index=False, header=False)


if __name__ == '__main__':
    spider = WeatherSpider()
    spider.get_html()
