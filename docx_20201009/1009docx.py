#coding: utf-8
# 替换word中数字
from docx import Document
from docx.shared import Inches


#创建 Document 对象，相当于打开一个 word 文档
doc = Document("20907.docx")


def replaceStr(old_text, new_text):
    for p in doc.paragraphs:
        if old_text in p.text:
            inline = p.runs
            for i in inline:
                if old_text in i.text:
                    text = i.text.replace(old_text, new_text)
                    i.text = text
                    
replaceStr("159308","234")

#保存文本
doc.save('20907.docx')



