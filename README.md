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
CREATE DATABASE sushi_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE sushi_db;

-- 1. 创建用户表
CREATE TABLE users (
    username VARCHAR(80) NOT NULL,
    password VARCHAR(120),
    PRIMARY KEY (username)
);

-- 2. 创建点赞表
CREATE TABLE likes (
    username VARCHAR(80) NOT NULL,
    sushi_name VARCHAR(50) NOT NULL,
    PRIMARY KEY (username, sushi_name),
    FOREIGN KEY (username) REFERENCES users(username)
);

-- 3. 创建收藏表
CREATE TABLE favorites (
    username VARCHAR(80) NOT NULL,
    sushi_name VARCHAR(50) NOT NULL,
    PRIMARY KEY (username, sushi_name),
    FOREIGN KEY (username) REFERENCES users(username)
);

-- 4. 创建评论表
CREATE TABLE comments (
    id INT NOT NULL AUTO_INCREMENT,
    username VARCHAR(80) NOT NULL,
    sushi_name VARCHAR(50) NOT NULL,
    content TEXT NOT NULL,
    score TINYINT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    FOREIGN KEY (username) REFERENCES users(username),
    INDEX idx_sushi (sushi_name)
);
```
