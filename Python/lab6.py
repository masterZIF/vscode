# lab6.py
import datetime
import os
import re
import requests  # 用于附加题
from functools import wraps

# ======================================================================
# [cite_start]1. 装饰器：重复执行5次 [cite: 1507]
# ======================================================================

def repeat_five_times(func):
    """
    不带参数的装饰器，使函数重复执行5次。
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"--- 函数 '{func.__name__}' 将执行5次 ---")
        for i in range(5):
            print(f"第 {i+1} 次执行:")
            func(*args, **kwargs)
        print("--- 执行完毕 ---")
    return wrapper

@repeat_five_times
def task1_func():
    print("  这是第一题的函数。")

# ======================================================================
# [cite_start]2. 装饰器：带参数，指定重复次数 [cite: 1508]
# ======================================================================

def repeat(num_times):
    """
    带参数的装饰器工厂，用于指定重复次数。
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"--- 函数 '{func.__name__}' 将执行 {num_times} 次 ---")
            for i in range(num_times):
                print(f"第 {i+1} 次执行:")
                func(*args, **kwargs)
            print("--- 执行完毕 ---")
        return wrapper
    return decorator

@repeat(num_times=3)
def task2_func(name):
    print(f"  这是第二题的函数，你好, {name}。")

# ======================================================================
# [cite_start]3. 装饰器：通讯录系统扩展 [cite: 1509]
# ======================================================================

# --- 装饰器定义 (Task 3a & 3b) ---

# "全局"登录状态
login_session = {"logged_in": False}
USER_FILE = 'user_info.txt'
LOG_FILE = 'call_log.txt'

