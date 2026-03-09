# GitHub Local Skill

本地 GitHub 专用技能，集成所有配置和操作指南。

## 用户配置

| 配置项 | 值 |
|--------|-----|
| GitHub 用户名 | `ins13014778` |
| 邮箱 | `478201690@qq.com` |
| SSH 密钥类型 | `ed25519` |
| SSH 公钥 | `ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAINH4BwyM1z5upw8UbsIxLwNUYX5JnRDGPiJj/FvQvgK0` |
| HTTP/HTTPS 代理 | `http://127.0.0.1:7897` |

## 连接状态

- ✅ **SSH 连接**: 已认证，可正常使用 `git@github.com` 方式操作
- ✅ **GitHub CLI (gh)**: 已登录，可直接使用所有 gh 命令

---

## 常用操作

### 仓库克隆

```bash
# SSH 方式（推荐）
git clone git@github.com:ins13014778/REPO_NAME.git

# HTTPS 方式（需要代理）
git clone https://github.com/ins13014778/REPO_NAME.git
```

### 提交与推送

```bash
# 标准流程
git add .
git commit -m "feat: 描述信息"
git push origin main

# 强制推送（谨慎使用）
git push -f origin main
```

### 分支操作

```bash
# 创建并切换分支
git checkout -b feature/new-feature

# 合并分支
git checkout main
git merge feature/new-feature

# 删除本地分支
git branch -d feature/new-feature

# 删除远程分支
git push origin --delete feature/new-feature
```

### 撤销操作

```bash
# 撤销最后一次提交（保留更改）
git reset --soft HEAD~1

# 撤销最后一次提交（丢弃更改）
git reset --hard HEAD~1

# 撤销工作区更改
git checkout -- FILE_PATH
```

---

## GitHub CLI (gh) 操作

### 当前登录状态

- ✅ **已登录账户**: `ins13014778`
- ✅ **Git 协议**: SSH
- ✅ **Token 权限**: `gist`, `read:org`, `repo`

### 首次登录（已完成，仅供参考）

```bash
# 设置代理（必须，否则无法连接）
$env:HTTP_PROXY="http://127.0.0.1:7897"
$env:HTTPS_PROXY="http://127.0.0.1:7897"

# 登录
gh auth login
# 选择: GitHub.com -> SSH -> Use existing SSH key -> id_ed25519 -> Login with a web browser
# 复制 one-time code -> 打开浏览器 -> 输入 code -> 授权
```

### 永久代理设置（已完成）

```powershell
# 已写入用户环境变量，新窗口自动生效
[Environment]::SetEnvironmentVariable("HTTP_PROXY", "http://127.0.0.1:7897", "User")
[Environment]::SetEnvironmentVariable("HTTPS_PROXY", "http://127.0.0.1:7897", "User")
```

### 常用命令

```bash
# 查看认证状态
gh auth status

# 查看当前用户仓库
gh repo list ins13014778

# 创建新仓库
gh repo create REPO_NAME --private --source=. --push

# 创建 Pull Request
gh pr create --title "PR标题" --body "PR描述"

# 查看 PR 列表
gh pr list

# 查看 Issue 列表
gh issue list

# 创建 Issue
gh issue create --title "标题" --body "内容"

# 克隆仓库（简写）
gh repo clone ins13014778/REPO_NAME
```

---

## 代理配置

当前已配置代理 `http://127.0.0.1:7897`

### Git 代理（已配置）

```bash
# 查看当前代理
git config --global --get http.proxy

# 临时取消代理
git config --global --unset http.proxy
git config --global --unset https.proxy

# 重新设置代理
git config --global http.proxy http://127.0.0.1:7897
git config --global https.proxy http://127.0.0.1:7897
```

### 系统代理（已永久配置）

```powershell
# 查看当前代理环境变量
[Environment]::GetEnvironmentVariable("HTTP_PROXY", "User")
[Environment]::GetEnvironmentVariable("HTTPS_PROXY", "User")

# 临时设置（当前会话）
$env:HTTP_PROXY = "http://127.0.0.1:7897"
$env:HTTPS_PROXY = "http://127.0.0.1:7897"

# 永久设置（已配置）
[Environment]::SetEnvironmentVariable("HTTP_PROXY", "http://127.0.0.1:7897", "User")
[Environment]::SetEnvironmentVariable("HTTPS_PROXY", "http://127.0.0.1:7897", "User")

# 取消永久代理
[Environment]::SetEnvironmentVariable("HTTP_PROXY", $null, "User")
[Environment]::SetEnvironmentVariable("HTTPS_PROXY", $null, "User")
```

