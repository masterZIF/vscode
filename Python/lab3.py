contacts_list = []

def print_header():
    """打印通讯录的表头"""
    print("=" * 80)
    # [cite: 18, 22, 27, 30] 统一的表格格式
    print(f"{'No.':<5} {'Name':<15} {'QQ':<15} {'Phone':<15} {'E-mail':<30}")
    print("-" * 80)

def print_contact(contact_data, index):
    """
    打印单条联系人记录
    :param contact_data: 包含联系人信息的字典
    :param index: 记录的序号（从1开始）
    """
    print(f"{index:<5} {contact_data['name']:<15} {contact_data['qq']:<15} {contact_data['phone']:<15} {contact_data['email']:<30}")

def print_all_contacts(contacts):
    """
    打印所有联系人
    [cite: 31, 32] 对应 's' 展示数据子界面
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
    [cite: 36] 包含容错要求
    """
    while True:
        try:
            num_str = input("请输入要操作的记录序号: ")
            num = int(num_str)
            
            # [cite: 21, 24] 若序号不存在，则给出提示
            if 1 <= num <= len(contacts):
                return num - 1  # 返回基于0的索引
            else:
                print(f"输入的序号 {num} 不存在，请重新输入 (范围 1-{len(contacts)}): ")
        except ValueError:
            print("输入无效，请输入一个数字序号。")

#  增、删、改、查功能分别使用函数封装

def add_contact(contacts):
    """
    [cite: 15] 2.1 增加数据子界面
    """
    print("--- 增加记录 ---")
    # [cite: 16] 输入数据包括姓名、QQ号码、电话号码、邮箱
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
    
    # [cite: 17] 输入成功后，提示添加成功，并返回添加的数据
    print("插入成功! 此时表为")
    print_header()
    print_contact(new_contact, len(contacts)) # 序号是新列表的长度
    print("=" * 80)

def delete_contact(contacts):
    """
    [cite: 19] 2.2 删除数据子界面
    """
    print("--- 删除记录 ---")
    if not contacts:
        print("通讯录为空，无法删除。")
        return

    # [cite: 20] 通过输入序号进行删除
    index_to_delete = get_valid_index(contacts)
    
    if index_to_delete is not None:
        # [cite: 13] 用列表中的对应方法对数据进行操作 (pop)
        deleted_contact = contacts.pop(index_to_delete)
        # [cite: 22] 删除后，提示删除成功
        print(f"已成功删除 {deleted_contact['name']} 的记录。")
        print("最新的列表为:")
        print_all_contacts(contacts)

def modify_contact(contacts):
    """
    [cite: 23] 2.3 修改数据子界面
    """
    print("--- 修改记录 ---")
    if not contacts:
        print("通讯录为空，无法修改。")
        return

    # [cite: 24] 输入待修改的序号，若序号不存在，给出提示
    index_to_modify = get_valid_index(contacts)
    
    if index_to_modify is not None:
        contact_to_modify = contacts[index_to_modify]
        print(f"正在修改序号 {index_to_modify + 1} ({contact_to_modify['name']}) 的记录。")
        
        # [cite: 25] 进入下一级页面选择需要修改的子项
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

        # [cite: 26] 若不需要修改，可以输入空格后回车取消修改
        new_value = input(f"请输入新的{field_name}，若不修改输入空格后回车: ")
        
        if new_value.strip() == "":
            print("不修改")
        else:
            contact_to_modify[field_key] = new_value
            # [cite: 27] 输入成功后，提示修改成功，并返回修改的数据
            print("已修改，最新的列表为:")
            print_all_contacts(contacts)


def find_contact(contacts):
    """
    [cite: 28] 2.4 查找记录子界面
    """
    print("--- 查找记录 ---")
    if not contacts:
        print("通讯录为空，无法查找。")
        return

    # [cite: 29] 输入序号进行查找
    index_to_find = get_valid_index(contacts)
    
    if index_to_find is not None:
        # [cite: 30] 查找成功，显示结果
        print("查找成功，结果为:")
        print_header()
        print_contact(contacts[index_to_find], index_to_find + 1)
        print("=" * 80)

def show_main_menu():
    """
    [cite: 8, 9] 1. 开始菜单
    """
    print("\n" + "#" * 30 + " NKCS InfoSystem V0.1 " + "#" * 30)
    print("=" * 34 + " Powered by Zodiac==" + "=" * 34)
    print("\n")
    print(" " * 30 + "a : 增加记录")
    print(" " * 30 + "d : 删除记录")
    print(" " * 30 + "c : 修改记录")
    print(" " * 30 + "f : 查找记录")
    print(" " * 30 + "s : 展示记录")
    print(" " * 30 + "q : 退出系统")
    print("\n")

def main():
    """
    [cite: 5] 实验主函数，通过实现通讯录管理系统，练习python中函数的定义、调用等知识。
    """
    while True:
        show_main_menu()
        #  敲击键盘的a, d, c, f ,s 可对应执行相关操作
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
            print("感谢使用 NKCS InfoSystem V0.1，再见！")
            break
        else:
            # [cite: 36] 如果输入的值不符合要求，需要进行提示
            print("输入代号无效，请重新输入 (a, d, c, f, s, q)")
        
        input("\n按回车键返回主菜单...")

if __name__ == "__main__":
    main()