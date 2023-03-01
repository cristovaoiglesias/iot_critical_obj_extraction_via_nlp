import nltk
import pandas as pd

# df = pd.read_csv('./data/requirements.csv', sep=',')
#
# dataset = []
# for sentence in df['feature']:
#     tokens = nltk.word_tokenize(sentence)
#     tags = nltk.pos_tag(tokens)
#     for tag in tags:
#         if tag[1] in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']:
#             if tag[0] in {'be', 'is', 'i', '\'s', '\'re', '\'ve', '\'m'}:
#                 break
#             annotation = tag[0]
#             if annotation in ['get', 'play', 'have', 'make', 'keep', 'come', 'want', 'do', 'go', 'let', 'think',
#                               'getting', 'playing', 'having', 'making', 'keeping', 'coming', 'wanting', 'doing', 'going', 'letting', 'thinking',
#                               'gets', 'plays', 'has', 'makes', 'keeps', 'comes', 'wants', 'does', 'goes', 'lets', 'thinks',
#                               'got', 'played', 'had', 'made', 'kept', 'came', 'wanted', 'did', 'done', 'went', 'gone', 'thought']:
#                 break
#             entity = 'SERVICE'
#             index1 = sentence.find(annotation)
#             index2 = index1 + len(annotation)
#             print(tag[1], sentence[index1: index2])
#             dataset.append((entity, annotation, index1, index2, sentence))
#             break
#
# data = pd.DataFrame(columns=['entity', 'annotation', 'index1', 'index2', 'sentence'], data=dataset)
# data.to_csv('./data/dataset_service.csv', sep='|')
entity="Service"
df = pd.read_csv('dataset_service_filtered.csv', sep='|')
for ind in df.index:
     # print(df['entity'][ind], df['sentence'][ind])
     sentence=str(df['sentence'][ind]).replace('"',"'")
     print("(\""+sentence+"\",{\"entities\": [("+str(df['index1'][ind])+","+str(df['index2'][ind])+",\""+entity+"\")]}),")
     # print("('"+str(line.strip())+"',{'entities': [("+str(idx1)+","+str(idx2)+",'"+entity+"')]})")