---

## SSH 密钥管理

### 查看公钥

```bash
cat ~/.ssh/id_ed25519.pub
```

### 测试 SSH 连接

```bash
ssh -T git@github.com
```

### 密钥位置

- 私钥: `~/.ssh/id_ed25519`
- 公钥: `~/.ssh/id_ed25519.pub`

---

## Git LFS 配置

已启用 Git LFS，用于大文件管理。

```bash
# 跟踪大文件类型
git lfs track "*.psd"
git lfs track "*.zip"

# 查看跟踪规则
git lfs track

# 推送 LFS 文件
git lfs push --all origin main
```

---

## Git 配置管理

### 全局配置文件

位置: `~/.gitconfig`

```bash
# 查看所有全局配置
git config --global --list

# 查看特定配置
git config --global user.name
git config --global user.email
```

### 用户信息配置

```bash
# 设置用户名
git config --global user.name "ins13014778"

# 设置邮箱
git config --global user.email "478201690@qq.com"

# 查看当前用户信息
git config user.name
git config user.email
```

### 凭据管理

```bash
# 记住密码（15分钟）
git config --global credential.helper cache

# 记住密码（1小时）
git config --global credential.helper 'cache --timeout=3600'

# 永久存储（Windows）
git config --global credential.helper wincred

# 永久存储（通用）
git config --global credential.helper store
```

### 编辑器配置

```bash
# 使用 VS Code 作为默认编辑器
git config --global core.editor "code --wait"

# 使用 Notepad++
git config --global core.editor "'C:/Program Files/Notepad++/notepad++.exe' -multiInst -notabbar -nosession -noPlugin"

# 使用 Vim
git config --global core.editor "vim"
```

### 差异比较工具

```bash
# 使用 VS Code 作为 diff 工具
git config --global diff.tool vscode
git config --global difftool.vscode.cmd "code --wait --diff $LOCAL $REMOTE"

# 使用 merge 工具
git config --global merge.tool vscode
git config --global mergetool.vscode.cmd "code --wait $MERGED"
```

### 别名配置

```bash
# 常用别名
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.lg "log --oneline --graph --all"
git config --global alias.last "log -1 HEAD"
git config --global alias.unstage "reset HEAD --"
git config --global alias.visual "log --graph --oneline --all --decorate"

# 使用别名
git st
git co main
git lg
```

### 换行符配置（Windows）

```bash
# 自动转换换行符（Windows推荐）
git config --global core.autocrlf true

# 强制 LF
git config --global core.autocrlf input

# 创建 .gitattributes 文件
echo "* text=auto" > .gitattributes
```

### 忽略文件配置

全局忽略文件: `~/.gitignore_global`

```bash
# 创建全局忽略文件
git config --global core.excludesfile ~/.gitignore_global

# 编辑全局忽略文件
code ~/.gitignore_global
```

常用全局忽略内容:
```
# 系统文件
.DS_Store
Thumbs.db
desktop.ini

# IDE
.idea/
.vscode/
*.swp
*.swo

# 编译产物
*.pyc
__pycache__/
node_modules/
dist/
build/

# 日志和临时文件
*.log
*.tmp
.env
.env.local
```

---

## Git 忽略规则管理

### 仓库级 .gitignore

```bash
# 创建仓库忽略文件
touch .gitignore

# 常见模板
# 忽略所有 .log 文件
*.log

# 但保留 important.log
!important.log

# 忽略 build 目录下所有文件
build/

# 忽略 doc 目录下的所有 .txt 文件
doc/**/*.txt

# 忽略根目录下的 config.env
/config.env
```

### 清除已跟踪的忽略文件

```bash
# 清除 git 缓存（让 .gitignore 生效）
git rm -r --cached .
git add .
git commit -m "chore: update .gitignore"
```

---

## Git Stash 管理

