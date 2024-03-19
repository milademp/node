import subprocess

# لیست پورت‌های مورد نظر
ports = [
    59050, 59051,
    60050, 60051,
    61050, 61051,
    62050, 62051,
    63050, 63051,
    64050, 64051,
    58050, 58051,
    57050, 57051,
    8080,
    2096,
    45000,
    53,
    56050, 56051,
    55050, 55051,
    54050, 54051,
    53050, 53051,
    52050, 52051,
    51050, 51051,
    50050, 50051
]

# ساختن دستورات ufw برای اضافه کردن قوانین برای هر پورت
commands = ["ufw allow {}/tcp".format(port) for port in ports]

# اجرای هر دستور
for cmd in commands:
    subprocess.run(cmd, shell=True)
    print("Port opened successfully: {}".format(cmd))

# دستور نصب Docker
docker_install_cmd = "curl -fsSL https://get.docker.com | sh"
subprocess.run(docker_install_cmd, shell=True)
print("Docker installed successfully.")

# دستور git clone
git_clone_cmd = "git clone https://github.com/Gozargah/Marzban-node"
subprocess.run(git_clone_cmd, shell=True, cwd="/root")
print("Repository cloned successfully.")

# دستور ایجاد پوشه
mkdir_cmd = "mkdir -p /var/lib/marzban-node"

# اجرای دستور
subprocess.run(mkdir_cmd, shell=True)
print("Directory /var/lib/marzban-node created successfully.")

# دستور ایجاد پوشه و دانلود فایل‌ها
command = "mkdir -p /var/lib/marzban/assets/ && wget -O /var/lib/marzban/assets/geosite.dat https://github.com/v2fly/domain-list-community/releases/latest/download/dlc.dat && wget -O /var/lib/marzban/assets/geoip.dat https://github.com/v2fly/geoip/releases/latest/download/geoip.dat && wget -O /var/lib/marzban/assets/iran.dat https://github.com/bootmortis/iran-hosted-domains/releases/latest/download/iran.dat"

# اجرای دستور
subprocess.run(command, shell=True)
print("Directory and files downloaded successfully. (iran block)")

# دستور ایجاد پوشه
mkdir_cmd = "mkdir -p /var/lib/marzban/xray-core"
subprocess.run(mkdir_cmd, shell=True)
print("Directory /var/lib/marzban/xray-core created successfully.")

# دستور دانلود فایل
wget_cmd = "wget -O /var/lib/marzban/xray-core/Xray-linux-64.zip https://github.com/XTLS/Xray-core/releases/download/v1.8.4/Xray-linux-64.zip"
subprocess.run(wget_cmd, shell=True)
print("File Xray-linux-64.zip downloaded successfully.")

# دستور نصب پکیج unzip
apt_install_cmd = "apt install -y zip"
subprocess.run(apt_install_cmd, shell=True)
print("Package 'zip' installed successfully.")

# دستور اکسترکت کردن فایل از حالت zip و حذف فایل zip
extract_cmd = "unzip /var/lib/marzban/xray-core/Xray-linux-64.zip -d /var/lib/marzban/xray-core/ && rm /var/lib/marzban/xray-core/Xray-linux-64.zip"
subprocess.run(extract_cmd, shell=True)
print("File extracted and zip file deleted successfully.")

# تعداد فایل‌های مورد نیاز
num_files = 10

