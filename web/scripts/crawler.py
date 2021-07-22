from bs4 import BeautifulSoup
import requests
from sitetop.models import todays
import datetime

# 쇼핑몰 탑 100 주소들
gmarketadd = requests.get("http://corners.gmarket.co.kr/BestSellers?viewType=C&largeCategoryCode=100000035")
naveradd = requests.get("https://search.shopping.naver.com/best100v2/detail.nhn?catId=50000138")
auctionadd = requests.get("http://corners.auction.co.kr/corner/categorybest.aspx?category=32000000")
elevenstadd = requests.get("https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&cornerNo=6&dispCtgrNo=1001357#pageNum%%5")
# 11번가는 top500임
sggadd = requests.get("http://www.ssg.com/disp/category.ssg?dispCtgId=6000161221&sort=sale&pageSize=100")

# 아동복 상위 브랜드
# 아가방
agabangpp = requests.get("https://www.agabangmall.com/goods/goods_list.php?page={}&cateCd=017001&pageNum=20&sort=sellcnt")
#모이몰른
moimolnpp = requests.get("http://mall.istyle24.com/Brand/Index/20010964?depth=3")
#오가닉맘
orgamicmampp = requests.get("https://organicmommall.co.kr")
#블루독 모르겠다.... 같은이름이 너무많아 어쩌지

#밍크뮤
minkmuipp = requests.get("http://www.thesymall.com/minkmui")

#뉴발
nbkidpp = requests.get("https://www.nbkorea.com/product/featuredList.action?cateGrpCode=250100&cIdx=1387")

#밀리밤 도 카테고리별로 나뉘어서 어떻게해야할지?

gmarketpp = BeautifulSoup(gmarketadd.text, features="html.parser")
naverpp = BeautifulSoup(naveradd.text, features="html.parser")
auctionpp = BeautifulSoup(auctionadd.text, features="html.parser")
elevenstpp = BeautifulSoup(elevenstadd.text, features="html.parser")
sggpp = BeautifulSoup(sggadd.text, features="html.parser")

day = datetime.datetime.now().date()
day_str = day.strftime('%Y-%m-%d')

def run():
    n=1
    for gmarket in gmarketpp.find_all("li"):
        try:
            gmarkettitle = gmarket.find("a", class_="itemname").text
            gmarketrank = gmarket.find("p").text
            rankclass = "no{}"
            rankclass2 = rankclass.format(n)
            rank = gmarket.find("p", class_=rankclass2).text
            n += 1
            # print("gmarket:",gmarkettitle, gmarketrank)
            if('[' in gmarkettitle):
                gmarketbrand = gmarkettitle.split('[')
                gmarketbrand = gmarketbrand[1]
                gmarketbrand = gmarketbrand.split(']')
                gmarketbrand = gmarketbrand[0]
            else:
                gmarketbrand = ""
            todays(category="gmarket", title=gmarkettitle, brand=gmarketbrand, today=day_str).save()
        except Exception as e:
            continue

    for naver in naverpp.find_all("li", class_="_itemSection"):
        try:
            navertitle = naver.find("a").get("title")
            # print("naver:",navertitle)
            if(' ' in navertitle):
                naverbrand = navertitle.split(' ')
                naverbrand = naverbrand[0]
            else:
                naverbrand = ""
            todays(category="naver", title=navertitle, brand=naverbrand, today=day_str).save()
        except Exception as e:
            continue

    for auction in auctionpp.find_all("div", class_="img-list"):
        try:
            auctiontitle = auction.find("em").text
            # print("auction:",auctiontitle)
            if('[' in auctiontitle):
                auctionbrand = auctiontitle.split('[')
                auctionbrand = auctionbrand[1]
                auctionbrand = auctionbrand.split(']')
                auctionbrand = auctionbrand[0]
            else:
                auctionbrand = ""
            todays(category="auction", title=auctiontitle, brand=auctionbrand, today=day_str).save()
        except Exception as e:
            continue

    for elevenst in elevenstpp.find_all("div", class_="ranking_pd"):
        try:
            if(int(elevenst.find("span",class_="best").text)<=100):
                elevensttitle = elevenst.find("p").text
            if('[' in elevensttitle):
                elevenstbrand = elevensttitle.split('[')
                elevenstbrand = elevenstbrand[1]
                elevenstbrand = elevenstbrand.split(']')
                elevenstbrand = elevenstbrand[0]
            else:
                elevenstbrand = ""
                # print("elevenst:",elevensttitle, elevenst.find("span",class_="best").text)
            todays(category="elevenst", title=elevensttitle, brand=elevenstbrand, today=day_str).save()
        except Exception as e:
            continue

    for sgg in sggpp.find_all("div", class_="title"):
        try:
            sggtitle = sgg.find("a", class_="clickable").get("data-react-tarea")
            sggtitle = sggtitle[17:]
            sggbrand = sgg.find("em").text
            todays(category="sgg", title=sggtitle, brand=sggbrand, today=day_str).save()
            print("sgg:", sggtitle)
        except Exception as e:
            continue