```bash
# 暂存当前修改
git stash

# 暂存并添加消息
git stash save "暂存描述"

# 查看暂存列表
git stash list

# 应用最近的暂存
git stash pop

# 应用指定暂存（保留暂存记录）
git stash apply stash@{0}

# 删除指定暂存
git stash drop stash@{0}

# 清空所有暂存
git stash clear

# 查看暂存内容
git stash show -p stash@{0}
```

---

## Git Tag 管理

```bash
# 创建轻量标签
git tag v1.0.0

# 创建带注释标签
git tag -a v1.0.0 -m "版本 1.0.0 发布"

# 查看所有标签
git tag

# 查看标签详情
git show v1.0.0

# 推送标签到远程
git push origin v1.0.0

# 推送所有标签
git push origin --tags

# 删除本地标签
git tag -d v1.0.0

# 删除远程标签
git push origin --delete v1.0.0

# 检出标签
git checkout v1.0.0

# 从标签创建分支
git checkout -b fix-v1.0.0 v1.0.0
```

---

## Git Remote 管理

```bash
# 查看远程仓库
git remote -v

# 添加远程仓库
git remote add origin git@github.com:ins13014778/REPO_NAME.git

# 修改远程仓库 URL
git remote set-url origin git@github.com:ins13014778/NEW_REPO.git

# 删除远程仓库
git remote remove origin

# 重命名远程仓库
git remote rename origin upstream

# 查看远程仓库详情
git remote show origin
```

---

## Git Log 与历史管理

```bash
# 查看提交历史
git log

# 简洁模式
git log --oneline

# 图形化显示
git log --oneline --graph --all

# 查看最近 N 条提交
git log -n 5

# 查看某个文件的历史
git log --follow FILE_PATH

# 查看某次提交的详情
git show COMMIT_HASH

# 查看某次提交的文件变更
git show --name-only COMMIT_HASH

# 搜索提交信息
git log --grep="关键词"

# 查看某个作者的提交
git log --author="ins13014778"

# 按时间范围查看
git log --since="2024-01-01" --until="2024-12-31"

# 查看每次提交的统计
git log --stat
```

---

## Git Diff 差异比较

```bash
# 查看工作区与暂存区差异
git diff

# 查看暂存区与最新提交差异
git diff --staged

# 查看两个提交之间的差异
git diff COMMIT1 COMMIT2

# 查看某个文件的差异
git diff FILE_PATH

# 查看分支间差异
git diff main feature

# 只显示文件名
git diff --name-only

# 显示统计信息
git diff --stat
```

---

## Git Blame 代码追溯

```bash
# 查看文件每行的修改信息
git blame FILE_PATH

# 查看指定行范围
git blame -L 10,20 FILE_PATH

# 显示邮箱
git blame -e FILE_PATH
```

---

## Git Rebase 变基

```bash
# 变基到 main 分支
git rebase main

# 交互式变基（压缩提交）
git rebase -i HEAD~3
# 将 pick 改为 squash 压缩提交

# 继续变基（解决冲突后）
git rebase --continue

# 跳过当前提交
git rebase --skip

# 放弃变基
git rebase --abort
```

---

## Git Cherry-pick 选择性合并

```bash
# 合并指定的提交
git cherry-pick COMMIT_HASH

# 合并多个提交
git cherry-pick COMMIT1 COMMIT2

# 合并提交范围
git cherry-pick COMMIT1..COMMIT2

# 只应用更改不提交
git cherry-pick -n COMMIT_HASH
```

---

## Git 子模块管理

```bash
# 添加子模块
git submodule add git@github.com:user/repo.git path/to/submodule

# 初始化子模块
git submodule init

# 更新子模块
git submodule update

# 克隆包含子模块的仓库
git clone --recursive git@github.com:user/repo.git

# 更新所有子模块到最新
git submodule update --remote

# 删除子模块
git submodule deinit path/to/submodule
git rm path/to/submodule
```

---

## Git GC 垃圾回收

```bash
# 手动垃圾回收
git gc

# 强制完整回收
git gc --aggressive

# 清理无效的远程分支引用
git remote prune origin

# 清理孤立对象
git prune

# 查看仓库大小
git count-objects -vH
```

---

## 常见问题处理

### 推送被拒绝

```bash
# 先拉取再推送
git pull origin main --rebase
git push origin main
```

### SSH 连接失败

```bash
# 检查 SSH agent
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# 测试连接
ssh -T git@github.com
```

### 代理问题

