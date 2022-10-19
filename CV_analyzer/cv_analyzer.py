import docx2txt
#count vectorizer converts text to vectors
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

cv = CountVectorizer()

job_description = docx2txt.process('job_desc.docx')
resume = docx2txt.process('Gillani_ML.docx')
print(resume)

content = [job_description, resume]
matrix = cv.fit_transform(content)

similarity_matrix = cosine_similarity(matrix)
print(similarity_matrix)
x = str(similarity_matrix[1][0]*100)
x_round = round(float(x))
#print(x_round)
print('Resume matches by : '+ str(x_round)+ '  %')
