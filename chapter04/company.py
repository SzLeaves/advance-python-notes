# 魔法函数：增强method的特性，跟class无关
# python会隐式调用

class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    # 可迭代类型 iterable
    def __getitem__(self, item):
        return self.employee[item]

    # 返回一个对象的长度
    def __len__(self):
        return len(self.employee)


company = Company(["tom", "bob", "jane"])

# 获取list
for x in company.employee:
    print(x)

print()
# 通过__getitem__将class变为可迭代类型 iterable
for x in company:
    print(x)
# 此时可以进行slice
print(company[:2])

print()
# 通过__len__可以使用len()获取长度
print(len(company))