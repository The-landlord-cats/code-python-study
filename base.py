def calculator():
    number_one = int(input("请输入第一个数字:"))
    number_two = int(input("请输入第二个数字:"))
    tool = input("请输入运算符(+、-、*、/):")
    lst_tool = ['+', '-', '*', '/']
    if tool in lst_tool:
        print("计算结果是:%s %s %s = %s" % (number_one, tool, number_two, eval(f"{number_one}{tool}{number_two}")))
    else:
        print(f"错误！不支持的运算符{tool},仅支持(+、-、*、/)")
calculator()