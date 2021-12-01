n = int(input("Nhập số bất kì vào: "))
if (n==1):
    print("Tôi là người Việt Nam")
elif (n==2):
    print("Tôi là người Hàn Quốc")
elif (n==3):
    print("Tôi là người Campuchia")
else:
    print("Tôi không phải là người")

#nhập vào 3 cạnh của tam giác ,kiểm tra hợp lệ về tam giác , và tính chu vi và diện tích
a = int(input("Nhập số đó vào: "))
b = int(input("Nhập số đó vào: "))
c = int(input("Nhập số đó vào: "))
if (a>0 and b>0 and c>0):
    print("Hợp lệ")
    C=a+b+c
    P=C/2
    S=P*(P-a)*(P-b)*(P-c)

    print("Chu vi là: ",C)
    print("Diện tích là: ",S)

else :
    print("Không thể tính")










