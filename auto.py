import os
import json

path = "sticker"  
base_url = "https://cdn1.tianli0.top/gh/tianli0/Sticker-Bochi/sticker/"  
icon_url_template = base_url + "{}"  

twikoo = {}  
data_valine = {} 
data_artalk = {}

file_list = [file for file in os.listdir(path) if file.endswith(".png")]

items_twikoo = []  
items_valine = []  
items_artalk = []  

# 遍历png文件
for file in file_list:
    icon = icon_url_template.format(file)
    text = file[:-4]

    items_twikoo.append({
        "icon": f"<img src=\"{icon}\">",
        "text": f"bochi-{text}"
    })

    data_valine[text] = icon

    items_artalk.append({
        "key": f"Strit-{text}",
        "val": icon
    })

twikoo["<img src=\"https://cdn1.tianli0.top/gh/tianli0/Sticker-Bochi/sticker/to.png\" style=\"width: 30px;top: 4px;position: relative;\" title=\"bochi\">"] = {
    "type": "image",
    "container": items_twikoo
}

data_valine = json.dumps(data_valine, indent=4, ensure_ascii=False)
data_artalk = {
    "name": "Strit",
    "type": "image",
    "items": items_artalk
}
data_artalk = json.dumps(data_artalk, indent=4, ensure_ascii=False)

with open("twikoo.json", "w", encoding="utf-8") as f:
    json.dump(twikoo, f, indent=4, ensure_ascii=False)
with open("valine.json", "w", encoding="utf-8") as f:
    f.write(data_valine)
with open("artalk.json", "w", encoding="utf-8") as f:
    f.write(data_artalk)

print("JSON文件生成成功！")
