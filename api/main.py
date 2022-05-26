from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

from load import load_sentences

import numpy

from fastapi import FastAPI
from pydantic import BaseModel

sentences, titles, backgrounds, sources = load_sentences()

model = SentenceTransformer('all-mpnet-base-v2')

sentence_embeddings = model.encode(sentences)

print(sentence_embeddings.shape)


class Search(BaseModel):
    query: str


app = FastAPI()


@app.post("/query")
async def search(search: Search):
    query_embedding = model.encode([search.query])
    similarities = cosine_similarity(
        query_embedding, sentence_embeddings).tolist()[0]
    sorted = numpy.argsort(similarities).tolist()[::-1]
    return [{'sentence': sentences[index],
             'similarities': similarities[index],
             'title': titles[index],
             'background': backgrounds[index],
             'source': sources[index]}
            for index in sorted[:5]]
