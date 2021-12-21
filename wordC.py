import pandas as pd
import wordcloud as wc
from wordcloud import STOPWORDS 
import os
import matplotlib.pyplot as plt
import csv

titles = []
body = []
#additional words to omit from cloud:
stop_words = ["NA", "NA NA","https"] + list(STOPWORDS)



directory = os.fsdecode('/Users/grantfinn/Library/Mobile Documents/com~apple~CloudDocs/UROP Research/Dump')
os.chdir(directory)
save_path = '/Users/grantfinn/Library/Mobile Documents/com~apple~CloudDocs/UROP Research/Clouds'
try:
     os.mkdir(save_path)
except:
     pass 

def concatenate_list_data(list):
    result= ''
    for element in list:
        result += str(element)
    return result

for file in os.listdir(directory):
     print(file)
     # filename = os.fsdecode(file)
     filename = file
     if filename.endswith(".csv"):
          # titles = str()
          # body = str()
          with open(filename, 'r', newline='', encoding='utf-8') as fh:
               # reader = csv.reader(fh, delimiter=',')
               reader = pd.read_csv(fh, low_memory=False)
               
               for row in reader.values:
                    try:
                         #titles.join(str(row[-2]))
                         titles.append(str(row[-2]))
                    except:
                         pass
                    try:
                         # body.join(str(row[-1]))
                         body.append(str(row[-1]))
                    except:
                         pass
               # try:
               #      titles = '\t'.join([i[-2] for i in reader])
               # except:
               #      pass
               # try:
               #      body = '\t'.join([j[-1] for j in reader])
               # except:
               #      pass

          
          save_token = ( '/' + filename[:-9] )

          T = concatenate_list_data(titles)
          B = concatenate_list_data(body)
          # print(titles)
          #WordCloud for just titles of posts
          wordcloudTitles = wc.WordCloud(stopwords = stop_words, width=800, height=400).generate(T)
          #Wordcloud for just body of posts
          wordcloudBody = wc.WordCloud(stopwords = stop_words, width=800, height=400).generate(B)


          #plt.imshow(wordcloudTitles, interpolation='bilinear')
          #plt.axis("off")
          #plt.show()

          # plt.imshow(wordcloudBody, interpolation='bilinear')
          # plt.axis("off")
          # plt.show()

          wordcloudTitles.to_file(save_path+save_token+'_Title.png')
          wordcloudBody.to_file(save_path+save_token+'_Body.png')
