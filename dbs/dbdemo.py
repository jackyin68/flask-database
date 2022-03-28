from dbs.dbop import query_by_id, query_count, query_all, query_by_filter, rows_add_by_dict, delete_by_id, \
    delete_by_filter, update_by_filter


# 添加
def add_demo():
    student_01 = ("Student", {"name": "周星驰", "gender": "男", "phone": "1382101xxx"})
    student_02 = ("Student", {"name": "张曼玉", "gender": "女", "phone": "1523321xxx"})
    students = [student_01, student_02]
    rst = rows_add_by_dict(students)
    print("rows_add_by_dict: ", rst)


# 删除
def delete_demo():
    rst = delete_by_id("Student", 4)
    print("delete_by_id: ", rst)
    rst = delete_by_filter("Teacher", ["id>0", "name=='王老师'"])
    print("delete_by_filter: ", rst)


# 更新
def updata_demo():
    rst = update_by_filter("Teacher", ["id>0", "name=='陆老师'"], update_dict={"name": "尹老师"})
    print("update_by_filter: ", rst)


# 查找
def query_demo():
    rst = query_by_id("Student", 1)
    print("query_by_id: ", rst)
    rst = query_all("Teacher")
    print("query_all: ", rst)
    rst = query_count("Teacher")
    print("query_count: ", rst)
    rst = query_by_filter("Teacher", ["id>=1"])
    print("query_by_filter: ", rst)
    rst = query_by_filter("Teacher", ["id>1", "name=='王老师'"])
    print("query_by_filter: ", rst)


if __name__ == '__main__':
    add_demo()
    delete_demo()
    updata_demo()
    query_demo()