```bash
# 如果代理导致问题，临时关闭
git config --global --unset http.proxy
git config --global --unset https.proxy
```

---

## 快速脚本

### 一键提交

```bash
git add . && git commit -m "update: $(date +%Y%m%d%H%M%S)" && git push
```

### 查看状态

```bash
git status && git log --oneline -5
```

---

---

## Claude MCP 配置

### 配置文件位置

| 文件 | 路径 | 用途 |
|------|------|------|
| 主配置 | `~/.mcp.json` | MCP 服务器定义 |
| Claude 设置 | `~/.claude/settings.json` | API 配置、环境变量 |
| 本地设置 | `~/.claude/settings.local.json` | 权限配置 |
| Antigravity 注册 | `~/.config/antigravity-mcp/registry.json` | Antigravity 工作区注册 |

### API 配置 (settings.json)

```json
{
  "env": {
    "ANTHROPIC_AUTH_TOKEN": "sk-sp-O7V9KXexoQnKujVPTfndj9hkUoYq6FB9DYx2pvT49emScDON",
    "ANTHROPIC_BASE_URL": "https://api.lkeap.cloud.tencent.com/coding/anthropic",
    "ANTHROPIC_DEFAULT_HAIKU_MODEL": "glm-5",
    "ANTHROPIC_DEFAULT_OPUS_MODEL": "minimax-m2.5",
    "ANTHROPIC_DEFAULT_SONNET_MODEL": "kimi-k2.5",
    "ANTHROPIC_MODEL": "glm-5",
    "ANTHROPIC_REASONING_MODEL": "kimi-k2.5",
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  },
  "includeCoAuthoredBy": false
}
```

### MCP 服务器配置 (~/.mcp.json)

```json
{
  "mcpServers": {
    "antigravity-sync": {
      "command": "node",
      "args": [
        "C:\\Users\\Administrator\\.gemini\\antigravity\\scratch\\antigravity-sync-mcp\\antigravity-mcp-server\\build\\dist\\index.js"
      ],
      "env": {
        "ANTIGRAVITY_SYNC_REGISTRY": "C:\\Users\\Administrator\\.config\\antigravity-mcp\\registry.json"
      }
    },
    "mcp-chrome-bridge": {
      "type": "stdio",
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/GuDaStudio/ChromeBridgeMCP",
        "mcp-chrome-bridge"
      ]
    }
  }
}
```

---

## 可用 MCP 服务器列表

### 1. antigravity-sync

**描述**: Antigravity CDP 桥接 MCP 服务器

**工具**:
| 工具名 | 功能 |
|--------|------|
| `mcp__antigravity-sync__antigravity-stop` | 停止当前 AI 生成 |
| `mcp__antigravity-sync__ask-antigravity` | 发送 prompt 到 Antigravity 并等待响应 |
| `mcp__antigravity-sync__launch-antigravity` | 启动 Antigravity 并启用 CDP 调试端口 |
| `mcp__antigravity-sync__ping` | 测试 MCP 服务器连接 |
| `mcp__antigravity-sync__quota-status` | 查询模型配额状态 |

---

### 2. chrome-devtools-mcp

**描述**: Chrome DevTools MCP 工具

