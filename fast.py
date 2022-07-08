# coding:utf-8
import uvicorn
from fastapi import FastAPI, Form, Response
from fastapi.responses import HTMLResponse
from api.news_163.crawler import main as new

app = FastAPI()


def get_table(data, headers):
    table = ''
    width = len(headers)
    head_p = []
    for i in headers:
        head_p.append(":----:")
    if headers:
        table += '|' + '|'.join(headers) + '|' + '\n'
        table += "|" + '|'.join(head_p) + '|'
    else:
        table = ''
    num = 0
    for row in data:
        if num % width == 0:
            table += "\n|"
        table += row + "|"
        num += 1
    print(table)
    return table


@app.get("/")
def read_root():
    # 读取html
    with open("index.html", "r") as f:
        html = f.read()
    return HTMLResponse(html)


@app.post("/api/markdown_table")
def main(data: str = Form(...), headers: str = Form(...)):
    data = eval(data)
    headers = eval(headers)
    print("data:", data)
    print("headers:", headers)
    return get_table(data, headers)


@app.get("/163news")
def news(response: Response, index: int = 0, origin: str = 'zhihu', cache: str = 'null'):
    response.headers["Cache-Control"] = "max-age=86400, immutable, stale-while-revalidate"
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    response.headers["Access-Control-Allow-Origin"] = "*"
    return new(index, origin)


if __name__ == "__main__":
    uvicorn.run("fast:app", host="127.0.0.1", port=61, log_level="info")
