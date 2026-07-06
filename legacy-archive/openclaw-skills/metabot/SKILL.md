---
name: metabot
description: MetaBot management skill for Feishu (飞书) bot operations. Start, stop, restart MetaBot service, check status, view logs, and manage configuration.
---

# MetaBot Management Skill

MetaBot 是一个飞书机器人桥接服务，将飞书消息连接到 Claude Code Agent SDK。此技能用于管理和操作 MetaBot 服务。

## 何时使用此技能

当用户：
- 提到 MetaBot、飞书机器人
- 需要启动、停止、重启 MetaBot 服务
- 查看 MetaBot 状态或日志
- 修改飞书配置或 API 密钥
- 遇到飞书机器人不响应的问题

## ⚠️ 关键：启动 MetaBot 的正确方式

**始终使用 `metabot` CLI 命令**，不要直接运行 PM2：

```bash
# ✅ 正确 - 使用 metabot CLI
metabot start      # 启动
metabot stop       # 停止
metabot restart    # 重启
metabot status     # 查看状态
metabot logs -n 50 # 查看最近 50 行日志

# ❌ 错误 - 不要直接使用 PM2
pm2 start metabot  # 可能缺少环境变量
```

## 核心工作流

### 1. 启动 MetaBot

```bash
metabot start
```

启动后应该看到：
- `status: online`
- `Feishu bot is running`
- `Bot info fetched`

### 2. 检查状态

```bash
metabot status
```

正常状态：
- `status: online` - 服务运行中
- `uptime: Xs` - 运行时间
- `restarts: 0` - 重启次数

异常状态：
- `status: errored` - 有错误，需要查看日志
- `status: stopped` - 服务已停止

### 3. 查看日志

```bash
# 查看最近 50 行日志
metabot logs -n 50

# 实时跟踪日志
metabot logs
```

常见日志信息：
- `Bot info fetched` - 飞书认证成功
- `Feishu bot is running` - 飞书机器人运行中
- `Failed to fetch bot info` - 认证失败，检查密钥
- `EADDRINUSE` - 端口被占用，需要清理

### 4. 重启服务

```bash
metabot restart
```

配置修改后必须重启才能生效。

### 5. 停止服务

```bash
metabot stop
```

## 配置文件位置

### 1. 主配置文件 (.env)
**路径**: `C:\Users\Administrator\metabot\.env`

包含飞书密钥、AI API 配置等核心信息：

```bash
# 查看配置
cat C:/Users/Administrator/metabot/.env
```

**关键字段**:
| 配置项 | 说明 |
| ------ | ---- |
| `FEISHU_APP_ID` | 飞书 App ID |
| `FEISHU_APP_SECRET` | 飞书 App Secret |
| `ANTHROPIC_AUTH_TOKEN` | AI API 密钥 |
| `ANTHROPIC_BASE_URL` | AI API 地址 |
| `API_PORT` | API 服务端口 (默认 9100) |

### 2. PM2 配置文件
**路径**: `C:\Users\Administrator\metabot\ecosystem.config.cjs`

包含 `NO_PROXY` 环境变量配置，确保飞书 API 请求不经过代理。

## 故障排查

### 问题 1：飞书发信息没人回

**可能原因**：
1. MetaBot 服务未运行
2. 飞书 API 认证失败
3. WebSocket 连接断开

**解决步骤**：
```bash
# 1. 检查状态
metabot status

# 2. 如果 stopped，启动服务
metabot start

# 3. 如果 errored，查看日志
metabot logs -n 100

# 4. 查看是否有认证错误
metabot logs | grep -i "400\|error\|failed"
```

### 问题 2：认证失败 (400 错误)

日志中出现：
```
AxiosError: Request failed with status code 400
The plain HTTP request was sent to HTTPS port
```

**原因**：系统代理配置导致飞书 API 请求被路由到本地代理。

**解决**：
1. 确认 `ecosystem.config.cjs` 中 `NO_PROXY` 配置正确
2. 重启服务：`metabot restart`

### 问题 3：端口被占用

日志中出现：
```
Error: listen EADDRINUSE: address already in use 0.0.0.0:9100
```

**解决**：
```bash
# 1. 查找占用端口的进程
netstat -ano | findstr :9100

# 2. 杀掉旧进程
taskkill /F /PID <PID>

# 3. 重启 MetaBot
metabot restart
```

## 命令速查

| 命令 | 说明 |
| ---- | ---- |
| `metabot start` | 启动服务 |
| `metabot stop` | 停止服务 |
| `metabot restart` | 重启服务 |
| `metabot status` | 查看状态 |
| `metabot logs -n 50` | 查看最近 50 行日志 |
| `metabot logs` | 实时跟踪日志 |

## 飞书机器人配置

### 飞书开发者后台设置

1. **创建应用**: https://open.feishu.cn/app
2. **添加机器人能力**
3. **配置权限**：
   - `im:message` - 读取和发送消息
   - `im:message:readonly` - 只读消息
   - `im:resource` - 上传图片/文件
4. **配置事件订阅**：
   - 订阅方式：选择「使用长连接接收事件/回调」
   - 添加事件：`im.message.receive_v1`
5. **发布应用**

### 修改飞书密钥

1. 编辑 `C:/Users/Administrator/metabot/.env`
2. 修改 `FEISHU_APP_ID` 和 `FEISHU_APP_SECRET`
3. 重启：`metabot restart`

## 决策流程

```
用户提到 MetaBot/飞书机器人
    ↓
检查状态 → metabot status
    ↓
如果 stopped → metabot start
如果 errored → metabot logs -n 100 → 根据错误排查
    ↓
正常运行 → 查看日志确认无错误
    ↓
飞书测试 → 发送消息验证响应
```

## 常见问题

| 问题 | 解决方案 |
| ---- | ---- |
| 服务启动失败 | 检查日志 `metabot logs` |
| 飞书不响应 | 检查状态、日志、事件订阅配置 |
| 400 认证错误 | 检查密钥、NO_PROXY 配置 |
| 端口占用 | 杀掉旧进程后重启 |
| WebSocket 断开 | 检查网络连接、重启服务 |

## 最佳实践

1. **始终使用 metabot CLI** - 自动处理环境变量和 PM2 配置
2. **配置修改后重启** - `.env` 或 `ecosystem.config.cjs` 修改后必须重启
3. **查看日志排查问题** - `metabot logs -n 100` 是首选调试工具
4. **定期检查状态** - 确保服务在线运行
