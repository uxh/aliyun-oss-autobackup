# 使用说明

## 注意

以下操作已在**Debian11 x64**、**Debian12 x64**上通过，其他系统暂未测试。

## 安装阿里云官方 SDK（Python 版）

1、安装 pip 工具

Debian11 x64 / Debian12 x64：

```bash
apt install -y python3-pip
```

2、更新 pip 工具

Debian11 x64 / Debian12 x64：

```bash
pip install --upgrade pip
```

如果提示`externally-managed-environment`，可以执行（将x替换为实际数字）：

```bash
mv /usr/lib/python3.x/EXTERNALLY-MANAGED /usr/lib/python3.x/EXTERNALLY-MANAGED.bk
```

3、安装 SDK

Debian11 x64 / Debian12 x64：

```bash
pip install oss2
```

4、安装其他依赖

Debian11 x64：

```bash
apt install -y wget zip python-dev
```

Debian12 x64：

```bash
apt install -y wget zip python-dev-is-python3
```

## 使用示例

1、下载备份脚本

英文版

```bash
wget --no-check-certificate -O backup.sh https://github.com/uxh/aliyun-oss-autobackup/raw/main/backup.sh
```

2、下载上传脚本

```bash
wget --no-check-certificate -O oss.upload.py https://github.com/uxh/aliyun-oss-autobackup/raw/main/oss.upload.py
```

3、修改备份脚本参数

请修改备份脚本中第 *16、17、20、21、24、25* 行中的相关配置

4、创建备份目录

```bash
mkdir -p /home/wwwbackups
```

5、备份网站目录

英文版执行此命令

```bash
bash backup.sh --file 123.com /home/wwwroot/123.com /home/wwwbackups/123.com
```

6、备份网站数据库

英文版执行此命令

```bash
bash backup.sh --db 123.com 123.com_database root w123456 /home/wwwbackups/123.com
```
