# from typing import Union

# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()


# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer: Union[bool, None] = None


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}


# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_name": item.name, "item_id": item_id}

# import uvicorn
# from fastapi import FastAPI
# app = FastAPI()
# @app.get("/")
# async def index():
#    return {"message": "Hello World"}
# if __name__ == "__main__":
#    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

# from fastapi import FastAPI
# app = FastAPI()
# @app.get("/")
# async def index():
#     return {"message": "Hello World"}

# import uvicorn
# @app.get("/hello/{name}")
# # async def hello(name):
#     # return {"name": name}

# @app.get("/hello")
# async def hello(name: str, age:int):
#     return {"name": name, "age": age}

# from fastapi import Path
# async def hello(name:str=Path(...,min_length=3,
# max_length=10)):
#    return {"name": name}

# from fastapi import Query
# @app.get("/hello/{name}/{age}")
# async def hello(*, name: str=Path(..., min_length=3), max_length=10, \
#                 age: int = Path(..., ge=1, le=100), \
#                 percent: float=Query(..., ge=0, le=100)):
#     return {"name": name, "age": age}

# from typing import List
# from pydantic import BaseModel

# class Student(BaseModel):
#     id: int
#     name: str
#     subjects: List[str] = []

#     >>> data = {
#         'id': 1,
#         'name': 'Ravikumar',
#         'subjects': ["Eng", "Math", "Sci"],
#     }

# import uvicorn

# from fastapi import FastAPI

# from typing import List

# from pydantic import BaseModel, Field
# app = FastAPI()
# class Student(BaseModel):
#    id: int
#    name :str = Field(None, title="name of student", max_length=10)
#    subjects: List[str] = []
# @app.post("/students/")
# async def student_data(s1: Student):
#    return s1

# from fastapi.templating import Jinja2Templates
# from fastapi.responses import HTMLResponse
# from fastapi import FastAPI, Request
# app = FastAPI()
# templates = Jinja2Templates(directory="templates")
# @app.get("/hello/", response_class=HTMLResponse)
# async def hello(request: Request):
#    return templates.TemplateResponse("hello.html", {"request": request})


# from fastapi import FastAPI, Request
# from fastapi.responses import HTMLResponse
# from fastapi.templating import Jinja2Templates
# from fastapi.staticfiles import StaticFiles
# app = FastAPI()
# templates = Jinja2Templates(directory="templates")
# app.mount("/static", StaticFiles(directory="static"), name="static")
# @app.get("/hello/{name}", response_class=HTMLResponse)
# async def hello(request: Request, name:str):
#    return templates.TemplateResponse("hello.html", {"request": request, "name":name})

# from fastapi import FastAPI, Form
# app = FastAPI()
# async def submit(nm: str = Form(...), pwd: str = Form(...)):
#     return {"username": nm}
# from pydantic import BaseModel
# class User(BaseModel):
#     username: str
#     password: str
# @app.post("/submit/", response_model=User)
# async def submit(nm: str = Form(...), pwd: str = Form(...)):
#     return User(username=nm, password=pwd)

# from fastapi import FastAPI, File, UploadFile, Request
# import shutil
# from fastapi.responses import HTMLResponse
# from fastapi.templating import Jinja2Templates
# app = FastAPI()
# templates = Jinja2Templates(directory="templates")
# @app.get("/upload", response_class=HTMLResponse)
# async def upload(request: Request):
#     return templates.TemplateResponse("uploadfile.html", {"request": request})

# @app.post("/uploader")
# async def create_upload_file(file: UploadFile = File(...)):
#     with open("destination.png", "wb") as buffer:
#         shutil.copyfile(file.file, buffer)
#     return {"filename": file.filename}

# Cookie Parameters
# from fastapi import FastAPI
# from fastapi.responses import JSONResponse
# app = FastAPI()
# @app.post("/cookie/")
# def create_cookie():
#     content = {"message": "cookie set"}
#     response = JSONResponse(content=content)
#     response.set_cookie(key="username", value="admin")
#     return response

# @app.get("/readcookie")
# async def read_cookie(username: str = Cookie(None)):
#     return {"username": username}

# from fastapi import Optional
# from fastapi import FastAPI, Header
# app = FastAPI()
# @app.get("/headers/")
# async def read_header(accept_language: Optional[str] = Header(None)):
#     return {"Accept-Language": accept_language}

