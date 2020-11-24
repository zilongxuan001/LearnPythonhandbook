# transDocx.py
#  更改肉菜周报的运维数据

from docx import Document
from docx.shared import Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
import re

document=Document(r"d:\ex\肉菜20907.doc")
paragraphs = document.paragraphs
text = re.sub('159308','235',paragraphs[18].text)
document.save()


ERROR: No matching distribution found for lxml>=2.3.2 (from python-docx)


