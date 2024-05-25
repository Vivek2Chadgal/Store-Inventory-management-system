#PRODUCT MANAGEMENT SYSTEM
#BY-VIVEK CHADGAL AND TANUJ MEHTA
#CLASS 12A
passwrd=input("Enter Password:")
import mysql.connector
mydb= mysql.connector.connect(host="localhost",user="root",password=passwrd,database="stocks")
mycursor=mydb.cursor()
                                                                                    
def product_mnmg():
                    print(30*'-')
                    print("PRODUCT MANAGEMENT SYSTEM")
                    print(30*'-')
                    print("1. ADD NEW PRODUCT")
                    print(30*'-')
                    print("2. LIST PRODUCT")
                    print(30*'-')
                    print("3. UPDATE PRODUCT")
                    print(30*'-')
                    print("4. DELETE PRODUCT")
                    print(30*'-')
                    print("5. QUIT PROGRAM")
                    print(30*'-')
                    p=int(input("ENTER YOUR CHOICE="))
                    print(30*'-')
                    if p==1:
                        mydb= mysql.connector.connect(host="localhost",user="root",password="mysql", database="stocks")
                        mycursor=mydb.cursor()
                        code=int(input("\t\t Enter product code:"))
                        name=input("\t\t Enter product name:")
                        qty=int(input("\t\t Enter product quantity:"))
                        price=float(input("\t\t Enter price of product:"))
                        cat=input("\t\t Enter product category:")
                        sql="INSERT INTO PRODUCTS(pcode,pname,pprice,pqty,pcat) values(%s,%s,%s,%s,%s);"
                        val=(code,name,price,qty,cat)
                        mycursor.execute(sql,val)
                        mydb.commit()
                        print("\t\t Product ADDED")
                        print(60*'-')
                        product_mnmg()
                    elif p==2:
                        print("\t\t\t List of all products")
                        print('\t\t',50*'-')
                        mydb=mysql.connector.connect(host="localhost", user="root", password="mysql",database="stocks")
                        mycursor=mydb.cursor()
                        z="SELECT* from PRODUCTS;"
                        mycursor.execute(z)
                        print("\t\t\t PRODUCT DETAILS")
                        print('\t\t',50*'-')
                        print("\t\t  code     name   price   quantity   category")
                        print('\t\t',50*'-')
                        for i in mycursor:
                                           print("\t\t ",i[0],"\t",i[1],' ',i[2], "\t ", i[3], "\t   ", i[4])
                                           print('\t\t',50*'-')
                        product_mnmg()
                    elif p==3:
                            mydb=mysql.connector.connect(host="localhost", user="root", password="mysql",database="stocks")
                            mycursor=mydb.cursor()
                            code=int(input("Enter the product code"))
                            qty=int(input("Enter the new quantity:"))
                            price=int(input("Enter INCREASED price of product"))
                            y="UPDATE PRODUCTS SET pqty=%s,pprice=pprice+%s WHERE pcode=%s;"
                            value=(qty,price,code)
                            mycursor.execute(y,value)
                            mydb.commit()
                            print("\t\t Products detail updated")
                            print(60*'-')
                            product_mnmg()
                    elif p==4:
                        mydb= mysql.connector.connect(host="localhost",user="root",password="mysql", database="stocks")
                        mycursor=mydb.cursor()
                        print(60*'-')
                        code=int(input("Enter product code to be DELETED:"))
                        val=(code,)
                        A="DELETE FROM PRODUCTS where pcode=%s;"
                        mycursor.execute(A,val)
                        mydb.commit()
                        print(60*'-')
                        print("Product DELETED Successfully")
                        print(60*'-')
                        product_mnmg()
                        
                    else:
                        print('\t\t',35*'-')
                        print("\t\t  THANKS FOR USING THIS PROGRAM")
                        print('\t\t',35*'-')
                        print("\t\t  CREDITS FOR THIS PROGRAM")
                        print("\t\t\t  TANUJ MEHTA")
                        print("\t\t\t  VIVEK CHADGAL")
                        print('\t\t',35*'-')
                        print("\t\t  SPECIAL CREDITS TO: MRS. SEEMA")
                        print('\t\t',35*'-')
                        


for j in mycursor:
        print(j)
product_mnmg()                                