# def set_rsp_headers():
#     content = {"message": "Hello World"}
#     headers = {"X-Web-Framework": "FastAPI", "Content-Language": "en-US"}
#     return JSONResponse(content=content, headers=headers)

# from typing import List
# from fastapi import FastAPI
# from pydantic import BaseModel, Field
# app = FastAPI()
# class student(BaseModel):
#     id: int
#     name: str = Field(None, title="name of student", max_length=10)
#     marks: List[int] = []
#     percent_marks: float
# class percent(BaseModel):
#     id: int
#     name: str = Field(None, title="name of student", max_length=10)
#     percent_marks: float
# @app.post("/marks", response_model=percent)
# async def get_marks(s1:student):
#     s1.percent_marks = sum(s1.marks)/2
#     return s1
# from typing import Tuple
# from fastapi import FastAPI
# from pydantic import BaseModel
# app = FastAPI()
# class supplier(BaseModel):
#     supplierID: int
#     supplierName: str
# class product(BaseModel):
#     productID: int
#     prodname: str
#     price: int
#     supp: supplier
# class customer(BaseModel):
#     custID: int
#     custname: str
#     prod: Tuple[product]
# @app.post('/invoice')
# async def getInvoice(c1:customer):
#     return c1

# from fastapi import FastAPI
# app = FastAPI()
# @app.get("/user/")
# async def user(id: str, name: str, age: int):
#     return {"id": id, "name": name, "age": age}
# @app.get("/admin/")
# async def admin(id: str, name: str, age: int):
#     return {"id": id, "name": name, "age": age}
# @app.get("/user/")
# async def user(dep: dependency = Depends(dependency)):
#     return dep
# @app.get("/admin/")
# async def admin(dep: dependency = Depends(dependency)):
#     return dep
# async def validate(dep: dependency = Depends(dependency)):
#    if dep.age > 18:
#       raise HTTPException(status_code=400, detail="You are not eligible")
# @app.get("/user/", dependencies=[Depends(validate)])
# async def user():
#    return {"message": "You are eligible"}

# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# app = FastAPI()
# origins = [
#     "https"://192.168.211.8000",
#     "http://localhost",
#     "http://localhost:8080",
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins = origins, 
#     allow_credentials = True,
#     allow_methods=["*"]
# )

# @app.get("/")
# async def main():
#    return {"message": "Hello World"}

from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

ALPHA_VANTAGE_API_KEY = "4CB4EU4HMKRT2KP2"
ALPHA_VANTAGE_BASE_URL = "https://www.alphavantage.co/query"


@app.get("/stock/quote/SBIN")
async def get_stock_quote(symbol: str):
    params = {
        "function": "GLOBAL_QUOTE",
        "symbol": symbol,
        "apikey": ALPHA_VANTAGE_API_KEY
    }
    response = requests.get(ALPHA_VANTAGE_BASE_URL, params=params)
    data = response.json()
    if "Global Quote" not in data:
        raise HTTPException(status_code=404, detail="Stock symbol not found")
    return data["Global Quote"]


@app.get("/stock/history/SBIN")
async def get_stock_history(symbol: str, interval: str = "daily", outputsize: str = "compact"):
    params = {
        "function": "TIME_SERIES_INTRADAY" if interval == "intraday" else "TIME_SERIES_DAILY",
        "symbol": symbol,
        "interval": interval,
        "outputsize": outputsize,
        "apikey": ALPHA_VANTAGE_API_KEY
    }
    response = requests.get(ALPHA_VANTAGE_BASE_URL, params=params)
    data = response.json()
    if "Time Series (Daily)" not in data and "Time Series (" + interval.capitalize() + ")" not in data:
        raise HTTPException(status_code=404, detail="Stock symbol not found or invalid interval")
    return data


@app.get("/stock/company/SBIN")
async def get_company_info(symbol: str):
    params = {
        "function": "OVERVIEW",
        "symbol": symbol,
        "apikey": ALPHA_VANTAGE_API_KEY
    }
    response = requests.get(ALPHA_VANTAGE_BASE_URL, params=params)
    data = response.json()
    if not data:
        raise HTTPException(status_code=404, detail="Company information not found")
    return data

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
