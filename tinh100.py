"""
Cho 1 dãy số 123456789, chèn vào giữa các số 1 phép toán (+, - or none) để ra kết quả 100
yêu cầu:
- không dùng package itertools
- không dùng 9 vòng for
"""


sum=0
a=[1,2,3,4,5,6,7,8,9]
a1 = a[:7]
a2 = a[7:]
sum1 = a1[0] + a1[1] - a1[2] - a1[3] + a1[4] - a1[5] + a1[6]
a3 = []
for i in a2:
    a3.append(str(i))
    a4 = sorted(a3, reverse=True)
sum = sum1 + int(''.join(a4))
print(sum)