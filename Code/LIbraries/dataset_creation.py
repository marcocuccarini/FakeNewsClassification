
!pip install newspaper3k
nltk.download('punkt')

from newspaper import 
import pandas as pd
import nltk
import pandas as pd



# Extract from the MMCovid_datset all the link of text associated to italian lenguage
def readjsonMM(path, lenguage)
  cols = ['lang', 'fact_url', 'label']
  data = []
  file_name = path
  cont_error=0
  cont=0
  with open(file_name, encoding='latin-1') as f:
    for line in f:
      doc = json.loads(line)
      try:
        if doc['lang'] == lenguage:
          lst = [doc['fact_url'], doc['label']]
          data.append(lst)
      except KeyError:
        print(" ")
  return df = pd.DataFrame(data=data)

#Extarct the text, title, autor, etc. from the page article or blog.

def GetNewsFromLink(list_link, lang='it'):
  listTitolo=[]
  listTesto=[]
  listArgomento=[]
  listKeyWord=[]
  listAutore=[]
  listGiornale=[]
  listData=[]
  #per ogni url specificato nella lista
  for list in list_link:
    first_article = Article(url="%s" % list, language=lang)
    first_article.download()
    first_article.parse()
    first_article.nlp()

    #for article in cnn_paper.articles:
    # print(article.url)

    # Titolo articolo
    listTitolo.append(first_article.title)
  
    # Nome giornale preso dall'url
    
    titGiorn=list.split('.')
    listGiornale.append(titGiorn[1])
    

    # Categoria argomento preso dall'url
    titGiorn=list.split('/')
    if(titGiorn[3]=='news'):
      listArgomento.append(titGiorn[4])
    else:
      listArgomento.append(titGiorn[3])


    # Testo articolo
    listTesto.append(first_article.text)

    # Key word del esto dell'articolo
    listKeyWord.append(first_article.keywords)
    # Autore articolo
    listAutore.append(first_article.authors)
    # Data articolo
    listData.append(first_article.publish_date)


  df = pd.DataFrame()
  df['Testo']=listTesto
  df['keyword']=listKeyWord
  df['Giornale']=listGiornale
  df['Data']=listData
  df['Autore']=listAutore
  df['Titolo']=listTitolo
  

  return df 