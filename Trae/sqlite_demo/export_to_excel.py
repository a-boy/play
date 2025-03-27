import sqlite3
import pandas as pd

# 连接到数据库
conn = sqlite3.connect('world_geo.db')

# 查询城市数据
cities_df = pd.read_sql_query("""
    SELECT name as '城市名称', 
           country as '所属国家', 
           population as '人口数量',
           latitude as '纬度',
           longitude as '经度'
    FROM cities
    ORDER BY country, name
""", conn)

# 查询河流数据
rivers_df = pd.read_sql_query("""
    SELECT name as '河流名称', 
           length_km as '长度(公里)', 
           countries as '流经国家'
    FROM rivers
    ORDER BY length_km DESC
""", conn)

# 查询河流-城市关联数据
river_cities_df = pd.read_sql_query("""
    SELECT 
        r.name as '河流名称',
        c.name as '城市名称',
        c.country as '所属国家'
    FROM river_cities rc
    JOIN rivers r ON rc.river_id = r.id
    JOIN cities c ON rc.city_id = c.id
    ORDER BY r.name, c.name
""", conn)

# 创建Excel写入器
with pd.ExcelWriter('world_geography.xlsx', engine='openpyxl') as writer:
    # 写入城市数据
    cities_df.to_excel(writer, sheet_name='城市', index=False)
    
    # 写入河流数据
    rivers_df.to_excel(writer, sheet_name='河流', index=False)
    
    # 写入河流-城市关联数据
    river_cities_df.to_excel(writer, sheet_name='河流城市关系', index=False)

# 关闭数据库连接
conn.close()

print('数据已成功导出到 world_geography.xlsx 文件！')