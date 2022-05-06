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


data = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12","13"]
headers = ["a", "b", "c"]


get_table(data, headers)
