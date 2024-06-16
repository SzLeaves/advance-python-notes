from class_method import Date


class User:
    def __init__(self, birthday):
        # 私有属性 加双下划线
        self.__birthday = birthday

    def get_age(self):
        # 返回年龄
        return 2018 - self.__birthday.year


if __name__ == "__main__": 
    user = User(Date(1990, 2, 1))
    # 直接访问私有属性报错 AttributeError: 'User' object has no attribute '__birthday'
    try:
        print(user.__birthday)
    except Exception as e:
        print(e)
        
    # 通过User可以直接调用 (可以认为是py的反射)
    print(user._User__birthday)
    print(user.get_age())