# متن دلخواه برای قرار دادن در فایل
text = """-----BEGIN CERTIFICATE-----
MIIEnDCCAoQCAQAwDQYJKoZIhvcNAQENBQAwEzERMA8GA1UEAwwIR296YXJnYWgw
IBcNMjQwMzE1MTM1NTM5WhgPMjEyNDAyMjAxMzU1MzlaMBMxETAPBgNVBAMMCEdv
emFyZ2FoMIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAwO34xDS+I+fb
ROkefVl6ykbjptSF2LYQvD+tyXT5oTjecvWVHKzD/umUPwHrRkC2kBvZTQ5BfgHs
wLHG3LuGWbztirEBT8j4ruoKFifJx9XK3eF1XE+FB30pot9SwMsYhcFtXRtJXZsY
GLS/m9gFALRQ5Z1jQdAm89+Zpot1wPbQEhi+2f/YfefiYWLDNcdQ/Q8bKbMs/v0R
7JJMgJDHMAnjrw4b8/cSn1c6T2hHP54h50mXW6IHHVI4v/n7oUqD25Mo+dFJx8FL
5r0dZUPvKC3mmLQjP7lSCdKuzaltPAS5rVYCs1Vqmd4U7DCX92q18xddu3HuxJFc
1WC0XV1MoVuaiDglsOqsUyUoohtS4CNJ1v31edQ+AVoe5tq9chQeKLJBvIYDbuZ+
U/TJXK/adSN5GsWtXd5HsiTSCGQOv7uH337meDzkQkuqhHuLgdL8z0KVjMWgJA/5
sy4993WPk8yqjR0x7Tv/W7OEYON5IY2H7LUyi26PY10qR47DxPlrHcf2wVSmzKnX
k99AWFBUy2nA70Wi0xtgDXQ+5fupamQOhY4jnn6rr8psmLpRhxIf9MVR/orjdSgf
S4wZ09k2jJNh1FGaIf7vIbXzhVbZnpXLpUHS5J+7E782R0gWU8fMQfdYrZ41Lbv3
+ASFI1tHrV5JNgZLnA3A0eL94SpSfk0CAwEAATANBgkqhkiG9w0BAQ0FAAOCAgEA
uLD5q+z86nOURSdm0eTbSAhgdqu3DXGvrqpfJp6i+r6dX5dobPQQ67u/rCYQV0cg
WrRaOtVrndOfzcj3G0H9v6YNlFxBA1Mo1t8LN30jj9p8piyK7KI514SgOYExIe2Y
oPqf3s2dlMo8BKnL3CLaaEAI0yz8sKESUQQWvLnJchH/Zr2BgB5xbZp4aWxqIsqE
Xj+SpVEOZVMfCv+k4Jr0MxQDkmZVnhEOTIVUKIV7rLqkhsusT5MbwVBHKS1bEmED
SLuES5/uOSaUz7R3yH+e5g/teiJv3dQbGihTLmkA+o8Zp0H7ImA477CB6EhVgAvG
yl1sre6K+T/ha+6h1rAYkIvTFKI8hx34QcKixwfsWQUcG85YkZKCJ0+c0XzRiAzE
IU6/Fj8f3qmHsZduBqr47YWu7zFvqqPslHz538uhNesCdtomD8n0B4K5gWHtI77v
uARNj18UV1+o4OyAj7OjFG0pZ7kaTr9wGZd3WRmRhblWLFbIG0aPcwJoa+vEA3YY
aMaDSxnsL3Gp5RSThttI3HlKcSU2ij4ALWsbJczEv8S/8TJR6j2QRyHSn/4jIbND
HCFkt5WOqJdmWsjXDglIUIRTrvTofflg2yXkp11wU4sEZcsg51J5FRHXcBmrBssa
bK1YRZlTrzSz60IxxzALvlWb/6lda9U+TGZPLQJP3WY=
-----END CERTIFICATE-----"""

# حلقه برای ایجاد فایل‌ها با نام‌های مختلف
for i in range(1, num_files + 1):
    file_name = f"/var/lib/marzban-node/ssl_client_cert_{i}.pem"
    command = f"echo '{text}' > {file_name}"
    subprocess.run(command, shell=True)
    print(f"File ssl_client_cert_{i}.pem created and text saved successfully.")