**工具**:
| 工具名 | 功能 |
|--------|------|
| `mcp__chrome-devtools-mcp__click` | 点击元素 |
| `mcp__chrome-devtools-mcp__close_page` | 关闭页面 |
| `mcp__chrome-devtools-mcp__drag` | 拖拽元素 |
| `mcp__chrome-devtools-mcp__emulate` | 模拟设备/网络 |
| `mcp__chrome-devtools-mcp__evaluate_script` | 执行 JavaScript |
| `mcp__chrome-devtools-mcp__fill` | 填充表单 |
| `mcp__chrome-devtools-mcp__fill_form` | 批量填充表单 |
| `mcp__chrome-devtools-mcp__get_console_message` | 获取控制台消息 |
| `mcp__chrome-devtools-mcp__get_network_request` | 获取网络请求详情 |
| `mcp__chrome-devtools-mcp__handle_dialog` | 处理对话框 |
| `mcp__chrome-devtools-mcp__hover` | 悬停元素 |
| `mcp__chrome-devtools-mcp__lighthouse_audit` | Lighthouse 审计 |
| `mcp__chrome-devtools-mcp__list_console_messages` | 列出控制台消息 |
| `mcp__chrome-devtools-mcp__list_network_requests` | 列出网络请求 |
| `mcp__chrome-devtools-mcp__list_pages` | 列出所有页面 |
| `mcp__chrome-devtools-mcp__navigate_page` | 导航页面 |
| `mcp__chrome-devtools-mcp__new_page` | 打开新标签页 |
| `mcp__chrome-devtools-mcp__performance_analyze_insight` | 分析性能洞察 |
| `mcp__chrome-devtools-mcp__performance_start_trace` | 开始性能追踪 |
| `mcp__chrome-devtools-mcp__performance_stop_trace` | 停止性能追踪 |
| `mcp__chrome-devtools-mcp__press_key` | 按键 |
| `mcp__chrome-devtools-mcp__resize_page` | 调整页面大小 |
| `mcp__chrome-devtools-mcp__select_page` | 选择页面 |
| `mcp__chrome-devtools-mcp__take_memory_snapshot` | 内存快照 |
| `mcp__chrome-devtools-mcp__take_screenshot` | 截图 |
| `mcp__chrome-devtools-mcp__take_snapshot` | 获取页面快照 |
| `mcp__chrome-devtools-mcp__type_text` | 输入文本 |
| `mcp__chrome-devtools-mcp__upload_file` | 上传文件 |
| `mcp__chrome-devtools-mcp__wait_for` | 等待文本出现 |

---

### 3. chrome-devtools (备用)

**描述**: Chrome DevTools 备用工具集，功能同上

---

### 4. context7

**描述**: 编程库文档查询

**工具**:
| 工具名 | 功能 |
|--------|------|
| `mcp__context7__query-docs` | 查询库文档和代码示例 |
| `mcp__context7__resolve-library-id` | 解析库名称为 Context7 ID |

---

### 5. coze-workflow

**描述**: 扣子工作流集成

**工具**:
| 工具名 | 功能 |
|--------|------|
| `mcp__coze-workflow__get_coze_workflow_info` | 查询工作流信息 |
| `mcp__coze-workflow__get_coze_workflow_status` | 查询工作流执行状态 |
| `mcp__coze-workflow__list_available_coze_workflows` | 列出可用工作流 |

---

### 6. filesystem

**描述**: 文件系统操作

**工具**:
| 工具名 | 功能 |
|--------|------|
| `mcp__filesystem__create_directory` | 创建目录 |
| `mcp__filesystem__directory_tree` | 目录树结构 |
| `mcp__filesystem__edit_file` | 编辑文件 |
| `mcp__filesystem__get_file_info` | 获取文件信息 |
| `mcp__filesystem__list_allowed_directories` | 列出允许访问的目录 |
| `mcp__filesystem__list_directory` | 列出目录内容 |
| `mcp__filesystem__list_directory_with_sizes` | 列出目录内容含大小 |
| `mcp__filesystem__move_file` | 移动/重命名文件 |
| `mcp__filesystem__read_file` | 读取文件 (已弃用) |
| `mcp__filesystem__read_media_file` | 读取媒体文件 |
| `mcp__filesystem__read_multiple_files` | 批量读取文件 |
| `mcp__filesystem__read_text_file` | 读取文本文件 |
| `mcp__filesystem__search_files` | 搜索文件 |
| `mcp__filesystem__write_file` | 写入文件 |

---

### 7. github

**描述**: GitHub API 操作

**工具**:
| 工具名 | 功能 |
|--------|------|
| `mcp__github__add_issue_comment` | 添加 Issue 评论 |
| `mcp__github__create_branch` | 创建分支 |
| `mcp__github__create_issue` | 创建 Issue |
| `mcp__github__create_or_update_file` | 创建/更新文件 |
| `mcp__github__create_pull_request` | 创建 PR |
| `mcp__github__create_pull_request_review` | 创建 PR 审查 |
| `mcp__github__create_repository` | 创建仓库 |
| `mcp__github__fork_repository` | Fork 仓库 |
| `mcp__github__get_file_contents` | 获取文件内容 |
| `mcp__github__get_issue` | 获取 Issue |
| `mcp__github__get_pull_request` | 获取 PR |
| `mcp__github__get_pull_request_comments` | 获取 PR 评论 |
| `mcp__github__get_pull_request_files` | 获取 PR 文件变更 |
| `mcp__github__get_pull_request_reviews` | 获取 PR 审查 |
| `mcp__github__get_pull_request_status` | 获取 PR 状态 |
| `mcp__github__list_commits` | 列出提交 |
| `mcp__github__list_issues` | 列出 Issues |
| `mcp__github__list_pull_requests` | 列出 PRs |
| `mcp__github__merge_pull_request` | 合并 PR |
| `mcp__github__push_files` | 推送多个文件 |
| `mcp__github__search_code` | 搜索代码 |
| `mcp__github__search_issues` | 搜索 Issues |
| `mcp__github__search_repositories` | 搜索仓库 |
| `mcp__github__search_users` | 搜索用户 |
| `mcp__github__update_issue` | 更新 Issue |
| `mcp__github__update_pull_request_branch` | 更新 PR 分支 |

