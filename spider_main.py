import html_downloader, html_outputer, html_parser, url_manager
import urllib.parse
import xlrd
import urllib

data = xlrd.open_workbook('example.xlsx')
table = data.sheets()[0]
nrows = table.nrows
wordlist = []

for i in range(nrows):
	if i==0:
		continue
	wordlist.append(table.row_values(i))

#list1 = ['苦茶','花乳花','槚','茶','茗','莈']
list2 = []
for i in range(len(wordlist)):
	list2.append(urllib.parse.quote(wordlist[i][0]))

class SpiderMain(object):
	def __init__(self):

        # url管理器
		self.urls = url_manager.UrlManager()

        # 下载器
		self.downloader = html_downloader.HtmlDownloader()

        # 解析器
		self.parser = html_parser.HtmlParser()

		# 输出器
		self.outputer = html_outputer.HtmlOutputer()
	def craw(self):
		i=0
		while i < len(list2): 
			try: 
			
				new_url = 'https://baike.baidu.com/item/%s' % (list2[i])
				
		
		# 启动下载器下载页面
				html_cont = self.downloader.download(new_url)

                # 启动解析器将新的url和爬到的数据进行保存
				new_urls, new_data = self.parser.parse(new_url, html_cont)
	
					# 将新的url添加
				self.urls.add_new_urls(new_urls)

                # 收集爬取数据
				self.outputer.collect_data(new_data)
				i +=1
				print('successfully craw %s' %(wordlist[i][0]))
			except :
				print('craw failed')
				i+=1
			
		self.outputer.output_html()
		
if __name__ == '__main__':
	obj_spider = SpiderMain()
	obj_spider.craw()