# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
from fake_useragent import UserAgent
from scrapy import signals

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapy.http import HtmlResponse
import time



class TestMiddleware():

    def process_request(self, request, spider):
        request.meta['proxy'] = 'http://110.189.152.86:31061'
        return None


class Test2Middleware():

    def process_request(self, request, spider):
        # 设置代理User-Agent参数
        ua = UserAgent()
        request.headers.setdefault('user_agent', ua.random)
        return None


class SeleniumMiddleware():
    def __init__(self, timeout=None, service_args=[]):
        self.timeout = timeout
        chromeOptions = webdriver.ChromeOptions()
        # chromeOptions.add_argument("--proxy-server=%s" % request.meta["proxy"])

        self.browser = webdriver.Chrome('/home/waving/chrome/chromedriver', chrome_options=chromeOptions)
        self.browser.set_window_size(1400, 700)
        self.wait = WebDriverWait(self.browser, self.timeout)

    # def __del__(self):
    #     self.browser.close()

    def process_request(self, request, spider):
        """
        抓取页面
        :param request: Request对象
        :param spider: Spider对象
        :return: HtmlResponse
        """
        try:
            self.browser.get(request.url)
            self.browser.execute_script('window.scrollTo(0, document.body.scrollHeight / 8)')

            time.sleep(2)
            self.browser.execute_script('window.scrollTo(0, 2 * document.body.scrollHeight / 8)')
            time.sleep(2)

            self.browser.execute_script('window.scrollTo(0, 3 * document.body.scrollHeight / 8)')
            time.sleep(2)

            self.browser.execute_script('window.scrollTo(0, 4 * document.body.scrollHeight / 8)')
            time.sleep(2)

            self.browser.execute_script('window.scrollTo(0, 5 * document.body.scrollHeight / 8)')
            time.sleep(2)

            self.browser.execute_script('window.scrollTo(0, 6 * document.body.scrollHeight / 8)')
            time.sleep(2)

            self.browser.execute_script('window.scrollTo(0, 7 * document.body.scrollHeight / 8)')
            time.sleep(2)
            self.browser.execute_script('window.scrollTo(0, 8 * document.body.scrollHeight / 8)')

            return HtmlResponse(url=request.url, body=self.browser.page_source, request=request, encoding='utf-8',
                                status=200)
        except TimeoutException:
            return HtmlResponse(url=request.url, status=500, request=request)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(timeout=crawler.settings.get('SELENIUM_TIMEOUT'))
