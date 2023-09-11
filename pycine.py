from fastapi import FastAPI
from tmdb import get_json

app = FastAPI()

@app.get("/artista/{name}") 
def get_artista(name: str):

    data=get_json("https://api.themoviedb.org/3/search/person",f"?query={name}")

    results = data['results']

    filtro=[]

    for artista in results:
        filtro.append({
            'id': artista['id'],
            'name': artista['name'],
            'popularity': artista['popularity']
        })

    return filtro,results

@app.get("/filme/{title}") 
async def find_movie(title: str):

    return {"title":title}

@app.get("/artista/filmes") 
async def find_filmes_artista(personId: int):

    data = get_json(f"https://api.themoviedb.org/3/person/{personId}/movie_credits")

    results = data['cast']

    return results