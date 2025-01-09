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
- 参数：无
- 响应示例：
  ```json
  {
    "status": "success",
    "data": [
      {
        "name": "三文鱼寿司",
        "image": "controllers/sushi_img/salmon_sushi.jpg",
        "price": 28
      },
      {
        "name": "金枪鱼寿司",
        "image": "controllers/sushi_img/tuna_sushi.jpg",
        "price": 25
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
    return api.get('/sushi/search', {
      params: { keyword }
    })
  }
}
```

```vue
<!-- components/SushiList.vue -->
<template>
  <div class="sushi-container">
    <!-- 搜索框 -->
    <div class="search-box">
      <el-input 
        v-model="searchKeyword" 
        placeholder="搜索寿司"
        @change="handleSearch"
      />
    </div>
    
    <!-- 寿司列表 -->
    <el-row :gutter="20">
      <el-col 
        v-for="sushi in sushiList" 
        :key="sushi.name"
        :xs="24" 
        :sm="12" 
        :md="8" 
        :lg="6"
      >
        <el-card class="sushi-card">
          <img :src="sushi.image" :alt="sushi.name">
          <h3>{{ sushi.name }}</h3>
          <p class="price">￥{{ sushi.price.toFixed(2) }}</p>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { sushiApi } from '@/api'

const sushiList = ref([])
const searchKeyword = ref('')

const loadSushiList = async () => {
  try {
    const response = await sushiApi.getAllSushi()
    sushiList.value = response.data.data
  } catch (error) {
    console.error('加载寿司列表失败:', error)
  }
}

const handleSearch = async () => {
  try {
    if (!searchKeyword.value.trim()) {
      await loadSushiList()
      return
    }
    const response = await sushiApi.searchSushi(searchKeyword.value)
    sushiList.value = response.data.data
  } catch (error) {
    console.error('搜索寿司失败:', error)
  }
}

onMounted(loadSushiList)
</script>
```

### 注意事项
1. 所有接口都返回统一的响应格式
2. 图片URL需要与后端服务器URL拼接
3. 建议使用 TypeScript 定义接口类型
4. 后端已配置 CORS，前端可直接访问
5. 建议使用 Pinia 或 Vuex 管理用户状态
6. 注意处理图片加载失败的情况