def get_user_data():
    """
    辅助函数，从 user_info.txt 加载用户数据。
    """
    try:
        with open(USER_FILE, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            user_db = {}
            for line in lines:
                # 假设格式是 username:password
                parts = line.strip().split(':')
                if len(parts) == 2:
                    user_db[parts[0]] = parts[1]
            return user_db
    except FileNotFoundError:
        print(f"警告: 未找到 {USER_FILE}。无法登录。")
        return {}
            
def login_required(func):
    """
    [cite_start][cite: 1511] 装饰器：检查用户登录状态。
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        # [cite: 1512] 如果已经登录则直接调用函数
        if login_session["logged_in"]:
            return func(*args, **kwargs)
        
        # [cite: 1512] 如果未登录要求用户进行登录
        print("--- 访问受限，请先登录 ---")
        user_db = get_user_data()
        
        if not user_db:
            print("用户数据库为空或加载失败，无法继续。")
            return

        while True:
            username = input("请输入用户名: ")
            password = input("请输入密码: ")
            
            # [cite: 1513] 验证
            if user_db.get(username) == password:
                print(f"登录成功！欢迎, {username}。")
                login_session["logged_in"] = True
                # 登录成功后调用函数
                return func(*args, **kwargs)
            else:
                print("用户名或密码错误，请重新输入。")
                        
    return wrapper

def log_call(func):
    """
    [cite_start][cite: 1516] 装饰器：记录函数调用时间和名称。
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        # [cite: 1517] 将调用的 函数名 和 调用时间 记录在 文本文件 当中
        call_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_message = f"函数: {func.__name__} | 调用时间: {call_time}\n"
        
        try:
            with open(LOG_FILE, 'a', encoding='utf-8') as f:
                f.write(log_message)
        except Exception as e:
            print(f"日志写入失败: {e}")
        
        # 执行原函数
        return func(*args, **kwargs)
    return wrapper

# --- lab3.py 的代码 ---
# (已从您提供的 lab3.py 文件中复制并应用了装饰器)

contacts_list = []

def print_header():
    """打印通讯录的表头"""
    print("=" * 80)
    print(f"{'No.':<5} {'Name':<15} {'QQ':<15} {'Phone':<15} {'E-mail':<30}")
    print("-" * 80)

def print_contact(contact_data, index):
    """
    打印单条联系人记录
    """
    print(f"{index:<5} {contact_data['name']:<15} {contact_data['qq']:<15} {contact_data['phone']:<15} {contact_data['email']:<30}")

@log_call
@login_required
def print_all_contacts(contacts):
    """
    打印所有联系人
    """
    print("~" * 28 + "通讯录数据列表" + "~" * 28)
    if not contacts:
        print("通讯录为空，请先添加记录。")
        print("~" * 70)
        return

    print_header()
    for i, contact in enumerate(contacts, start=1):
        print_contact(contact, i)
    print("=" * 80)

def get_valid_index(contacts):
    """
    获取一个有效的、基于1的序号，并转换成基于0的列表索引。
    """
    while True:
        try:
            num_str = input("请输入要操作的记录序号: ")
            num = int(num_str)
            
            if 1 <= num <= len(contacts):
                return num - 1  # 返回基于0的索引
            else:
                print(f"输入的序号 {num} 不存在，请重新输入 (范围 1-{len(contacts)}): ")
        except ValueError:
            print("输入无效，请输入一个数字序号。")

@log_call
@login_required
def add_contact(contacts):
    """
    增加数据子界面
    """
    print("--- 增加记录 ---")
    name = input("请输入姓名: ")
    qq = input("请输入QQ: ")
    phone = input("请输入电话: ")
    email = input("请输入邮箱: ")
    
    new_contact = {
        "name": name,
        "qq": qq,
        "phone": phone,
        "email": email
    }
    
    contacts.append(new_contact)
    
    print("插入成功! 此时表为")
    print_header()
    print_contact(new_contact, len(contacts))
    print("=" * 80)

@log_call
@login_required
def delete_contact(contacts):
    """
    删除数据子界面
    """
    print("--- 删除记录 ---")
    if not contacts:
        print("通讯录为空，无法删除。")
        return

    index_to_delete = get_valid_index(contacts)
    
    if index_to_delete is not None:
        deleted_contact = contacts.pop(index_to_delete)
        print(f"已成功删除 {deleted_contact['name']} 的记录。")
        print("最新的列表为:")
        print_all_contacts(contacts)

@log_call
@login_required
def modify_contact(contacts):
    """
    修改数据子界面
    """
    print("--- 修改记录 ---")
    if not contacts:
        print("通讯录为空，无法修改。")
        return

    index_to_modify = get_valid_index(contacts)
    
    if index_to_modify is not None:
        contact_to_modify = contacts[index_to_modify]
        print(f"正在修改序号 {index_to_modify + 1} ({contact_to_modify['name']}) 的记录。")
        
        print("请输入要修改的子项:")
        print("  n : 修改姓名")
        print("  q : 修改QQ")
        print("  p : 修改电话")
        print("  m : 修改邮箱")
        print("  (其他键退出修改)")
        
        sub_choice = input("请选择: ").lower()
        
        field_key = None
        field_name = ""

        if sub_choice == 'n':
            field_key, field_name = "name", "姓名"
        elif sub_choice == 'q':
            field_key, field_name = "qq", "QQ"
        elif sub_choice == 'p':
            field_key, field_name = "phone", "电话"
        elif sub_choice == 'm':
            field_key, field_name = "email", "邮箱"
        else:
            print("已取消修改。")
            return

        new_value = input(f"请输入新的{field_name}，若不修改输入空格后回车: ")
        
        if new_value.strip() == "":
            print("不修改")
        else:
            contact_to_modify[field_key] = new_value
            print("已修改，最新的列表为:")
            print_all_contacts(contacts)

@log_call
@login_required
def find_contact(contacts):
    """
    查找记录子界面
    """
    print("--- 查找记录 ---")
    if not contacts:
        print("通讯录为空，无法查找。")
        return

    index_to_find = get_valid_index(contacts)
    
    if index_to_find is not None:
        print("查找成功，结果为:")
        print_header()
        print_contact(contacts[index_to_find], index_to_find + 1)
        print("=" * 80)

def show_main_menu():
    """
    开始菜单
    """
    print("\n" + "#" * 30 + " NKCS InfoSystem V0.2 " + "#" * 30)
    print("=" * 34 + " Powered by Zodiac==" + "=" * 34)
    print("\n")
    print(" " * 30 + "a : 增加记录")
    print(" " * 30 + "d : 删除记录")
    print(" " * 30 + "c : 修改记录")
    print(" " * 30 + "f : 查找记录")
    print(" " * 30 + "s : 展示记录")
    print(" " * 30 + "q : 退出系统")
    print("\n")

def main_lab3():
    """
    实验主函数，通过实现通讯录管理系统，练习python中函数的定义、调用等知识。
    """
    while True:
        show_main_menu()
        choice = input("请输入功能对应的代号: ").strip().lower()
        
        if choice == 'a':
            add_contact(contacts_list)
        elif choice == 'd':
            delete_contact(contacts_list)
        elif choice == 'c':
            modify_contact(contacts_list)
        elif choice == 'f':
            find_contact(contacts_list)
        elif choice == 's':
            print_all_contacts(contacts_list)
        elif choice == 'q':
            print("感谢使用 NKCS InfoSystem V0.2，再见！")
            break
        else:
            print("输入代号无效，请重新输入 (a, d, c, f, s, q)")
        
        input("\n按回车键返回主菜单...")

# ======================================================================
# [cite_start]4. 附加题：缓存网页内容 [cite: 1518]
# ======================================================================

def cache_webpage(func):
    """
    [cite_start][cite: 1521] 装饰器：实现缓存网页内容功能。
    """
    @wraps(func)
    def wrapper(url):
        # [cite: 1523] 根据URL生成一个简单的文件名，例如 baidu.html
        domain_match = re.search(r'https?://(www\.)?([^/]+)', url)
        if domain_match:
            filename = domain_match.group(2) + ".html"
        else:
            # 备用文件名
            filename = url.replace(':', '').replace('/', '_') + ".html"
        
        # [cite: 1522] 检查缓存文件是否存在且不为空
        if os.path.exists(filename) and os.path.getsize(filename) > 0:
            print(f"--- 发现缓存 {filename}，从本地读取 ---")
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    return f.read()
            except Exception as e:
                print(f"本地缓存读取失败: {e}")
        
        # [cite: 1522] 否则就去下载页面
        print(f"--- 本地无缓存，正在下载 {url} ---")
        content = func(url)
        
        # [cite: 1522] 之后缓存在文件中
        if content:
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"--- 已保存至 {filename} ---")
            except Exception as e:
                print(f"缓存写入失败: {e}")
        
        return content
    return wrapper

