# PythonRoad
product_list = [["iphone",5800],["imac",12000],["iwatch",3000],["ipad",4000],["ipod",1000]];
shopping_cart = [];
salary = input("input your salary:");
if salary.isdigit():
  salary = int(salary);
  while True:
    for item in product_list:
      print(product_list.index(item),item);
     user_choice = input("which to buy");
     if user_choice.isdigit():
      user_choice = int(user_choice);
      if user_choice < len(product_list) and user_choice >=0:
        p_item = product_list[user_choice];
        if p_item[1] <= salary:
          shopping_cart.append(p_item);
          salary -= p_item[1];
          print("add %s into shoppingcart and balance is %s"%(p_item,salary));
        else:
          print("the balance is %s,what fuck to buy"%(salary));
      else:
        print("the product code is not exist");
     elif user_choice == "q":
      for i in shopping_cart:
        print(i,"the balance is %s"%(salary));
      exit()
     else:
      print("invilable option")
else:
  print("please input the corrent salary");
     
