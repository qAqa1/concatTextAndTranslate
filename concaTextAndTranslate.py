delimiters = '.!?'

english_text_filename = 'english.txt'
translate_text_filename = 'translate.txt'
output_text_filename = 'output.csv'


def split_to_sentences(text):
    sentences = []
    last_sentence = ''
    for ch in text:
        last_sentence += ch
        if ch in delimiters:
            sentences.append(last_sentence.strip())
            last_sentence = ''
    return sentences


def read_sentences(path_to_text, text_name='Split text'):
    with open(path_to_text, 'r', encoding='utf8') as content_file:
        sentences = split_to_sentences(content_file.read())
        sentences_num = 1
        print(text_name + ':')
        for sentence in sentences:
            print(str(sentences_num) + ')', sentence)
            sentences_num += 1
        return sentences


english_sentences = read_sentences(english_text_filename, "English text")
print()
translate_sentences = read_sentences(translate_text_filename, "Translate")

if len(english_sentences) != len(translate_sentences):
    raise Exception('The number of sentences does not match!')

print()
print('Concat:')
csv_separator = ';'
concat_num = 0
result_text = ''
for english_sentence, translate_sentence in zip(english_sentences, translate_sentences):
    concat_num += 1
    print(str(concat_num) + ')', english_sentence, translate_sentence)
    result_text += '''"''' + english_sentence + '''"''' + csv_separator + '''"''' + translate_sentence + '''"''' + '\n'

result_text = result_text.strip()

with open(output_text_filename, 'w', encoding='cp1251') as output_file:
    output_file.write(result_text)
