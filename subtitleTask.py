import re
import codecs

arabicPattern = re.compile("[ء-ي]")
englishPattern = re.compile("[a-zA-Z]")

arabic =open('ar.srt', 'w', encoding='utf-8')
english =open('en.srt', 'w', encoding='utf-8')
with codecs.open('enar.srt', 'r','utf-8') as mix:
    for line in mix:
        if(arabicPattern.search(line)):
            arabic.write(line)
        elif(englishPattern.search(line)):
            english.write(line)
        else:
            english.write(line)
            arabic.write(line)

mix.close()
arabic.close()
english.close()
