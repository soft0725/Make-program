import requests
from bs4 import BeautifulSoup

# 이 코드는 부산의 날씨만 보여주는 프로그램 입니다.

html = requests.get('https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%B6%80%EC%82%B0+%EB%82%A0%EC%94%A8+&oquery=%EB%84%A4%EC%9D%B4%EB%B2%84+%EB%82%A0%EC%94%A8&tqi=hXLAzlprvh8ssT4EImlssssst9K-139142')

bs = BeautifulSoup(html.content, 'html.parser')

Search_data = bs.find('div',class_='temperature_text')

print(Search_data.get_text())