import requests
from bs4 import BeautifulSoup
from .models import Meaning

dict = {
    'noun': 'n',
    'pronoun': 'pron',
    'verb': 'v',
    'auxiliary verb': 'aux',
    'adjective': 'adj',
    'adverb': 'adv',
    'preposition': 'prep',
    'conjunction': 'conj',
    'exclamation': 'int',
}

def fetchMeaning(word, Voc):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}
    word = word.strip()
    url = f"https://dictionary.cambridge.org/zht/%E8%A9%9E%E5%85%B8/%E8%8B%B1%E8%AA%9E-%E6%BC%A2%E8%AA%9E-%E7%B9%81%E9%AB%94/{word}"
    r = requests.get(url, headers=headers) #將此頁面的HTML GET下來

    if(r.status_code == requests.codes.ok):
        soup = BeautifulSoup(r.text,"html.parser") #將網頁資料以html.parser
        
        div = soup.find_all(class_="pr entry-body__el")
        if div:
            for tag in div:
                speech_tag = tag.find(class_="pos dpos")
                if speech_tag and dict.get(speech_tag.text):
                    speech = dict.get(speech_tag.text)
                    sel = tag.find_all(class_="trans dtrans dtrans-se break-cj")
                    for x in sel:
                        next_node = x.find_next_siblings("div")
                        chinese = x.text
                        if next_node:
                            try:
                                chinese_sentences = next_node[0].find("span",class_="trans dtrans dtrans-se hdb break-cj").text
                                english_sentences = next_node[0].find("span",class_="eg deg").text
                            except AttributeError:
                                continue
                        try:
                            Mean = Meaning(chinese = chinese, chinese_sentences = chinese_sentences, english_sentences = english_sentences, speech = speech, vocabulary = Voc)
                            Mean.save()
                        except UnboundLocalError:
                            return "Could not find the sentence of word"
            return "success"
        else:
            return "Could not find the meaning of word"
    else:
        return "Could not connect to dictionary"
