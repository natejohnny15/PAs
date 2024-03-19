import numpy as np

def first_func():
    f = np.poly1d([2,3,1])
    print(f'First function:\nf(x) = \n{f}\nf(2) = {f(2)}\n')

def second_func():
    f = np.poly1d([1,0,1])
    fd = np.polyder(f)
    print(f"Second function:\nf'(2) = {fd(2)}\n\n")

def get_x1():
    return float(input("Enter a value for x_1: "))
     
def get_poly():
    return input("Enter your polynomial, for example, if you wanted to enter 2x^2 + 2x + 4, you would enter '2,2,4':")
    
def make_poly():
    coeffs_str = get_poly()
    coeffs = coeffs_str.split(',')
    for i in range(len(coeffs)): 
        coeffs[i] = float(coeffs[i])
    return np.poly1d(coeffs)


def newtons_method(f,x_1,count):
    fd = np.polyder(f)
    print(f"x_{count} = {x_1:.3f}")
    x_n = x_1 - (f(x_1)/fd(x_1))
    if round(x_n,3) == round(x_1,3):
        print(f"The final value with stabilized thousandths place is: {x_n:.3f}")
        return x_n
    else: 
        count += 1
        return newtons_method(f, x_n,count), count
      


def main():
    first_func()
    second_func() 
    f = make_poly()
    x_1 = get_x1()
    print('\n')
    newtons_method(f, x_1,0)
    print(f"\nRoots using numpy.roots() : {np.roots(f)}")
    
main()
    

