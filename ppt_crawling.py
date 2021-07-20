from pptx import Presentation
import os
import re
import csv


# 훈련용 데이터 저장
x_train = []
y_train = []

# PPT 디렉토리 불러오기
root_dir = os.listdir('CCNA/work')

for i in range(len(root_dir)):
    sub_dir = os.listdir('CCNA/work/' + f'{root_dir[i]}')
    for j in range(len(sub_dir)):
        prs = Presentation(f'CCNA/work/{root_dir[i]}/{sub_dir[j]}')
        for slide in prs.slides:
            slide_text = []
            for shape in slide.shapes:
                if shape.has_text_frame:
                    for paragraph in shape.text_frame.paragraphs:
                        paragraph.text = re.sub(r"^\s+", "", paragraph.text.lower())
                        paragraph.text = paragraph.text.replace('\\xa0', ' ')
                        paragraph.text = paragraph.text.replace('\\x0', ' ')
                        paragraph.text = paragraph.text.replace('', ' ')
                        paragraph.text = paragraph.text.replace("//", '')
                        paragraph.text = re.sub(r"[^a-zA-Z0-9-]", " ", paragraph.text)
                        slide_text.append(paragraph.text)
                elif shape.has_table:
                    table = shape.table
                    for row_idx, row in enumerate(table.rows):
                        for col_idx, cell in enumerate(row.cells):
                            cell.text = re.sub(r"^\s+", "", cell.text.lower())
                            cell.text = cell.text.replace('\\xa0', ' ')
                            cell.text = cell.text.replace('\\x0', ' ')
                            cell.text = cell.text.replace('', ' ')
                            cell.text = cell.text.replace("///'", '')
                            cell.text = re.sub(r"[^a-zA-Z0-9-\\s]", " ", cell.text)
                            slide_text.append(cell.text)

            slide_text = [text for text in slide_text if len(text) > 1]
            slide_str = ''
            for text in slide_text:
                slide_str += text

            for phrase in phrases:
                slide_str = slide_str.replace(phrase, re.sub(' +', '-', phrase))
            x_train.append(slide_str)
            y_train.append(root_dir[i])

x_file = open('x_train.csv','w', newline='')
wr = csv.writer(x_file)
for x in x_train:
    wr.writerow([x])

y_file = open('y_train.csv','w', newline='')
wr = csv.writer(y_file)
for y in y_train:
    wr.writerow([y])

