import sqlite3
import os

# 创建数据库文件
db_file = 'world_geo.db'
if os.path.exists(db_file):
    os.remove(db_file)

# 连接到数据库
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# 创建城市表
cursor.execute('''
CREATE TABLE cities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    country TEXT NOT NULL,
    population INTEGER,
    latitude REAL,
    longitude REAL
)
''')

# 创建河流表
cursor.execute('''
CREATE TABLE rivers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    length_km INTEGER,
    countries TEXT
)
''')

# 创建河流-城市关联表
cursor.execute('''
CREATE TABLE river_cities (
    river_id INTEGER,
    city_id INTEGER,
    FOREIGN KEY (river_id) REFERENCES rivers (id),
    FOREIGN KEY (city_id) REFERENCES cities (id),
    PRIMARY KEY (river_id, city_id)
)
''')

# 插入示例城市数据
cities_data = [
    ('北京', '中国', 21540000, 39.9042, 116.4074),
    ('上海', '中国', 24870000, 31.2304, 121.4737),
    ('纽约', '美国', 8419000, 40.7128, -74.0060),
    ('伦敦', '英国', 8982000, 51.5074, -0.1278),
    ('巴黎', '法国', 2148000, 48.8566, 2.3522),
    ('开罗', '埃及', 9539000, 30.0444, 31.2357),
    ('重庆', '中国', 31020000, 29.4316, 106.9123),
    ('武汉', '中国', 11210000, 30.5928, 114.3055)
]

cursor.executemany('INSERT INTO cities (name, country, population, latitude, longitude) VALUES (?, ?, ?, ?, ?)', cities_data)

# 插入示例河流数据
rivers_data = [
    ('长江', 6300, '中国'),
    ('黄河', 5464, '中国'),
    ('尼罗河', 6650, '埃及,苏丹,埃塞俄比亚'),
    ('亚马逊河', 6400, '巴西,秘鲁,哥伦比亚'),
    ('密西西比河', 3730, '美国')
]

cursor.executemany('INSERT INTO rivers (name, length_km, countries) VALUES (?, ?, ?)', rivers_data)

# 插入河流-城市关联数据
cursor.execute('SELECT id FROM cities WHERE name = "重庆"')
chongqing_id = cursor.fetchone()[0]
cursor.execute('SELECT id FROM cities WHERE name = "武汉"')
wuhan_id = cursor.fetchone()[0]
cursor.execute('SELECT id FROM rivers WHERE name = "长江"')
yangtze_id = cursor.fetchone()[0]

cursor.execute('SELECT id FROM cities WHERE name = "开罗"')
cairo_id = cursor.fetchone()[0]
cursor.execute('SELECT id FROM rivers WHERE name = "尼罗河"')
nile_id = cursor.fetchone()[0]

river_cities_data = [
    (yangtze_id, chongqing_id),
    (yangtze_id, wuhan_id),
    (nile_id, cairo_id)
]

cursor.executemany('INSERT INTO river_cities (river_id, city_id) VALUES (?, ?)', river_cities_data)

# 提交更改并关闭连接
conn.commit()
conn.close()

print('数据库初始化完成！')