@cache_webpage
def download_webpage(url):
    """
    [cite_start][cite: 1519] 编写下载网页内容的函数
    """
    try:
        response = requests.get(url)
        response.raise_for_status() # 检查 4xx/5xx 错误
        # [cite: 1520] 函数返回下载页面的结果
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"下载 {url} 失败: {e}")
        return None

# ======================================================================
# 运行所有任务
# ======================================================================

if __name__ == "__main__":
    
    print("======== 任务1：重复执行5次 ========")
    task1_func()

    print("\n======== 任务2：重复执行3次 ========")
    task2_func("Nankai")
    
    # --------------------------------------------
    # 开启附加题会自动下载网页，如果不需要请注释掉
    print("\n======== 附加题：网页缓存 ========")
    baidu_url = "https://www.baidu.com"
    
    # 第一次调用：会下载并缓存
    print("--- 第一次调用 (百度) ---")
    download_webpage(baidu_url)
    
    # 第二次调用：会从缓存读取
    print("\n--- 第二次调用 (百度) ---")
    download_webpage(baidu_url)
    
    # --------------------------------------------

    print("\n======== 任务3：启动通讯录系统 ========")
    # 运行通讯录系统
    main_lab3()
    
    print("\n(已注释掉 main_lab3() 的调用，如需测试请取消本行注释)")
    # 提示：取消上一行的注释 # main_lab3() 即可运行通讯录系统。
    # 运行通讯录会进入循环，所以把它放在最后。