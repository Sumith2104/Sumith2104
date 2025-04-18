def zomato_data(file_name, num_records):
    data = []
    del_status = ["Delivered","Cancelled"]
    pay_meth = ["UPI", "CASH", "CARD"]
    datelist = [i for i in range(1, 32)]
    used_cus_nos = set()
    used_res_nos = set()
    fitem = set()
    order_set = set()

    for _ in range(num_records):
        while True:
            ord_num = random.randint(255419, 10000000)
            cus_id = random.randint(26500, 39084)
            resto_id = random.randint(67544, 384973)
            customer = f"CUSID{cus_id}"
            resto = f"RESTOID{resto_id}"
            date = random.choice(datelist)
            dat = f"{date}-03-2025"
            food = random.randint(2000, 2500)
            quantity = random.randint(1, 10)
            delivery = random.choice(del_status)
            payment = random.choice(pay_meth)
            if cus_id not in used_cus_nos:
                used_cus_nos.add(cus_id)
            if resto_id not in used_res_nos:
                used_res_nos.add(resto_id)
            if food not in fitem:
                fitem.add(food)
            if ord_num not in order_set:
                order_set.add(ord_num)
                break

        inp_for_list = [ord_num,  dat, customer, resto, food,quantity,delivery, payment]
        data.append(inp_for_list)

    df = pandas.DataFrame(data, columns=["order_id","orderDate","customer_id","Restaurant_ID","Food_item","quantity","deliver_status","payment_method"])
    df.to_csv(file_name,mode = 'a', index=False, chunksize=10000)
    gc.collect()
    exit("Done")

#private
