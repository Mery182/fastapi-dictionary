from fastapi import FastAPI, HTTPException, Query
from typing import Optional, Dict
from pydantic import BaseModel, Field

app = FastAPI()

# Глоссарий
dictionary: Dict[int, Dict] = {
    1: {
        "term": "Vue.js",
        "definition": "Vue.js is an open-source model–view–viewmodel front end JavaScript framework for building user interfaces and single-page applications.",
        "priority": 1,
    },
    2: {
        "term": "API",
        "definition": "An application programming interface (API) is a connection between computers or between computer programs.",
        "priority": 2,
    },
    3: {
        "term": "WEB",
        "definition": "The World Wide Web (WWW or simply the Web) is an information system that enables content sharing over the Internet.",
        "priority": 1,
    },
}

# Pydantic модель для термина
class Term(BaseModel):
    term: str = Field(..., title="Term", description="The name of the term")
    definition: str = Field(..., title="Definition", description="The description of the term")
    priority: int = Field(..., gt=0, lt=4, title="Priority", description="Priority level (1-3)")
    relation: Optional[int] = Field(None, title="Relation", description="Related term ID, if any")
    author: Optional[str] = Field("mery182", title="Author", description="Author of the term")

# Получение списка всех терминов
@app.get("/terms", response_model=Dict[int, Term])
async def get_all_terms():
    """Returns all terms in the dictionary."""
    return dictionary

# Получение информации о конкретном термине по ID
@app.get("/terms/{term_id}", response_model=Term)
async def get_term_by_id(term_id: int):
    """Returns a specific term by its ID."""
    if term_id not in dictionary:
        raise HTTPException(status_code=404, detail="Term ID not found")
    return dictionary[term_id]

# Получение информации о термине по ключевому слову
@app.get("/terms/search")
async def search_term_by_keyword(keyword: str = Query(..., title="Keyword", description="Keyword to search for a term")):
    """Search for a term by keyword."""
    result = [value for value in dictionary.values() if keyword.lower() in value["term"].lower()]
    if not result:
        raise HTTPException(status_code=404, detail="No terms found with the given keyword")
    return result

# Добавление нового термина
@app.post("/terms/{term_id}", response_model=Term)
async def add_term(term_id: int, new_term: Term):
    """Adds a new term to the dictionary."""
    if term_id in dictionary:
        raise HTTPException(status_code=400, detail="Term ID already exists")
    dictionary[term_id] = new_term.dict()
    return dictionary[term_id]

# Обновление существующего термина
@app.put("/terms/{term_id}", response_model=Term)
async def update_term(term_id: int, updated_term: Term):
    """Updates an existing term by its ID."""
    if term_id not in dictionary:
        raise HTTPException(status_code=404, detail="Term ID not found")
    dictionary[term_id].update(updated_term.dict(exclude_unset=True))
    return dictionary[term_id]

# Удаление термина
@app.delete("/terms/{term_id}", response_model=dict)
async def delete_term(term_id: int):
    """Deletes a term from the dictionary."""
    if term_id not in dictionary:
        raise HTTPException(status_code=404, detail="Term ID not found")
    del dictionary[term_id]
    return {"message": f"Term with ID {term_id} deleted successfully"}


# uvicorn myapp:app --reload
# Посмотреть готовые api http://127.0.0.1:8000/docs
# def app(environ, start_response):

#         data = b"Hello, World!\n"
#         start_response("200 OK", [
#             ("Content-Type", "text/plain"),
#             ("Content-Length", str(len(data)))
#         ])
#         return iter([data])