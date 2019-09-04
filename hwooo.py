# -*-coding: utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
import openpyxl
import time


#브라우저 버전에 맞게 driver설치 후 사용
#현재 페이지가 저장
driver = webdriver.Chrome("C:/Users/user/Desktop/jjj/chromedriver_win32/chromedriver")


#엑셀파일 생성
wb = openpyxl.Workbook()
#sheet는 현재 sheet해당
sheet = wb.active
wb.save('test3.xlsx')
totalDB = []

def insert_data_to_excel(crawling_result):
    check = False
    for i in totalDB:
        if i['title']==crawling_result['title']:
            check = True
            break

    if check == False:
        totalDB.append(crawling_result)
        sheet.append(list(crawling_result.values()))
        wb.save('test3.xlsx')

#크롤링
def crawling(driver):
    crawling_result = {'url' : None, 'title' : None, 'subTitle' : None, '지원대상' : None,'선정기준' : None, '지원내용' : None,'신청방법' : None}
    crawling_result['url'] = driver.current_url #현재 url 저장
    
    try:
        #xpath를 가진것 text형태로 결과물에 저장
        crawling_result['title'] = driver.find_element_by_xpath('//*[@id="contents"]/div[3]/div[1]/h3').text
        crawling_result['subTitle'] = driver.find_element_by_xpath('//*[@id="contents"]/div[3]/div[2]/table/tbody/tr/td[3]').text
        crawling_result['지원대상'] = driver.find_element_by_xpath('//*[@id="contents"]/div[3]/div[3]/table/tbody/tr[1]/td').text
        crawling_result['선정기준'] = driver.find_element_by_xpath('//*[@id="contents"]/div[3]/div[3]/table/tbody/tr[4]/td').text
        crawling_result['지원내용'] = driver.find_element_by_xpath('//*[@id="contents"]/div[3]/div[3]/table/tbody/tr[3]/td').text
        crawling_result['신청방법'] = driver.find_element_by_xpath('//*[@id="contents"]/div[3]/div[4]/table/tbody/tr[3]/td').text

    except:
        note = "asdf"
    #엑셀에 데이터 저장


    insert_data_to_excel(crawling_result)




def make_domain():
    #도메인 분석 저장

    for k in range(1,57):
        firstname = 'https://work.go.kr/empWelfareSrv/recommendSrv/recommendSrvSrchLifeCycle.do?service_all=on&sortOrdr=ASC&serviceCode=&sdetailCd=01%7C02%7C03%7C04%7C05&pageUnit=10&lifedetailCd=01%2C02%2C03%2C04%2C05&_csrf=b8f46f82-cd68-4aad-9231-ab700f8029e2&allchk=&beforeQuery=&serviceCodeText=&srchChkCnt=558&'
        secondname = 'pageIndex=%d'%k
        thirdname = "&searchQuery=&sortOrdrText="
        for i in range(2,12):
                driver.get(firstname+secondname+thirdname)
                sample = driver.find_element_by_xpath('//*[@id="selectFieldFrm"]/div[4]/table/tbody[%d]/tr/td[3]/a'%i)
                driver.execute_script("arguments[0].click();",sample)
                crawling(driver)

make_domain()
#driver및 엑셀 파일 종료
driver.close()
wb.close()
