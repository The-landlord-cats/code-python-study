import os
student_record_sum = []
student_list_sum = []
def input_student():
    while 1:
        student_id = input("请输入学号(输入stop 停止录入):")
        if student_id == "stop":
            break
        student_name = input(f"请输入学号{student_id}对应的学员姓名:")
        true_write = 0
        for i in student_list_sum:
            if i["学号"] == student_id:
                true_write = 1
                print(f"学号{student_id}已存在，请勿重复录入！")
                break
        if true_write == 0:
            student_list_sum.append({"学号":student_id, "姓名":student_name})
            print(f"学员{student_name}录入成功")
    with open("学员名单.txt", "w", encoding="utf-8") as f:
        for g in student_list_sum:
            f.write(f"{g['学号']},{g['姓名']}\n")
    return student_list_sum


def get_student():
    if os.path.exists("学员名单.txt"):
        student_list_sum.clear()
        with open("学员名单.txt", "r", encoding="utf-8") as f:
            line = f.readlines()
            for i in line:
                i = i.strip()
                if i:
                    student_id, name = i.split(",")
                    student_list_sum.append({"学号": student_id, "姓名": name})
        print("===== 学员名单已从文件加载 =====\n")
    else:
        print("暂无学员名单文件，请先初始化学员名单！\n")


def collection_call():
    if not student_list_sum:
        print("暂无学员信息，请先加载/初始化学员名单！\n")
        pass
    student_record_sum.clear()
    date = input("请输入本次点名日期:")
    for i in student_list_sum:
        print(f"\n当前点名:{i['姓名']}  {i['学号']}")
        while 1:
            student_state = input("请输入出勤状态（出勤/迟到/缺勤/请假/公差）：")
            if student_state in ["出勤", "迟到", "缺勤", "请假", "公差"]:
                student_record_sum.append({
                    "学号": i["学号"],
                    "姓名": i["姓名"],
                    "状态": student_state,
                    "日期": date
                })
                print(f"{i['姓名']}记录为：{student_state}")
                break
            else:
                print("输入错误！请输入：出勤/迟到/缺勤/请假/公差 中的一种\n")
    with open(f"考勤记录_{date}.txt", "w", encoding="utf-8") as f:
        f.write(f"日期：{date}\n")
        f.write("学号,姓名,状态\n")
        for i in student_record_sum:
            f.write({"学号":i["学号"],"姓名":i["姓名"],"状态":i["状态"]})
    print("===== 本次点名完成，考勤记录已保存 =====\n")
    return date


def id_name():
    ask_id = input("输入想查询对应名字的学号:")
    ask_name = 0
    if os.path.exists("学员名单.txt"):
        student_list_sum.clear()
        with open("学员名单.txt", "r", encoding="utf-8") as f:
            line = f.readlines()
            for i in line:
                i = i.strip()
                if i:
                    student_id, name = i.split(",")
                    student_list_sum.append({"学号": student_id, "姓名": name})
    student_record_sum_dict = eval(student_list_sum)
    for i in student_record_sum_dict:
        if i["学号"] == ask_id:
            ask_name = i["姓名"]
    print(f"您要查询的学号{ask_id}对应学员的名字是{ask_name}")


def student_person_record_ask(date):
    target_name = input("请输入要查询的姓名:")
    target_state = input("请输入要统计的状态(例如:出勤/迟到/缺勤/请假/公差):")
    count = 0
    with open(f"考勤记录_{date}.txt", "r", encoding="utf-8") as f:
        line = f.readlines()      
        for line_num, i in enumerate(line, 1):
            i = i.strip()  
            if not i:  
                continue
            dic_true = eval(line)
            if isinstance(dic_true, dict) and "姓名" in dic_true and "状态" in dic_true:
                if dic_true["姓名"] == target_name and dic_true["状态"] == target_state:
                        count += 1
                print(f"第{line_num}行匹配：{dic_true}")
        print(f"===== 统计结果 =====\n")
        print(f"姓名：{target_name}")
        print(f"状态：{target_state}")
        print(f"出现次数：{count}")
        

def show_record():
    if not student_record_sum:
        print("暂无本次考勤记录，请先完成点名！\n")
        pass
    print("===== 本次考勤统计结果 =====\n")
    sum = len(student_record_sum)
    come = 0  # 出勤
    late = 0     # 迟到
    absent = 0   # 缺勤
    leave = 0    # 请假
    tolreance = 0 # 公差
    for i in student_record_sum:
        if i["状态"] == "出勤":
            come += 1
        elif i["状态"] == "迟到":
            late += 1
        elif i["状态"] == "缺勤":
            absent += 1
        elif i["状态"] == "请假":
            leave += 1
        elif i["状态"] == "公差":
            tolreance += 1
    print(f"应到人数：{sum}")
    print(f"出勤人数：{come}")
    print(f"迟到人数：{late}")
    print(f"缺勤人数：{absent}")
    print(f"请假人数：{leave}")
    print(f"公差人数：{tolreance}")
    print("\n===== 详细考勤名单 =====")
    for g in student_record_sum:
        print(f"{g['学号']}\t{g['姓名']}\t{g['状态']}")
    print("\n")


def main():
    while 1:
        print("===== 空军航空大学学员管理系统 =====")
        print("1. 初始化学员名单（录入+保存）")
        print("2. 加载学员名单")
        print("3. 队列点名")
        print("4. 查看本次考勤统计")
        print("5. 查询单个学员任一出勤状态次数")
        print("6. 查询已知学号的学员姓名")
        print("7. 退出系统")
        print("=" * 20)

        i = input("请输入操作序号(1-7):")
        if i == "1":
            input_student()
        elif i == "2":
            get_student()
        elif i == "3":
            collection_call()
        elif i == "4":
            show_record()
        elif i == "5":
            student_person_record_ask()
        elif i == "6":
            id_name()
        elif i == "7":
            print("感谢使用，系统退出！")
            break
        else:
            print("输入错误,请输入1-7的序号\n")


if __name__ == "__main__":
    print("欢迎使用空军航空大学学员管理系统\n")
    main()


