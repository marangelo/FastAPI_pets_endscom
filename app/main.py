from fastapi import FastAPI, Path, Query
from fastapi.responses import HTMLResponse,JSONResponse
from pydantic import BaseModel,Field
from typing import Optional,List
fg


app = FastAPI()
app.title = "FastAPI GumaCorp"
app.version = "0.0.1"

class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=5, max_length=15)
    year: int = Field(le=2022,ge=2022)
    rating: float
    category: str = Field(min_length=5, max_length=15)

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "title": "Pelicula requerida",
                "year": 2001,
                "rating" : 5,
                "category": "Action"
            }
        }

movies= [
    {
        "id": 1,
        "title": "Fast and the Furious",
        "year": 2001,
        "rating" : 5,
        "category": "Action"
    },
    {
        "id": 2,
        "title": "Fast and the Furious 02",
        "year": 2001,
        "rating" : 5,
        "category": "Action"
    },
    {
        "id": 3,
        "title": "Fast and the Furious 03",
        "year": 2001,
        "rating" : 5,
        "category": "Action"
    }
]

@app.get("/", tags=["Home"])
def read_root():
    return HTMLResponse("<h1>Manos les Faltaran para pelarmela</h1>")

@app.get("/movies/", tags=["Movies"],response_model=List[Movie],status_code=200)
def get_movies() ->List[Movie]:
    return JSONResponse(status_code=200,content=movies)

@app.get("/movies/{movie_id}", tags=["Movies"],response_model=Movie,status_code=200)
def get_movie(movie_id: int = Path(ge=1, le=2000)) -> Movie:
    for movie in movies:
        if movie["id"] == movie_id:
            return JSONResponse(status_code=200,content=movies)
    return JSONResponse(status_code=404,content=[])
        
@app.get("/movies/", tags=["Movies"],response_model=List[Movie],status_code=200)
def get_movies_by_category(category: str = Query(min_length=5, max_length=15)) -> List[Movie]:
    data = [movie for movie in movies if movie["category"] == category]
    return JSONResponse(status_code=200,content=data)

@app.post("/movies/", tags=["Movies"],response_model=dict,status_code=201)
def create_movie(movie: Movie) -> dict:
    movies.append(movie)
    return JSONResponse(status_code=201,content={"message": "Movie created"})


@app.put("/movies/{movie_id}", tags=["Movies"],response_model=dict,status_code=200)
def update_movie(movie_id: int, movie: Movie) -> dict:
    for m in movies:
        if m["id"] == movie_id:
            m["id"] = movie.id
            m["title"] = movie.title
            m["year"] = movie.year
            m["rating"] = movie.rating
            m["category"] = movie.category
            return JSONResponse(content={"message": "Movie updated"})


@app.delete("/movies/{movie_id}", tags=["Movies"],response_model=dict,status_code=200)
def delete_movie(movie_id: int)-> dict:
    for movie in movies:
        if movie["id"] == movie_id:
            movies.remove(movie)
            return JSONResponse(status_code=200,content={"message": "Movie deleted"})


