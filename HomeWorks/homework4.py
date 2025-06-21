# def square_result(user):
#     def wrapper(*args, **kwargs):
#         solving = user(*args, **kwargs)
#         return solving ** 2
#     return wrapper
#
#
# @square_result
# def add(a, b):
#    return a + b
#
# print(add(2, 3))





def check_user(user):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if user == "admin":
                return func(*args, **kwargs)
            elif user:
                print("У вас нету доступа! Доступно только для admin.")
        return wrapper
    return decorator



@check_user("admin")
def delete_database():
    print("База данных удалена!")

@check_user("guest")
def delete_logs():
    print("Логи удалены!")

delete_database()
delete_logs()
