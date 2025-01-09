# 寿司店项目数据库设置

## 环境要求
- Python 3.7+
- MySQL 5.7+
- pymysql

## 安装步骤

1. 打开文件目录运行
```bash
python app.py
```
3. 缺什么pip什么（
4. 数据库
```bash
   -- 创建数据库
CREATE DATABASE IF NOT EXISTS sushi_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- 使用数据库
USE sushi_db;

-- 创建用户表
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(80) NOT NULL UNIQUE,
    password VARCHAR(120),
    UNIQUE INDEX idx_username (username)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```
