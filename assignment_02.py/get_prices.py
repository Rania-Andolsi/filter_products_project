def get_prices(filename):
    products=[ ]
    prices=[ ]
    f=open(filename,'r')
    t=f.read()
    l=t.splitlines()
    f.close()
    for line in l:
        product, price= line.strip().split(',')
        products.append(product)
        prices.append(float(price))
    return products, prices
filename= input("enter the filename: ")
products,prices= get_prices(filename)
print(products[:3])
print(prices[:3])
for product, price in zip(products,prices):
    print(f"{product} {price}")
    




