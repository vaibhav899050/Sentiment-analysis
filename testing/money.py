import requests
from bs4 import BeautifulSoup
import pandas
import csv
import subprocess
import os
from googletrans import Translator

# Define the URL to scrape

url_2024 = ["https://www.moneycontrol.com/company-article/larsentoubro/news/LT",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=2&next=0&durationType=M&Year=&duration=6&news_type="]

url_2023 = ["https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&durationType=Y&Year=2023",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=2&next=0&durationType=Y&Year=2023&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=3&next=0&durationType=Y&Year=2023&duration=1&news_type="]

url_2022 = ["https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&durationType=Y&Year=2022",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=2&next=0&durationType=Y&Year=2022&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=3&next=0&durationType=Y&Year=2022&duration=1&news_type=",
            ]

url_2021 = ["https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&durationType=Y&Year=2021",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=2&next=0&durationType=Y&Year=2021&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=3&next=0&durationType=Y&Year=2021&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=4&next=0&durationType=Y&Year=2021&duration=1&news_type=",
            ]

url_2020 = ["https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&durationType=Y&Year=2020",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=2&next=0&durationType=Y&Year=2020&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=3&next=0&durationType=Y&Year=2020&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=4&next=0&durationType=Y&Year=2020&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=5&next=0&durationType=Y&Year=2020&duration=1&news_type="]

url_2019 = ["https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&durationType=Y&Year=2019",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=2&next=0&durationType=Y&Year=2019&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=3&next=0&durationType=Y&Year=2019&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=4&next=0&durationType=Y&Year=2019&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=5&next=0&durationType=Y&Year=2019&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=6&next=0&durationType=Y&Year=2019&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=7&next=0&durationType=Y&Year=2019&duration=1&news_type="]

url_2018 = ["https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&durationType=Y&Year=2018",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=2&next=0&durationType=Y&Year=2018&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=3&next=0&durationType=Y&Year=2018&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=4&next=0&durationType=Y&Year=2018&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=5&next=0&durationType=Y&Year=2018&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=6&next=0&durationType=Y&Year=2018&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=7&next=0&durationType=Y&Year=2018&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=8&next=0&durationType=Y&Year=2018&duration=1&news_type="]

url_2017 = ["https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&durationType=Y&Year=2017",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=2&next=0&durationType=Y&Year=2017&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=3&next=0&durationType=Y&Year=2017&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=4&next=0&durationType=Y&Year=2017&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=5&next=0&durationType=Y&Year=2017&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=8&next=0&durationType=Y&Year=2017&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=9&next=0&durationType=Y&Year=2017&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=10&next=0&durationType=Y&Year=2017&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&pageno=11&next=1&durationType=Y&Year=2017&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=12&next=1&durationType=Y&Year=2017&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=13&next=1&durationType=Y&Year=2017&duration=1&news_type=",
            ]

url_2016 = ["https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&durationType=Y&Year=2016",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=2&next=0&durationType=Y&Year=2016&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=3&next=0&durationType=Y&Year=2016&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=4&next=0&durationType=Y&Year=2016&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=5&next=0&durationType=Y&Year=2016&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=6&next=0&durationType=Y&Year=2016&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=7&next=0&durationType=Y&Year=2016&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=8&next=0&durationType=Y&Year=2016&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=9&next=0&durationType=Y&Year=2016&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=10&next=0&durationType=Y&Year=2016&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&pageno=11&next=1&durationType=Y&Year=2016&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=12&next=1&durationType=Y&Year=2016&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=13&next=1&durationType=Y&Year=2016&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=14&next=1&durationType=Y&Year=2016&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=15&next=1&durationType=Y&Year=2016&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=16&next=1&durationType=Y&Year=2016&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=17&next=1&durationType=Y&Year=2016&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=18&next=1&durationType=Y&Year=2016&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=19&next=1&durationType=Y&Year=2016&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=20&next=1&durationType=Y&Year=2016&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&pageno=21&next=2&durationType=Y&Year=2016&duration=1&news_type="]

url_2015 = ["https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&durationType=Y&Year=2015",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=2&next=0&durationType=Y&Year=2015&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=3&next=0&durationType=Y&Year=2015&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=4&next=0&durationType=Y&Year=2015&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=5&next=0&durationType=Y&Year=2015&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=6&next=0&durationType=Y&Year=2015&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=7&next=0&durationType=Y&Year=2015&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=8&next=0&durationType=Y&Year=2015&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=9&next=0&durationType=Y&Year=2015&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=10&next=0&durationType=Y&Year=2015&duration=1&news_type=",
            ]

url_2014 = ["https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&durationType=Y&Year=2014",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=2&next=0&durationType=Y&Year=2014&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=3&next=0&durationType=Y&Year=2014&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=4&next=0&durationType=Y&Year=2014&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=5&next=0&durationType=Y&Year=2014&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=6&next=0&durationType=Y&Year=2014&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=7&next=0&durationType=Y&Year=2014&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=8&next=0&durationType=Y&Year=2014&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=9&next=0&durationType=Y&Year=2014&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=10&next=0&durationType=Y&Year=2014&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&pageno=11&next=1&durationType=Y&Year=2014&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=12&next=1&durationType=Y&Year=2014&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=13&next=1&durationType=Y&Year=2014&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=14&next=1&durationType=Y&Year=2014&duration=1&news_type="]

url_2013 = ["https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&durationType=Y&Year=2013",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=2&next=0&durationType=Y&Year=2013&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=3&next=0&durationType=Y&Year=2013&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=4&next=0&durationType=Y&Year=2013&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=5&next=0&durationType=Y&Year=2013&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=6&next=0&durationType=Y&Year=2013&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=7&next=0&durationType=Y&Year=2013&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=8&next=0&durationType=Y&Year=2013&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=9&next=0&durationType=Y&Year=2013&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=10&next=0&durationType=Y&Year=2013&duration=1&news_type=",
            ]

url_2012 = ["https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&durationType=Y&Year=2012",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=2&next=0&durationType=Y&Year=2012&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=3&next=0&durationType=Y&Year=2012&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=4&next=0&durationType=Y&Year=2012&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=5&next=0&durationType=Y&Year=2012&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=6&next=0&durationType=Y&Year=2012&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=7&next=0&durationType=Y&Year=2012&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=8&next=0&durationType=Y&Year=2012&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=9&next=0&durationType=Y&Year=2012&duration=1&news_type=",
            "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=10&next=0&durationType=Y&Year=2012&duration=1&news_type="]

url_combined = ["https://www.moneycontrol.com/company-article/larsentoubro/news/LT",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=2&next=0&durationType=M&Year=&duration=6&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&durationType=Y&Year=2023",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=2&next=0&durationType=Y&Year=2023&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=3&next=0&durationType=Y&Year=2023&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&durationType=Y&Year=2022",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=2&next=0&durationType=Y&Year=2022&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=3&next=0&durationType=Y&Year=2022&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&durationType=Y&Year=2021",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=2&next=0&durationType=Y&Year=2021&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=3&next=0&durationType=Y&Year=2021&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=4&next=0&durationType=Y&Year=2021&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&durationType=Y&Year=2020",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=2&next=0&durationType=Y&Year=2020&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=3&next=0&durationType=Y&Year=2020&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=4&next=0&durationType=Y&Year=2020&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=5&next=0&durationType=Y&Year=2020&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&durationType=Y&Year=2019",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=2&next=0&durationType=Y&Year=2019&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=3&next=0&durationType=Y&Year=2019&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=4&next=0&durationType=Y&Year=2019&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=5&next=0&durationType=Y&Year=2019&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=6&next=0&durationType=Y&Year=2019&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=7&next=0&durationType=Y&Year=2019&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&durationType=Y&Year=2018",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=2&next=0&durationType=Y&Year=2018&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=3&next=0&durationType=Y&Year=2018&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=4&next=0&durationType=Y&Year=2018&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=5&next=0&durationType=Y&Year=2018&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=6&next=0&durationType=Y&Year=2018&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=7&next=0&durationType=Y&Year=2018&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=8&next=0&durationType=Y&Year=2018&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&durationType=Y&Year=2017",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=2&next=0&durationType=Y&Year=2017&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=3&next=0&durationType=Y&Year=2017&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=4&next=0&durationType=Y&Year=2017&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=5&next=0&durationType=Y&Year=2017&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=8&next=0&durationType=Y&Year=2017&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&durationType=Y&Year=2016",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=2&next=0&durationType=Y&Year=2016&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=3&next=0&durationType=Y&Year=2016&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=4&next=0&durationType=Y&Year=2016&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=5&next=0&durationType=Y&Year=2016&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=6&next=0&durationType=Y&Year=2016&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=7&next=0&durationType=Y&Year=2016&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=8&next=0&durationType=Y&Year=2016&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=9&next=0&durationType=Y&Year=2016&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=10&next=0&durationType=Y&Year=2016&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&pageno=11&next=1&durationType=Y&Year=2016&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=12&next=1&durationType=Y&Year=2016&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=13&next=1&durationType=Y&Year=2016&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=14&next=1&durationType=Y&Year=2016&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=15&next=1&durationType=Y&Year=2016&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=16&next=1&durationType=Y&Year=2016&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=17&next=1&durationType=Y&Year=2016&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=18&next=1&durationType=Y&Year=2016&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=19&next=1&durationType=Y&Year=2016&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=20&next=1&durationType=Y&Year=2016&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&pageno=21&next=2&durationType=Y&Year=2016&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&durationType=Y&Year=2015",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=2&next=0&durationType=Y&Year=2015&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=3&next=0&durationType=Y&Year=2015&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=4&next=0&durationType=Y&Year=2015&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=5&next=0&durationType=Y&Year=2015&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=6&next=0&durationType=Y&Year=2015&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=7&next=0&durationType=Y&Year=2015&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=8&next=0&durationType=Y&Year=2015&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=9&next=0&durationType=Y&Year=2015&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=10&next=0&durationType=Y&Year=2015&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&durationType=Y&Year=2014",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=2&next=0&durationType=Y&Year=2014&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=3&next=0&durationType=Y&Year=2014&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=4&next=0&durationType=Y&Year=2014&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=5&next=0&durationType=Y&Year=2014&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=6&next=0&durationType=Y&Year=2014&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=7&next=0&durationType=Y&Year=2014&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=8&next=0&durationType=Y&Year=2014&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=9&next=0&durationType=Y&Year=2014&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=10&next=0&durationType=Y&Year=2014&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&pageno=11&next=1&durationType=Y&Year=2014&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=12&next=1&durationType=Y&Year=2014&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=13&next=1&durationType=Y&Year=2014&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=14&next=1&durationType=Y&Year=2014&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&durationType=Y&Year=2013",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=2&next=0&durationType=Y&Year=2013&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=3&next=0&durationType=Y&Year=2013&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=4&next=0&durationType=Y&Year=2013&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=5&next=0&durationType=Y&Year=2013&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=6&next=0&durationType=Y&Year=2013&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=7&next=0&durationType=Y&Year=2013&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=8&next=0&durationType=Y&Year=2013&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=9&next=0&durationType=Y&Year=2013&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=10&next=0&durationType=Y&Year=2013&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&durationType=Y&Year=2012",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=2&next=0&durationType=Y&Year=2012&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=3&next=0&durationType=Y&Year=2012&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=4&next=0&durationType=Y&Year=2012&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=5&next=0&durationType=Y&Year=2012&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=6&next=0&durationType=Y&Year=2012&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=7&next=0&durationType=Y&Year=2012&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=8&next=0&durationType=Y&Year=2012&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=9&next=0&durationType=Y&Year=2012&duration=1&news_type=",
                "https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=LT&scat=&pageno=10&next=0&durationType=Y&Year=2012&duration=1&news_type="
                ]

Final_news1 = []
Final_news2 = []

Time_stamp1 = []
Time_stamp2 = []
Time_Stamp = []

print("Data Scraping in progress .... ")

for url in url_combined:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    nifty50 = soup.find_all("a", class_="g_14bl")
    sensex = soup.find_all("p", class_="PT3")

    for l in range(len(nifty50)):
        str1 = nifty50[l].text
        Final_news1.append(str1)

    for l1 in range(len(sensex)):
        if l1 % 2 != 0:
            str2 = sensex[l1].text
            Final_news2.append(str2)
        else:
            str3 = sensex[l1].text
            #  Time_stamp1.append(str3)
            #  Time_stamp2.append(str3)
            Time_Stamp.append(str3)

# print(len(Final_news1))
# print(len(Final_news2))


Final_news = []
x = len(Final_news1)

for i in range(x):
    Final_news.append(Final_news1[i])
    Final_news.append(Final_news2[i])

# print(len(Final_news))

print(len(Final_news))
print(len(Time_Stamp))

Final_Final_news = []
Final_Final_time = []

print("\n\n")

file_path = "news.csv"

dummy = set()

for i in range(x):
    string = Final_news[i]

    if string not in dummy:
        Final_Final_news.append(string)
        Final_Final_time.append(Time_Stamp[i // 2])
        dummy.add(string)

# print(len(Final_Final_news))
# print((Final_Final_time))


new_Time_Stamp = [timestamp.split("|")[1].strip() for timestamp in Final_Final_time]

with open(file_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Content', 'Timestamp'])  # Writing header row
    for string, timestamp in zip(Final_Final_news, new_Time_Stamp):
        writer.writerow([string, timestamp])

print("Scraped Succesfully")
print('Translation in progress...')

# # df = pandas.read_csv(file_path)
# # translator = Translator()
# # def translate_to_english(text):
# #     translation = translator.translate(text, dest='en')
# #     return translation.text

# # df['Content'] = df['Content'].apply(translate_to_english)
# # df.to_csv('Scraped-news/translated_file.csv', index=False)
# print("Translated Succesfully...")


print(f"CSV file saved successfully at: {file_path}")