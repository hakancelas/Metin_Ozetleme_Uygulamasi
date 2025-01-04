# Gerekli kütüphanelerin içe aktarılması
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer
import nltk

# NLTK için stopwords verisini indirme (ilk defa çalıştırıldığında)
nltk.download('stopwords')

# Kullanıcıdan metin alma
print("Lütfen özetlenmesini istediğiniz metni girin (Çıkmak için 'q' tuşuna basabilirsiniz):")
text = ""

# Kullanıcıdan metin alınması
while True:
    line = input()
    if line == 'q':
        break
    text += line + "\n"

# Metni özetlemek için TextRank algoritması kullanma
parser = PlaintextParser.from_string(text, Tokenizer())
summarizer = TextRankSummarizer()

# 3 cümlelik bir özet alma
summary = summarizer(parser.document, 3)  # 3 cümleli bir özet almak için

# Özetin yazdırılması
print("\nMetnin özeti:")
for sentence in summary:
    print(sentence)