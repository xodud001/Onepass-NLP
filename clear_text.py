import util

cleared_text = []

test_data = util.csv_load('test_data.csv')

for text in test_data:
    cleared_text.append(util.clear_word(text))


util.array_to_csv(cleared_text, 'cleared_text.csv')

