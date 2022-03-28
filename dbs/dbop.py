from dbs.dbcreate import db, Student, Teacher, Course, Grade

file_name = "dbcreate"
modules = __import__(file_name)


# 添加记录
def rows_add(objects):
    rst = db.session.add_all(objects)
    db.session.commit()
    return rst


# 根据词典添加记录
def rows_add_by_dict(objects):
    object_list = []
    for object in objects:
        table_class = getattr(modules, object[0])
        object_list.extend([table_class(**object[1])])
    rst = rows_add(object_list)
    return rst


# 根据id主键获取数据
def query_by_id(class_name, id):
    table_class = getattr(modules, class_name)
    rst = table_class.query.get(id)
    return rst


# 获取表内所有数据
def query_all(class_name):
    table_class = getattr(modules, class_name)
    rst = table_class.query.all()
    return rst


# 获取表内所有数据的个数
def query_count(class_name):
    table_class = getattr(modules, class_name)
    rst = table_class.query.count()
    return rst


# 根据条件查询数据
def query_by_filter(class_name, conditions):
    expression_str = None
    for i, condition in enumerate(conditions):
        condition = class_name + "." + condition
        if i == 0:
            expression_str = "{}.query.filter({})".format(class_name, condition)
        else:
            expression_str += ".filter({})".format(condition)

    if expression_str is None:
        rst = query_all(class_name)
    else:
        expression_str += ".all()"
        rst = eval(expression_str)
    db.session.commit()
    return rst


# 根据id删除
def delete_by_id(class_name, id):
    expression = "{0}.query.filter({0}.id == {1}).delete()".format(class_name, id)
    rst = eval(expression)
    db.session.commit()
    return rst


# 根据条件删除数据
def delete_by_filter(class_name, conditions):
    expression_str = None
    for i, condition in enumerate(conditions):
        condition = class_name + "." + condition
        if i == 0:
            expression_str = "{}.query.filter({})".format(class_name, condition)
        else:
            expression_str += ".filter({})".format(condition)

    if expression_str is None:
        rst = None
    else:
        expression_str += ".delete()"
        rst = eval(expression_str)
    db.session.commit()
    return rst

# 根据条件更新
def update_by_filter(class_name,conditions,update_dict):
    expression_str = None
    for i, condition in enumerate(conditions):
        condition = class_name + "." + condition
        if i == 0:
            expression_str = "{}.query.filter({})".format(class_name, condition)
        else:
            expression_str += ".filter({})".format(condition)

    if expression_str is None:
        rst = None
    else:
        expression_str += ".update({})".format(update_dict)
        rst = eval(expression_str)
    db.session.commit()
    return rst