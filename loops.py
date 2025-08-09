for i in range(10):
    print(i)

for x in range(10):
    print('x -',x)

for x in range(1,11):
    print(f"2*{x}={2*x}")

#for x in range(1,11):
    #print(f"1+{x}={1+x}")

def mul(num):
    for x in range(1,11):
        print(f"{num}*{x}={num*x}")
mul(4)
for i in range(1,11):
    if(i%2==0 and i%2==0):
        print(f"{i}-fuzz buzz")
    elif(i%3==0):
            print(f"{i}-buzz")
    elif(i%2==0):
            print(f"{i}-fuzz")


for y in range(1,11):
     if(y%2==0):
        print(y**2,'squares')
     else:
        print(y**3,'cubes')

for y in range(2,9):
    print(y**3) 
    print(y**2)                

ecommerce_data = [
    {
        "order_id": "ORD004",
        "customer_name": "John Smith",
        "order_id": "ORD001",
        "customer_name": "Alice Johnson",
        "product": "Wireless Mouse",
        "category": "Electronics",
        "quantity": 2,
        "price_per_unit": 599,
        "payment_method": "Credit Card",
        "delivery_status": "Delivered"
    },
    {
        "order_id": "ORD002",
        "customer_name": "Rajesh Kumar",
        "product": "Bluetooth Speaker",
        "category": "Electronics",
        "quantity": 1,
        "price_per_unit": 1999,
        "payment_method": "UPI",
        "delivery_status": "Shipped"
    },
    {
        "order_id": "ORD003",
        "customer_name": "Maria Fernandez",
        "product": "Leather Handbag",
        "category": "Fashion",
        "quantity": 1,
        "price_per_unit": 2499,
        "payment_method": "Cash on Delivery",
        "delivery_status": "Out for Delivery"
    },
    {
        "order_id": "ORD004",
        "customer_name": "John Smith",
        "product": "Running Shoes",
        "category": "Footwear",
        "quantity": 1,
        "price_per_unit": 3499,
        "payment_method": "Net Banking",
        "delivery_status": "Delivered"
    },
    {
        "order_id": "ORD005",
        "customer_name": "Anjali Mehta",
        "product": "Cotton Bedsheet Set",
        "category": "Home & Living",
        "quantity": 3,
        "price_per_unit": 899,
        "payment_method": "Credit Card",
        "delivery_status": "Cancelled"
    },
    {
        "order_id": "ORD006",
        "customer_name": "Samuel Lee",
        "product": "Smart Watch",
        "category": "Wearable Tech",
        "quantity": 1,
        "price_per_unit": 5299,
        "payment_method": "Debit Card",
        "delivery_status": "Delivered"
    },
    {
        "order_id": "ORD007",
        "customer_name": "Neha Sharma",
        "product": "Makeup Kit",
        "category": "Beauty",
        "quantity": 2,
        "price_per_unit": 1499,
        "payment_method": "UPI",
        "delivery_status": "Processing"
    },
    {
        "order_id": "ORD008",
        "customer_name": "David Brown",
        "product": "Office Chair",
        "category": "Furniture",
        "quantity": 1,
        "price_per_unit": 4599,
        "payment_method": "Credit Card",
        "delivery_status": "Delivered"
    }
]

for x in ecommerce_data:
    print(x["costomer_name"])