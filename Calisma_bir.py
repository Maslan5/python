
def factorial(n):
    try:
        n = int(n)
        if(n<0):
            print("Lütfen pozitif bir tam sayı giriniz.")
            return factorial(input("Lütfen Faktöriyeli Alınacak Sayıyı Giriniz : "))
        elif(n==0):
            return 1
        else:
            return n * factorial(n-1)

    except ValueError:
        print("Lütfen sadece tam sayı giriniz.")
        return factorial(input("Lütfen Faktöriyeli Alınacak Sayıyı Giriniz : "))
print(factorial(input("Lütfen faktöriyeli alınacak sayıyı giriniz  : ")))