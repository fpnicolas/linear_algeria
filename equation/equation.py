from sympy import Matrix, solve_linear_system, symbols
x,y,z,u = symbols('x,y,z,u')
A = Matrix(((1,-1,2,-2,0),(0,1,1,2,0),(2,-1,5,-2,0)))
answer = solve_linear_system(A,x,y,z,u)
print(answer)
  
