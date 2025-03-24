import random
import csv
from faker import Faker
from datetime import datetime
import uuid

# 初始化 Faker 生成器
fake = Faker("zh_CN")

# 预定义浏览器和操作系统列表
browsers = ["Edge", "Chrome", "Safari", "Firefox"]
os_list = ["安卓", "win", "ios", "macOS", "linux"]
websites = ["github.com", "douyin.com", "qq.com", "aliyun.com", "xiaohongshu.com", "jd.com", "taobao.com", "baidu.com", "bilibili.com", "weibo.com"]

# 生成随机数据
def generate_data(start_id, num_records):
    data = []
    for i in range(start_id, start_id + num_records):
        ip_address = fake.ipv4()  # 随机生成一个IPv4地址
        ip_location = fake.province()  # 省份信息
        login_time = fake.date_time_between_dates(datetime(2025, 1, 1), datetime(2025, 12, 31)).strftime("%Y-%m-%d %H:%M:%S")
        website = random.choice(websites)
        user_uid = random.randint(100000, 999999)
        session_id = str(uuid.uuid4())
        browser = random.choice(browsers)
        login_os = random.choice(os_list)
        stay_time = random.randint(5, 600)  # 5秒 - 10分钟

        # 生成一条数据
        data.append([i, ip_address, ip_location, login_time, website, user_uid, session_id, browser, login_os, stay_time])
    
    return data

# 用户输入起始ID和结束ID
start_id = int(input("请输入起始ID: "))
end_id = int(input("请输入结束ID: "))

# 计算数据条数
num_records = end_id - start_id + 1
data_per_file = 1000  # 每个文件的数据条数

# 分批生成数据并保存到多个CSV文件
for file_num in range(num_records // data_per_file):
    start_id_for_file = start_id + file_num * data_per_file
    end_id_for_file = start_id_for_file + data_per_file - 1
    data = generate_data(start_id_for_file, data_per_file)

    # 生成唯一文件名（时间戳 + UUID），并在文件名中包含起始ID
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    unique_id = uuid.uuid4().hex[:6]  # 取 UUID 的前6位，保证唯一性同时避免过长
    csv_filename = f"IP_data_{timestamp}_{unique_id}_from{start_id_for_file}_to{end_id_for_file}.csv"
    
    # 保存到 CSV 文件
    with open(csv_filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "IP", "IP归属地详细信息", "登录时间", "登录网址", "用户UID", "会话ID", "浏览器", "登录操作系统", "网页停留时间"])
        writer.writerows(data)

    print(f"随机数据已生成，并保存到 {csv_filename}")

# 如果数据总数不能被1000整除，还需生成一个文件
remaining_data = num_records % data_per_file
if remaining_data > 0:
    start_id_for_file = start_id + (num_records // data_per_file) * data_per_file
    end_id_for_file = start_id_for_file + remaining_data - 1
    data = generate_data(start_id_for_file, remaining_data)

    # 生成唯一文件名（时间戳 + UUID），并在文件名中包含起始ID
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    unique_id = uuid.uuid4().hex[:6]  # 取 UUID 的前6位，保证唯一性同时避免过长
    csv_filename = f"IP_data_{timestamp}_{unique_id}_from{start_id_for_file}_to{end_id_for_file}.csv"
    
    # 保存到 CSV 文件
    with open(csv_filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "IP", "IP归属地详细信息", "登录时间", "登录网址", "用户UID", "会话ID", "浏览器", "登录操作系统", "网页停留时间"])
        writer.writerows(data)

    print(f"随机数据已生成，并保存到 {csv_filename}")
1