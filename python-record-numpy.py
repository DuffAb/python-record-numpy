import numpy as np
from numpy.random import default_rng
rg = default_rng()
# 参考连接：https://numpy.org/devdocs/user/quickstart.html

A = np.arange(15)
print(A)


A = A.reshape(3, 5)
print(A)


# 数组的轴(维)数
print(A.ndim)

# 返回一个整数元组，表示每个维度中数组的大小。比如一个n行m列的矩阵，则返回(n, m)
print(A.shape)

# 数组中元素的总数
print(A.size)

# 数组中元素类型的对象
print(A.dtype)

# 数组中每个元素的字节大小
print(A.itemsize)

# 包含数组的实际元素的缓冲区
print(A.data)

print(type(A))

# 有几种创建数组的方法
B = np.array([6, 7, 8])
print(B)
B = np.array([(1.5,2,3), (4,5,6)])
print(B)
# 数组的类型也可以在创建时显式指定
B = np.array( [ [1,2], [3,4] ], dtype=complex) # 复数类型
print(B)
# 创建1个3行4列的全0矩阵
A = np.zeros( (3,4) )
print(A)
# 创建2个3行4列的全1矩阵
A = np.ones( (2,3,4), dtype=np.int16 )
print(A)
# 创建1个2行3列的未初始化的矩阵
A = np.empty( (2,3) )
print(A)
# 创建元素范围 10 <= X < 30，间隔为5的数组
A = np.arange( 10, 30, 5 )
print(A)
A = np.arange( 0, 2, 0.3 )
print(A)

A = np.arange(6)                         # 1d array
A = np.arange(12).reshape(4,3)           # 2d array
A = np.arange(24).reshape(2,3,4)         # 3d array





###### Basic Operations 基本运算 #####
a = np.array( [20,30,40,50] )
b = np.arange( 4 )
# 矩阵减法
c = a-b
# 数组内各元素分别平方
c = b**2
# 数组内各元素取 sin 再乘 10
c = 10*np.sin(a)
# 数组内各元素与 35 比较大小，返回 True 或 False
c = a < 35


A = np.array( [[1,1], [0,1]] )
B = np.array( [[2,0], [3,4]] )

# 矩阵点乘，即A、B 矩阵内元素对应相乘
C = A * B      # elementwise product
print(C)
C = np.multiply(A, B)
print(C)

# 矩阵乘法 C=AB
C = A @ B      # matrix product
print(C)
C = A.dot(B)   # another matrix product
print(C)

a = np.ones((2,3), dtype=int)
b = rg.random((2,3))
# *= 操作符，
a *= 3
print(a)

b += a
print(b)

# a += b                  # b is not automatically converted to integer type
# print(a)

# 矩阵转置
c = b.T
print(b)
print(c)