---

### 8. grok-search

**描述**: Grok 网络搜索 (强制使用)

**配置**:
- API 地址: `https://ai.zybbq.xyz/v1`
- 模型: `grok-4.1-thinking`
- API Key: `sk-DLwYp6UlgoTG2bjJTg6gczpBpKsBO2zqnBj3oLWAXyDyunj0`

**工具**:
| 工具名 | 功能 |
|--------|------|
| `mcp__grok-search__get_config_info` | 获取配置信息 |
| `mcp__grok-search__switch_model` | 切换模型 |
| `mcp__grok-search__toggle_builtin_tools` | 开关内置工具 |
| `mcp__grok-search__web_fetch` | 抓取网页内容 |
| `mcp__grok-search__web_search` | 网络搜索 |

**使用规则**:
- ❌ 禁止使用内置 `WebSearch` 和 `WebFetch`
- ✅ 必须使用 `mcp__grok-search__web_search` 和 `mcp__grok-search__web_fetch`

---

### 9. playwright

**描述**: Playwright 浏览器自动化

**工具**:
| 工具名 | 功能 |
|--------|------|
| `mcp__playwright__browser_click` | 点击 |
| `mcp__playwright__browser_close` | 关闭浏览器 |
| `mcp__playwright__browser_console_messages` | 控制台消息 |
| `mcp__playwright__browser_drag` | 拖拽 |
| `mcp__playwright__browser_evaluate` | 执行 JS |
| `mcp__playwright__browser_file_upload` | 文件上传 |
| `mcp__playwright__browser_fill_form` | 填充表单 |
| `mcp__playwright__browser_handle_dialog` | 处理对话框 |
| `mcp__playwright__browser_hover` | 悬停 |
| `mcp__playwright__browser_install` | 安装浏览器 |
| `mcp__playwright__browser_navigate` | 导航 |
| `mcp__playwright__browser_navigate_back` | 后退 |
| `mcp__playwright__browser_network_requests` | 网络请求 |
| `mcp__playwright__browser_press_key` | 按键 |
| `mcp__playwright__browser_resize` | 调整大小 |
| `mcp__playwright__browser_run_code` | 运行 Playwright 代码 |
| `mcp__playwright__browser_select_option` | 选择选项 |
| `mcp__playwright__browser_snapshot` | 页面快照 |
| `mcp__playwright__browser_tabs` | 标签页管理 |
| `mcp__playwright__browser_take_screenshot` | 截图 |
| `mcp__playwright__browser_type` | 输入 |
| `mcp__playwright__browser_wait_for` | 等待 |

---

### 10. streamable-mcp-server (Chrome 扩展)

**描述**: Chrome 浏览器扩展 MCP

