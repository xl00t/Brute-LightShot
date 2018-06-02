import cfscrape
import threading
from itertools import product
import bs4 as BeautifulSoup
 
chars = ['abcdefghijklmnopqrstuvwxyz','bcdefghijklmnopqrstuvwxyza','cdefghijklmnopqrstuvwxyzab','defghijklmnopqrstuvwxyzabc','efghijklmnopqrstuvwxyzabcd','fghijklmnopqrstuvwxyzabcde','ghijklmnopqrstuvwxyzabcdef','hijklmnopqrstuvwxyzabcdefg','ijklmnopqrstuvwxyzabcdefgh','jklmnopqrstuvwxyzabcdefghi','klmnopqrstuvwxyzabcdefghij','lmnopqrstuvwxyzabcdefghijk','mnopqrstuvwxyzabcdefghijkl','nopqrstuvwxyzabcdefghijklm','opqrstuvwxyzabcdefghijklmn','pqrstuvwxyzabcdefghijklmno','qrstuvwxyzabcdefghijklmnop','rstuvwxyzabcdefghijklmnopq','stuvwxyzabcdefghijklmnopqr','tuvwxyzabcdefghijklmnopqrs','uvwxyzabcdefghijklmnopqrst','vwxyzabcdefghijklmnopqrstu','wxyzabcdefghijklmnopqrstuv','xyzabcdefghijklmnopqrstuvw','yzabcdefghijklmnopqrstuvwx','zabcdefghijklmnopqrstuvwxy']
 
def brute(chars):
        for length in range(6,7):
                to_attempt = product(chars, repeat=length)
                for attempt in to_attempt:
                        a = ''.join(attempt)
                        uri = "/"+str(a)
                        scraper = cfscrape.create_scraper()
                        r = scraper.get("http://prntscr.com/" + uri).content
                        soup = BeautifulSoup.BeautifulSoup(r, "html.parser")
                        x = soup.find('img')['src']
                        if x != "//st.prntscr.com/2018/02/28/0442/img/0_173a7b_211be8ff.png":
                                response = scraper.get(x)
                                with open("img/"+str(a)+".png", 'wb') as f:
                                        f.write(response.content)
                                        print(str(a)+".png")
                        else:
                                print(a+" | "+x)
for i in range(0,5):
    threading.Thread(target=brute,args=(chars[i],)).start()
