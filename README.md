# SparkCopy

使用 Flask 提供小红书文案生成页面与 `/generate` 接口，后端通过 DeepSeek API 生成内容。

## Windows 本地运行

1. 安装 Python 3.10 或更新版本。
2. 在项目目录打开 PowerShell，创建并启用虚拟环境：

   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. 安装依赖：

   ```powershell
   pip install -r requirements.txt
   ```

4. 打开项目根目录的 `.env` 文件，在 `DEEPSEEK_API_KEY=` 后粘贴你的 DeepSeek API Key。默认模型为 `deepseek-chat`，也可按需修改 `DEEPSEEK_MODEL`。
5. 启动服务：

   ```powershell
   python app.py
   ```

6. 浏览器访问 `http://127.0.0.1:5000`。

请勿将真实 API Key 写入前端 HTML、提交到 Git 或发到聊天中。`.env` 已加入 `.gitignore`。

## 部署到 PythonAnywhere

本项目包含 Flask 后端，不能只用 GitHub Pages 托管。PythonAnywhere 官方当前的 Developer 方案标价为每月 10 美元，并提供外网访问；免费方案的外网访问受限，DeepSeek API 可能无法访问。请在订阅前确认方案和价格。

1. 在 PythonAnywhere 创建/登录账号，并在 **Web** 页面创建 Python Web App，选择 Manual configuration 和 Python 版本。
2. 将项目文件上传到 `/home/<你的用户名>/sparkcopy/`。不要上传 `.venv`、`__pycache__` 或本机 `.env`。
3. 打开 **Consoles → Bash**，运行 `mkvirtualenv --python=/usr/bin/python3.13 sparkcopy-venv`（如 Web App 选了其他 Python 版本，请相应调整），然后 `workon sparkcopy-venv`、`cd ~/sparkcopy`、`pip install -r requirements.txt`。
4. 在 PythonAnywhere 的 Files 页面创建 `/home/<你的用户名>/sparkcopy/.env`，填入 `DEEPSEEK_API_KEY=你的密钥`，并保留 API URL 和模型配置。密钥只放在服务器文件中，不要上传到 GitHub。
5. 在 **Web → Virtualenv** 填入 `/home/<你的用户名>/.virtualenvs/sparkcopy-venv`。
6. 将 `pythonanywhere_wsgi.py` 的内容复制到 Web 页面显示的 WSGI configuration file。确保项目目录为 `~/sparkcopy`；如果你使用了其他目录，请修改 `PROJECT_DIR`。
7. 在 **Web** 页面点击 Reload，然后访问 `https://<你的用户名>.pythonanywhere.com`。

上传前务必确认真实 API Key 没有放进公开仓库。PythonAnywhere 的公开网址任何人都可以访问，API 使用费用会计入你自己的 DeepSeek 账户。