**工具**:
| 工具名 | 功能 |
|--------|------|
| `mcp__streamable-mcp-server__chrome_bookmark_add` | 添加书签 |
| `mcp__streamable-mcp-server__chrome_bookmark_delete` | 删除书签 |
| `mcp__streamable-mcp-server__chrome_bookmark_search` | 搜索书签 |
| `mcp__streamable-mcp-server__chrome_click_element` | 点击元素 |
| `mcp__streamable-mcp-server__chrome_close_tabs` | 关闭标签 |
| `mcp__streamable-mcp-server__chrome_computer` | 鼠标键盘操作 |
| `mcp__streamable-mcp-server__chrome_console` | 控制台捕获 |
| `mcp__streamable-mcp-server__chrome_fill_or_select` | 填充/选择 |
| `mcp__streamable-mcp-server__chrome_get_web_content` | 获取网页内容 |
| `mcp__streamable-mcp-server__chrome_gif_recorder` | GIF 录制 |
| `mcp__streamable-mcp-server__chrome_handle_dialog` | 处理对话框 |
| `mcp__streamable-mcp-server__chrome_handle_download` | 处理下载 |
| `mcp__streamable-mcp-server__chrome_history` | 浏览历史 |
| `mcp__streamable-mcp-server__chrome_javascript` | 执行 JS |
| `mcp__streamable-mcp-server__chrome_keyboard` | 键盘输入 |
| `mcp__streamable-mcp-server__chrome_navigate` | 导航 |
| `mcp__streamable-mcp-server__chrome_network_capture` | 网络捕获 |
| `mcp__streamable-mcp-server__chrome_network_request` | 发送网络请求 |
| `mcp__streamable-mcp-server__chrome_read_page` | 读取页面 |
| `mcp__streamable-mcp-server__chrome_request_element_selection` | 请求元素选择 |
| `mcp__streamable-mcp-server__chrome_screenshot` | 截图 |
| `mcp__streamable-mcp-server__chrome_switch_tab` | 切换标签 |
| `mcp__streamable-mcp-server__chrome_upload_file` | 上传文件 |
| `mcp__streamable-mcp-server__get_windows_and_tabs` | 获取窗口和标签 |
| `mcp__streamable-mcp-server__performance_analyze_insight` | 性能分析 |
| `mcp__streamable-mcp-server__performance_start_trace` | 开始追踪 |
| `mcp__streamable-mcp-server__performance_stop_trace` | 停止追踪 |

---

## MCP GitHub 工具调用

本技能可配合以下 MCP 工具使用：

- `mcp__github__create_issue` - 创建 Issue
- `mcp__github__create_pull_request` - 创建 PR
- `mcp__github__list_issues` - 列出 Issues
- `mcp__github__list_pull_requests` - 列出 PRs
- `mcp__github__search_code` - 搜索代码
- `mcp__github__get_file_contents` - 获取文件内容
- `mcp__github__push_files` - 推送多个文件
- `mcp__github__create_branch` - 创建分支

### 示例：创建 Issue

```
使用 mcp__github__create_issue
参数:
- owner: ins13014778
- repo: REPO_NAME
- title: "Bug描述"
- body: "详细内容"
```

### 示例：创建 PR

```
使用 mcp__github__create_pull_request
参数:
- owner: ins13014778
- repo: REPO_NAME
- title: "功能描述"
- head: feature-branch
- base: main
- body: "PR描述"
```

---

## MetaBot 配置

**仓库**: https://github.com/xvirobotics/metabot

**描述**: 构建 supervised, self-improving agent organization 的基础设施。让 Claude Code 从终端解放出来，通过飞书/Telegram 在手机上访问。

### 安装位置

| 项目 | 路径 |
|------|------|
| CLI 工具 | `~/.local/bin/` |
| 配置目录 | `~/.metabot/` |

### CLI 工具

| 命令 | 功能 |
|------|------|
| `metabot` | MetaBot 管理 |
| `mb` | Agent Bus 操作 |
| `mm` | MetaMemory 操作 |
| `fd` | 飞书文档读取 |

### metabot 命令

```bash
# MetaBot 管理
metabot update                      # 拉取最新、重建、重启
metabot start                       # 用 PM2 启动
metabot stop                        # 停止
metabot restart                     # 重启
metabot logs                        # 查看实时日志
metabot status                      # PM2 进程状态
```

### mb (Agent Bus) 命令

```bash
# Agent Bus 操作
mb bots                             # 列出所有 bots
mb task <bot> <chatId> <prompt>     # 委托任务
mb schedule list                    # 列出计划任务
mb schedule cron <bot> <chatId> '<cron>' <prompt>  # 创建周期任务
mb schedule pause <id>              # 暂停周期任务
mb schedule resume <id>             # 恢复周期任务
mb stats                            # 成本与使用统计
mb health                           # 状态检查
```

### mm (MetaMemory) 命令

