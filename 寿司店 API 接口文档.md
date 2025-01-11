# 寿司店 API 接口文档

## 基础信息
- 基础URL: `http://localhost:5001/api`
- 所有请求和响应数据格式均为 `application/json`
- 响应格式统一为：
  ```typescript
  {
    status: 'success' | 'error',
    data?: any,
    message?: string
  }
  ```

## 1. 用户认证接口

### 1.1 用户注册
- 接口：`POST /auth/register`
- 描述：新用户注册
- 请求体：
  ```typescript
  {
    username: string,  // 用户名
    password: string   // 密码
  }
  ```
- 响应示例：
  ```json
  {
    "status": "success",
    "message": "注册成功"
  }
  ```
- 错误响应：
  ```json
  {
    "status": "error",
    "message": "用户名已存在"
  }
  ```

### 1.2 用户登录
- 接口：`POST /auth/login`
- 描述：用户登录
- 请求体：
  ```typescript
  {
    username: string,  // 用户名
    password: string   // 密码
  }
  ```
- 响应示例：
  ```json
  {
    "status": "success",
    "message": "登录成功",
    "user_id": 1
  }
  ```
- 错误响应：
  ```json
  {
    "status": "error",
    "message": "用户名或密码错误"
  }
  ```

## 2. 寿司菜单接口

### 2.1 获取所有寿司
- 接口：`GET /sushi/`
- 描述：获取所有寿司列表
- 响应示例：
  ```json
  {
    "status": "success",
    "data": [
      {
        "name": "三文鱼寿司",
        "image": "controllers/sushi_img/salmon_sushi.jpg",
        "price": 28
      }
    ]
  }
  ```

### 2.2 搜索寿司
- 接口：`GET /sushi/search`
- 描述：根据关键词搜索寿司
- 查询参数：
  - `keyword`: string (搜索关键词)
- 请求示例：`GET /sushi/search?keyword=三文鱼`
- 响应示例：同 2.1

### 2.3 获取寿司详情
- 接口：`GET /sushi/detail`
- 描述：获取寿司的详细信息
- 查询参数：
  - `sushi_name`: string (寿司名称)
- 响应示例：
  ```json
  {
    "status": "success",
    "data": {
      "content": "# 金枪鱼寿司\n\n制作步骤..."
    }
  }
  ```

## 3. 寿司互动接口

### 3.1 获取寿司状态
- 接口：`GET /sushi/actions/status/{sushi_name}`
- 描述：获取寿司的点赞、评论数等状态
- 查询参数：
  - `username`: string (可选，用户名)
- 响应示例：
  ```json
  {
    "likes_count": 10,
    "comments_count": 5,
    "average_score": 4.5,
    "user_status": {
      "has_liked": true,
      "has_favorited": false
    }
  }
  ```

### 3.2 点赞操作
#### 点赞
- 接口：`POST /sushi/actions/like`
- 描述：对寿司进行点赞
- 请求体：
  ```typescript
  {
    username: string,
    sushi_name: string
  }
  ```
- 响应示例：
  ```json
  {
    "status": "success",
    "message": "点赞成功"
  }
  ```

#### 取消点赞
- 接口：`POST /sushi/actions/unlike`
- 描述：取消寿司点赞
- 请求体：同点赞接口
- 响应示例：
  ```json
  {
    "status": "success",
    "message": "取消点赞成功"
  }
  ```

### 3.3 收藏操作
#### 收藏
- 接口：`POST /sushi/actions/favorite`
- 描述：收藏寿司
- 请求体：
  ```typescript
  {
    username: string,
    sushi_name: string
  }
  ```
- 响应示例：同点赞接口

#### 取消收藏
- 接口：`POST /sushi/actions/unfavorite`
- 描述：取消收藏寿司
- 请求体：同收藏接口
- 响应示例：同点赞接口

### 3.4 评论功能
#### 添加评论
- 接口：`POST /sushi/actions/comment`
- 描述：添加寿司评论
- 请求体：
  ```typescript
  {
    username: string,
    sushi_name: string,
    content: string,
    score: number  // 1-5分
  }
  ```
- 响应示例：
  ```json
  {
    "status": "success",
    "message": "评论成功"
  }
  ```

#### 获取评论列表
- 接口：`GET /sushi/actions/comments/{sushi_name}`
- 描述：获取寿司的评论列表
- 响应示例：
  ```json
  {
    "comments": [
      {
        "id": 1,
        "username": "user1",
        "content": "非常好吃",
        "score": 5,
        "created_at": "2024-01-12 15:30:00"
      }
    ]
  }
  ```

### 3.5 用户互动记录
#### 获取用户点赞列表
- 接口：`GET /sushi/actions/user/likes/{username}`
- 描述：获取用户点赞过的寿司列表
- 响应示例：
  ```json
  {
    "likes": ["金枪鱼寿司", "三文鱼寿司"]
  }
  ```

#### 获取用户收藏列表
- 接口：`GET /sushi/actions/user/favorites/{username}`
- 描述：获取用户收藏的寿司列表
- 响应示例：
  ```json
  {
    "favorites": ["金枪鱼寿司", "三文鱼寿司"]
  }
  ```

## Vue3 代码示例

```typescript
// api/index.ts
import axios from 'axios'

const API_BASE_URL = 'http://localhost:5001/api'

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json'
  }
})

// 原有的 API
export const authApi = {
  register(username: string, password: string) {
    return api.post('/auth/register', { username, password })
  },
  login(username: string, password: string) {
    return api.post('/auth/login', { username, password })
  }
}

export const sushiApi = {
  getAllSushi() {
    return api.get('/sushi/')
  },
  searchSushi(keyword: string) {
    return api.get('/sushi/search', { params: { keyword } })
  }
}

// 新增互动 API
export const interactionApi = {
  getSushiStatus(sushiName: string, username?: string) {
    return api.get(`/sushi/actions/status/${sushiName}`, {
      params: { username }
    })
  },
  likeSushi(username: string, sushiName: string) {
    return api.post('/sushi/actions/like', { username, sushi_name: sushiName })
  },
  unlikeSushi(username: string, sushiName: string) {
    return api.post('/sushi/actions/unlike', { username, sushi_name: sushiName })
  },
  favoriteSushi(username: string, sushiName: string) {
    return api.post('/sushi/actions/favorite', { username, sushi_name: sushiName })
  },
  unfavoriteSushi(username: string, sushiName: string) {
    return api.post('/sushi/actions/unfavorite', { username, sushi_name: sushiName })
  },
  addComment(username: string, sushiName: string, content: string, score: number) {
    return api.post('/sushi/actions/comment', {
      username,
      sushi_name: sushiName,
      content,
      score
    })
  },
  getComments(sushiName: string) {
    return api.get(`/sushi/actions/comments/${sushiName}`)
  },
  getUserLikes(username: string) {
    return api.get(`/sushi/actions/user/likes/${username}`)
  },
  getUserFavorites(username: string) {
    return api.get(`/sushi/actions/user/favorites/${username}`)
  }
}
```

## 注意事项
1. 所有接口都返回统一的响应格式
2. 图片URL需要与后端服务器URL拼接
3. 建议使用 TypeScript 定义接口类型
4. 后端已配置 CORS，前端可直接访问
5. 建议使用 Pinia 或 Vuex 管理用户状态
6. 注意处理图片加载失败的情况
7. 互动功能需要用户登录才能使用
8. 用户只能对同一个寿司点赞/收藏一次
9. 评分必须在 1-5 分之间
10. 评论提交后不可修改或删除