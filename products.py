
#3.檢查檔案是否存在
import os #作業系統(operating system)

products = []
if os.path.isfile("products.csv"):
    print("Yeah~找到檔案了!")
    #將讀取檔案的程式碼放到這裡執行
    with open("products.csv", "r", encoding="Big5") as f:
        for line in f:
            if "商品,價格" in line:
                continue #如果line裡面出現"商品，價格"，則不執行這次的迴圈，重新執行下次的
            name, price = line.strip().split(",")
            #strip() --> 刪除讀取的檔案裡的換行(\n)語法
            #split(",") --> 讀取的檔案以"，"做切割(因為檔案寫入csv時，已經沒有逗號了，故這裡重新加上)
            products.append([name, price])
    print(products)

else:
    print("此檔案不存在")



#2.讀取檔案  (提到檢查檔案是否存在的程式行底下)
'''
products = []
with open("products.csv", "r", encoding="Big5") as f:
    for line in f:
        if "商品,價格" in line:
            continue #如果line裡面出現"商品，價格"，則不執行這次的迴圈，重新執行下次的
        name, price = line.strip().split(",")
        #strip() --> 刪除讀取的檔案裡的換行(\n)語法
        #split(",") --> 讀取的檔案以"，"做切割(因為檔案寫入csv時，已經沒有逗號了，故這裡重新加上)
        products.append([name, price])
print(products)
'''

#1.寫入檔案
products = []
while True:
    name = input("請輸入商品名稱: ")
    if name == "q":
        break
    price = int(input("請輸入商品價格: "))
    products.append([name, price])
    #p = []
    #p.append(name)
    #p.append(price)  or 省略前三行 p = [name, price]
    #products.append(p)
print(products)

#印出購買紀錄
for product in products:
    print(product[0], "的價格是", product[1])

with open("products.csv", "w", encoding = "Big5") as f:
    #encoding = Big5, 為excel檔裡的中文編碼系統。若要存成txt檔，則使用 utf-8
    #或統一使用utf-8,之後再在excel裡做轉換 (建議還是盡量使用utf-8)
    f.write("商品,價格\n")
    for product in products:
        f.write(product[0] + "," + str(product[1]) + "\n")
                             #因為price是數字，不能與字串一起用+號，所以在這裡要重新轉成字串