```bash
# MetaMemory 读取
mm search "部署指南"                # 全文搜索
mm list                             # 列出文档
mm folders                          # 文件夹树
mm path /projects/my-doc            # 按路径获取文档

# MetaMemory 写入
echo '# Notes' | mm create "标题" --folder ID --tags "dev"
echo '# Updated' | mm update DOC_ID
mm mkdir "new-folder"               # 创建文件夹
mm delete DOC_ID                    # 删除文档
```

### fd (飞书文档) 命令

```bash
# 飞书文档读取
fd read <feishu-url>                # 按 URL 读取文档
fd read-id <docId>                  # 按 ID 读取文档
fd info <feishu-url>                # 获取文档元数据
```

### API 端点 (默认端口 9100)

| 方法 | 路径 | 描述 |
|------|------|------|
| `GET` | `/api/health` | 健康检查 |
| `GET` | `/api/bots` | 列出 bots |
| `POST` | `/api/bots` | 创建 bot |
| `GET` | `/api/bots/:name` | 获取 bot 详情 |
| `DELETE` | `/api/bots/:name` | 删除 bot |
| `POST` | `/api/tasks` | 委托任务给 bot |
| `POST` | `/api/schedule` | 计划一次性或周期任务 |
| `GET` | `/api/schedule` | 列出计划任务 |
| `PATCH` | `/api/schedule/:id` | 更新计划任务 |
| `DELETE` | `/api/schedule/:id` | 取消计划任务 |
| `POST` | `/api/schedule/:id/pause` | 暂停周期任务 |
| `POST` | `/api/schedule/:id/resume` | 恢复周期任务 |
| `POST` | `/api/sync` | 触发 MetaMemory → Wiki 同步 |
| `GET` | `/api/sync` | Wiki 同步状态 |
| `GET` | `/api/feishu/document` | 读取飞书文档为 Markdown |
| `GET` | `/api/stats` | 成本与使用统计 |
| `GET` | `/api/metrics` | Prometheus 指标端点 |

### 聊天命令

| 命令 | 描述 |
|------|------|
| `/reset` | 清除会话 |
| `/stop` | 中止当前任务 |
| `/status` | 会话信息 |
| `/memory list` | 浏览知识树 |
| `/memory search <query>` | 搜索知识库 |
| `/sync` | 同步 MetaMemory 到飞书 Wiki |
| `/sync status` | 显示 Wiki 同步状态 |
| `/help` | 显示帮助 |
| `/metaskill ...` | 生成 agent teams、agents 或 skills |
| `/metabot` | Agent bus、调度和 bot 管理 API 文档 |

### 配置文件

**bots.json** - 定义 bots:

```json
{
  "feishuBots": [{
    "name": "metabot",
    "feishuAppId": "cli_xxx",
    "feishuAppSecret": "...",
    "defaultWorkingDirectory": "/home/user/project"
  }],
  "telegramBots": [{
    "name": "tg-bot",
    "telegramBotToken": "123456:ABC...",
    "defaultWorkingDirectory": "/home/user/project"
  }]
}
```

**环境变量 (.env)**:

| 变量 | 默认值 | 描述 |
|------|--------|------|
| `API_PORT` | 9100 | HTTP API 端口 |
| `API_SECRET` | - | Bearer token 认证 |
| `MEMORY_ENABLED` | true | 启用 MetaMemory |
| `MEMORY_PORT` | 8100 | MetaMemory 端口 |
| `WIKI_SYNC_ENABLED` | true | 启用 MetaMemory→Wiki 同步 |

### 第三方 AI 提供商

```bash
ANTHROPIC_BASE_URL=https://api.moonshot.ai/anthropic    # Kimi/Moonshot
ANTHROPIC_BASE_URL=https://api.deepseek.com/anthropic   # DeepSeek
ANTHROPIC_BASE_URL=https://api.z.ai/api/anthropic       # GLM/Zhipu
ANTHROPIC_AUTH_TOKEN=your-key
```

### MCP MetaBot 工具

| 工具名 | 功能 |
|--------|------|
| `mcp__metabot__*` | MetaBot HTTP API 调用 |

### MCP MetaMemory 工具

| 工具名 | 功能 |
|--------|------|
| `mcp__metamemory__*` | 读写共享记忆文档 |

### MCP MetaSkill 工具

| 工具名 | 功能 |
|--------|------|
| `mcp__metaskill__*` | 创建 AI agent teams、agents 或 skills |