# متن دلخواه برای جایگزینی در فایل
custom_text = """
services:
  marzban-node-1:
    # build: .
    image: gozargah/marzban-node:latest
    restart: always
    network_mode: host

    environment:
      SERVICE_PORT: 62050
      XRAY_API_PORT: 62051
      SSL_CLIENT_CERT_FILE: "/var/lib/marzban-node/ssl_client_cert_1.pem"
      XRAY_EXECUTABLE_PATH: "/var/lib/marzban/xray-core/xray"

    volumes:
      - /var/lib/marzban-node:/var/lib/marzban-node
      - /var/lib/marzban:/var/lib/marzban
      - /var/lib/marzban/assets:/usr/local/share/xray

  marzban-node-2:
    # build: .
    image: gozargah/marzban-node:latest
    restart: always
    network_mode: host

    environment:
      SERVICE_PORT: 63050
      XRAY_API_PORT: 63051
      SSL_CLIENT_CERT_FILE: "/var/lib/marzban-node/ssl_client_cert_2.pem"
      XRAY_EXECUTABLE_PATH: "/var/lib/marzban/xray-core/xray"

    volumes:
      - /var/lib/marzban-node:/var/lib/marzban-node
      - /var/lib/marzban:/var/lib/marzban
      - /var/lib/marzban/assets:/usr/local/share/xray

  marzban-node-3:
    # build: .
    image: gozargah/marzban-node:latest
    restart: always
    network_mode: host

    environment:
      SERVICE_PORT: 64050
      XRAY_API_PORT: 64051
      SSL_CLIENT_CERT_FILE: "/var/lib/marzban-node/ssl_client_cert_3.pem"
      XRAY_EXECUTABLE_PATH: "/var/lib/marzban/xray-core/xray"

    volumes:
      - /var/lib/marzban-node:/var/lib/marzban-node
      - /var/lib/marzban:/var/lib/marzban
      - /var/lib/marzban/assets:/usr/local/share/xray

  marzban-node-4:
    # build: .
    image: gozargah/marzban-node:latest
    restart: always
    network_mode: host

    environment:
      SERVICE_PORT: 58050
      XRAY_API_PORT: 58051
      SSL_CLIENT_CERT_FILE: "/var/lib/marzban-node/ssl_client_cert_4.pem"
      XRAY_EXECUTABLE_PATH: "/var/lib/marzban/xray-core/xray"

    volumes:
      - /var/lib/marzban-node:/var/lib/marzban-node
      - /var/lib/marzban:/var/lib/marzban
      - /var/lib/marzban/assets:/usr/local/share/xray

  marzban-node-5:
    # build: .
    image: gozargah/marzban-node:latest
    restart: always
    network_mode: host

    environment:
      SERVICE_PORT: 61050
      XRAY_API_PORT: 61051
      SSL_CLIENT_CERT_FILE: "/var/lib/marzban-node/ssl_client_cert_5.pem"
      XRAY_EXECUTABLE_PATH: "/var/lib/marzban/xray-core/xray"

    volumes:
      - /var/lib/marzban-node:/var/lib/marzban-node
      - /var/lib/marzban:/var/lib/marzban
      - /var/lib/marzban/assets:/usr/local/share/xray

  marzban-node-6:
    # build: .
    image: gozargah/marzban-node:latest
    restart: always
    network_mode: host

    environment:
      SERVICE_PORT: 60050
      XRAY_API_PORT: 60051
      SSL_CLIENT_CERT_FILE: "/var/lib/marzban-node/ssl_client_cert_6.pem"
      XRAY_EXECUTABLE_PATH: "/var/lib/marzban/xray-core/xray"

    volumes:
      - /var/lib/marzban-node:/var/lib/marzban-node
      - /var/lib/marzban:/var/lib/marzban
      - /var/lib/marzban/assets:/usr/local/share/xray

  marzban-node-7:
    # build: .
    image: gozargah/marzban-node:latest
    restart: always
    network_mode: host

    environment:
      SERVICE_PORT: 59050
      XRAY_API_PORT: 59051
      SSL_CLIENT_CERT_FILE: "/var/lib/marzban-node/ssl_client_cert_7.pem"
      XRAY_EXECUTABLE_PATH: "/var/lib/marzban/xray-core/xray"

    volumes:
      - /var/lib/marzban-node:/var/lib/marzban-node
      - /var/lib/marzban:/var/lib/marzban
      - /var/lib/marzban/assets:/usr/local/share/xray

  marzban-node-8:
    # build: .
    image: gozargah/marzban-node:latest
    restart: always
    network_mode: host

    environment:
      SERVICE_PORT: 57050
      XRAY_API_PORT: 57051
      SSL_CLIENT_CERT_FILE: "/var/lib/marzban-node/ssl_client_cert_8.pem"
      XRAY_EXECUTABLE_PATH: "/var/lib/marzban/xray-core/xray"

    volumes:
      - /var/lib/marzban-node:/var/lib/marzban-node
      - /var/lib/marzban:/var/lib/marzban
      - /var/lib/marzban/assets:/usr/local/share/xray

  marzban-node-9:
    # build: .
    image: gozargah/marzban-node:latest
    restart: always
    network_mode: host

    environment:
      SERVICE_PORT: 56050
      XRAY_API_PORT: 56051
      SSL_CLIENT_CERT_FILE: "/var/lib/marzban-node/ssl_client_cert_8.pem"
      XRAY_EXECUTABLE_PATH: "/var/lib/marzban/xray-core/xray"

    volumes:
      - /var/lib/marzban-node:/var/lib/marzban-node
      - /var/lib/marzban:/var/lib/marzban
      - /var/lib/marzban/assets:/usr/local/share/xray

  marzban-node-10:
    # build: .
    image: gozargah/marzban-node:latest
    restart: always
    network_mode: host

    environment:
      SERVICE_PORT: 55050
      XRAY_API_PORT: 55051
      SSL_CLIENT_CERT_FILE: "/var/lib/marzban-node/ssl_client_cert_8.pem"
      XRAY_EXECUTABLE_PATH: "/var/lib/marzban/xray-core/xray"

    volumes:
      - /var/lib/marzban-node:/var/lib/marzban-node
      - /var/lib/marzban:/var/lib/marzban
      - /var/lib/marzban/assets:/usr/local/share/xray

  marzban-node-11:
    # build: .
    image: gozargah/marzban-node:latest
    restart: always
    network_mode: host

    environment:
      SERVICE_PORT: 54050
      XRAY_API_PORT: 54051
      SSL_CLIENT_CERT_FILE: "/var/lib/marzban-node/ssl_client_cert_8.pem"
      XRAY_EXECUTABLE_PATH: "/var/lib/marzban/xray-core/xray"

    volumes:
      - /var/lib/marzban-node:/var/lib/marzban-node
      - /var/lib/marzban:/var/lib/marzban
      - /var/lib/marzban/assets:/usr/local/share/xray

  marzban-node-12:
    # build: .
    image: gozargah/marzban-node:latest
    restart: always
    network_mode: host

    environment:
      SERVICE_PORT: 53050
      XRAY_API_PORT: 53051
      SSL_CLIENT_CERT_FILE: "/var/lib/marzban-node/ssl_client_cert_8.pem"
      XRAY_EXECUTABLE_PATH: "/var/lib/marzban/xray-core/xray"

    volumes:
      - /var/lib/marzban-node:/var/lib/marzban-node
      - /var/lib/marzban:/var/lib/marzban
      - /var/lib/marzban/assets:/usr/local/share/xray

  marzban-node-9:
    # build: .
    image: gozargah/marzban-node:latest
    restart: always
    network_mode: host

    environment:
      SERVICE_PORT: 52050
      XRAY_API_PORT: 52051
      SSL_CLIENT_CERT_FILE: "/var/lib/marzban-node/ssl_client_cert_8.pem"
      XRAY_EXECUTABLE_PATH: "/var/lib/marzban/xray-core/xray"

    volumes:
      - /var/lib/marzban-node:/var/lib/marzban-node
      - /var/lib/marzban:/var/lib/marzban
      - /var/lib/marzban/assets:/usr/local/share/xray

  marzban-node-9:
    # build: .
    image: gozargah/marzban-node:latest
    restart: always
    network_mode: host

    environment:
      SERVICE_PORT: 51050
      XRAY_API_PORT: 51051
      SSL_CLIENT_CERT_FILE: "/var/lib/marzban-node/ssl_client_cert_8.pem"
      XRAY_EXECUTABLE_PATH: "/var/lib/marzban/xray-core/xray"

    volumes:
      - /var/lib/marzban-node:/var/lib/marzban-node
      - /var/lib/marzban:/var/lib/marzban
      - /var/lib/marzban/assets:/usr/local/share/xray

  marzban-node-9:
    # build: .
    image: gozargah/marzban-node:latest
    restart: always
    network_mode: host

    environment:
      SERVICE_PORT: 50050
      XRAY_API_PORT: 50051
      SSL_CLIENT_CERT_FILE: "/var/lib/marzban-node/ssl_client_cert_8.pem"
      XRAY_EXECUTABLE_PATH: "/var/lib/marzban/xray-core/xray"

    volumes:
      - /var/lib/marzban-node:/var/lib/marzban-node
      - /var/lib/marzban:/var/lib/marzban
      - /var/lib/marzban/assets:/usr/local/share/xray
"""

# مسیر فایل docker-compose.yml
file_path = "~/Marzban-node/docker-compose.yml"

# دستور برای پاک کردن محتوای فایل و جایگزینی با متن دلخواه
command = f"echo '{custom_text.strip()}' > {file_path} && chmod 644 {file_path}"
subprocess.run(command, shell=True)
print("File docker-compose.yml updated successfully.")

# روشن شدن فایروال
ufw_enable_cmd = "ufw enable"
subprocess.run(ufw_enable_cmd, shell=True)
print("Firewall enabled successfully.")

command = "cd ~/Marzban-node && docker-compose down && docker-compose up -d"
subprocess.run(command, shell=True)
print("Docker Compose commands executed successfully.")

print("*********************************************")
print("Created by Milad Ajourloo 🧑‍🚀")
print("3/19/2024 ⏰")
print("ID Telegram: @alecsander1997 ©️")
print("*********************************************")
