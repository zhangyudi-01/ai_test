# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


# def print_hi(name):
#     # 在下面的代码行中使用断点来调试脚本。
#     print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。

# match_sport_names = {1: "足球", 2: "篮球"}
match_id = '25041'
warning_map = {'25041':None}
warning = warning_map.get(match_id) or []
print(warning)