products = []
while True:
    name = input("請輸入商品名稱: ")
    if name == "q":
        break
    price = input("請輸入商品價格: ")
    products.append([name, price])
    #p = []
    #p.append(name)
    #p.append(price)  or 省略前三行 p = [name, price]
    #products.append(p)
print(products)

for product in products:
    print(product[0], "的價格是", product[1])

with open("products.csv", "w", encoding = "Big5") as f:
    for product in products:
        f.write(product[0] + "," + product[1] + "\n")
