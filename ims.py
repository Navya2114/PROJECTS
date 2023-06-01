import pyodbc
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

server = 'LAPTOP-JPOUJBR6\SQLEXPRESS'
database = 'NEWIMS'
driver = '{SQL Server}'

connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};trusted_connection=yes'

conn = pyodbc.connect(connection_string)


#cn.execute(f"insert into customer(customer_name,customer_address,customer_email) values('{customer_name}','{customer_address}','{customer_email}')")
#conn.commit()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/show-customers')
def customer_show():
    cn = conn.cursor()
    cn.execute("select * from customer")
    data = []
    for i in cn.fetchall():
        customer = {}
        customer['customer_id'] = i[0]
        customer['customer_name'] = i[1]
        customer['customer_address'] = i[2]
        customer['customer_email'] = i[3]
        data.append(customer)
    print(data)

    return render_template('showcustomers.html',data = data) 

@app.route('/show-product')
def product_show():
    cn = conn.cursor()
    cn.execute("select * from product")
    data = []
    for i in cn.fetchall():
        product = {}
        product['product_id'] = i[0]
        product['product_name'] = i[1]
        product['product_stock'] = i[2]
        product['product_price'] = i[3]
        product['product_supplierid'] = i[4]
        data.append(product)
    print(data)

    return render_template('showproducts.html',data = data)        


@app.route('/show-supplier')
def supplier_show():
    cn = conn.cursor()
    cn.execute("select * from supplier")
    data = []
    for i in cn.fetchall():
        supplier = {}
        supplier['supplier_id'] = i[0]
        supplier['supplier_name'] = i[1]
        supplier['supplier_address'] = i[2]
        supplier['supplier_email'] = i[3]
        data.append(supplier)
    print(data)

    return render_template('showsupplier.html',data = data) 

@app.route('/show-orders')
def orders_show():
    cn = conn.cursor()
    cn.execute("select * from orders")
    data = []
    for i in cn.fetchall():
        orders = {}
        orders['order_id'] = i[0]
        orders['product_id'] = i[1]
        orders['customer_id'] = i[2]
        orders['quantity'] = i[3]
        data.append(orders)
    print(data)

    return render_template('showorders.html',data = data) 

@app.route('/add-customer',methods = ['GET','POST'])
def addcustomer():
    if request.method=='POST':
        cn = conn.cursor()
        customername = request.form.get('name')
        customeraddress = request.form.get('address')
        customeremail = request.form.get('email')
        cn.execute(f"insert into customer(customer_name,customer_address,customer_email) values('{customername}','{customeraddress}','{customeremail}')")
        conn.commit()
        print('Data has been Inserted')
        return jsonify({'message':'sucessfull'})
    else:
        return render_template('addcustomer.html')
    
    
@app.route('/add-product',methods = ['GET','POST'])
def addproduct():
    if request.method=='POST':
        cn = conn.cursor()
        productname = request.form.get('product_name')
        productstock = request.form.get('product_stock')
        productprice = request.form.get('product_price')
        supplierid = request.form.get('product_supplier_id')
        print(productname,productstock,productprice,supplierid)
        cn.execute(f"insert into product(product_name,stock,price,supplier_id) values('{productname}','{productstock}',{productprice},'{supplierid}')")
        conn.commit()
        print('Data has been Inserted')
        return jsonify({'message':'sucessfull'})
    else:
        return render_template('addproduct.html')    

    
@app.route('/add-supplier',methods = ['GET','POST'])
def addsupplier():
    if request.method=='POST':
        cn = conn.cursor()
        suppliername = request.form.get('name')
        supplieraddress = request.form.get('address')
        supplieremail = request.form.get('email')
        cn.execute(f"insert into supplier(supplier_name,supplier_address,supplier_email) values('{suppliername}','{supplieraddress}','{supplieremail}')")
        conn.commit()
        print('Data has been Inserted')
        return jsonify({'message':'sucessfull'})
    else:
        return render_template('addsupplier.html')
    

@app.route('/add-orders',methods = ['GET','POST'])
def addorders():
    if request.method=='POST':
        cn = conn.cursor()
        productid = request.form.get('product_id')
        customerid = request.form.get('customer_id')
        quantity = request.form.get('quantity')
        cn.execute(f"insert into orders(product_id,customer_id,quantity) values('{productid}','{customerid}','{quantity}')")
        conn.commit()
        print('Data has been Inserted')
        return jsonify({'message':'sucessfull'})
    else:
        return render_template('addorders.html')



    
    
@app.route('/update-customer',methods = ['GET','POST'])
def updatecustomer():
    if request.method=='POST':
        cn = conn.cursor()
        customerid = request.form.get('customerid')
        change = request.form.get('change')
        newvalue = request.form.get('newvalue')
        print(change,newvalue,customerid)
        cn.execute(f"update customer set {change} = '{newvalue}' where customer_id = '{customerid}'")
        conn.commit()
        print('Data has been updated')
        return jsonify({'message':'sucessfull'})
    else:
        return render_template('updatecustomer.html')    



@app.route('/update-product',methods = ['GET','POST'])
def updateproduct():
    if request.method=='POST':
        cn = conn.cursor()
        productid = request.form.get('productid')
        change = request.form.get('change')
        newvalue = request.form.get('newvalue')
        print(change,newvalue,productid)
        cn.execute(f"update product set {change} = '{newvalue}' where product_id = '{productid}'")
        conn.commit()
        print('Data has been updated')
        return jsonify({'message':'sucessfull'})
    else:
        return render_template('updateproduct.html')




if __name__ == '__main__':
    app.run()


