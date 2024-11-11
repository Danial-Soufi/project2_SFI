def newton_raphson_root_fourth(a, tolerance=1e-6):
    x = a / 2.0  
    while True:
        f_x = x**4 - a
        f_prime_x = 4 * x**3
        x_new = x - f_x / f_prime_x
        
        if abs(x_new - x) < tolerance:
            return x_new
        
        x = x_new

a = 30

root = newton_raphson_root_fourth(a)
print(f" {a}  {root}")