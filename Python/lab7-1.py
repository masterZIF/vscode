class User:
    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd

class Account:
    def __init__(self):
        self.user_list = []  # 用户列表

    def login(self):
        """
        用户登录，用户输入用户名和密码并去 self.user_list 中检查用户是否合法
        """
        print("\n--- 开始登录 ---")
        name = input("请输入用户名: ")
        pwd = input("请输入密码: ")

        for user in self.user_list:
            if user.name == name and user.pwd == pwd:
                return True
        return False

    def register(self):
        """
        用户注册，动态创建 User 对象，并添加到 self.user_list 中
        """
        print("\n--- 用户注册 ---")
        name = input("设置用户名: ")
        pwd = input("设置密码: ")
        
        # 创建对象并添加
        new_user = User(name, pwd)
        self.user_list.append(new_user)
        print(f"用户 {name} 注册成功！")

    def run(self):
        """
        主程序，先进行 2 次用户注册注册两个不同的用户，再进行用户登录（3 次重试机会）
        """
        # 1. 注册两个用户
        print("请先注册两个用户：")
        self.register()
        self.register()

        # 2. 登录尝试，最多3次
        for i in range(3):
            print(f"\n>>> 第 {i + 1} 次登录尝试")
            if self.login():
                print("登录成功！")
                break
            else:
                print("用户名或密码错误。")
                if i == 2:
                    print("三次尝试失败，程序退出。")

if __name__ == "__main__":
    obj = Account()
    obj.run()