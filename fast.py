# coding:utf-8
import uvicorn
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI(docs_url=None, redoc_url=None)


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


@app.post("/api/markdown_table")
def main(data: str = Form(...), headers: str = Form(...)):
    data = eval(data)
    headers = eval(headers)
    print("data:", data)
    print("headers:", headers)
    return get_table(data, headers)


if __name__ == "__main__":
    uvicorn.run("fast:app", host="127.0.0.1", port=61, log_level="info")
