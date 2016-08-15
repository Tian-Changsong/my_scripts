#encoding: utf-8
from selenium import webdriver
from bs4 import BeautifulSoup
import time
c = webdriver.Ie()
c.get('http://ehr.spreadtrum.com/spreadtrum_hr/loginx.aspx')

c.switch_to.frame("head")# frame id or name
want = c.find_element_by_link_text("考勤信息")
want.click()
if len(c.window_handles) == 1:
    oriWindow = c.window_handles
c.switch_to.parent_frame()
c.switch_to.frame("cnt")
c.switch_to.frame('Links')
kaoqin=c.find_element_by_id("101")
kaoqin.click()
time.sleep(1)
oriWindow = c.window_handles[0]
newWindow = c.window_handles[1] if c.window_handles[0] == oriWindow else c.window_handles[0]
c.switch_to.window(newWindow)
c.switch_to.frame('ifrm')
okButton=c.find_element_by_name('btnOK')
okButton.click()
c.switch_to.window(oriWindow)
c.switch_to.frame("cnt")
c.switch_to.frame('detail')
pageContent = BeautifulSoup(c.page_source, "html.parser")
tableHeaders = [i.contents[0].contents[0] for i in pageContent.find_all("th")]
tableData = [i.contents[0] for i in pageContent.find_all("td", attrs={"class":"selected"})]
tableData.remove(tableData[0])
for i in range(len(tableHeaders)):
    if tableHeaders[i] == u'考勤异常':
        continue
    print "%s: %s" % (tableHeaders[i], tableData[i])


