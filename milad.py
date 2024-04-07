import subprocess
import os
import OpenSSL.crypto
from colorama import init, Fore, Style

# تابع سازنده colorama
init()

# نصب pip
install_pip_command = "sudo apt install python3-pip"
result = subprocess.run(install_pip_command, shell=True)

# اعتبارسنجی نصب pip
if result.returncode == 0:
    print(Fore.GREEN + "**********************************" + Style.RESET_ALL)
    print(Fore.GREEN + "python3-pip installed successfully." + Style.RESET_ALL)
    print(Fore.GREEN + "**********************************" + Style.RESET_ALL)
else:
    print(Fore.RED + "**********************************" + Style.RESET_ALL)
    print(Fore.RED + "Error installing python3-pip." + Style.RESET_ALL)
    print(Fore.RED + "**********************************" + Style.RESET_ALL)
    exit()


# نصب ماژول
install_subprocess = "sudo pip install subprocess.run"
install_pyopenssl = "sudo pip install pyOpenSSL"
install_colorama = "pip install colorama"

# نصب ماژول colorama
result_colorama = subprocess.run(install_colorama, shell=True)
# بررسی نصب colorama
if result_colorama.returncode != 0:
    print(Fore.RED + "**********************************" + Style.RESET_ALL)
    print(Fore.RED + "Error installing colorama module. Aborting script execution." + Style.RESET_ALL)
    print(Fore.RED + "**********************************" + Style.RESET_ALL)
    exit()

# نصب ماژول subprocess.run
result_subprocess = subprocess.run(install_subprocess, shell=True)
# بررسی نصب subprocess.run
if result_subprocess.returncode != 0:
    print(Fore.RED + "**********************************" + Style.RESET_ALL)
    print(Fore.RED + "Error installing subprocess.run module. Aborting script execution." + Style.RESET_ALL)
    print(Fore.RED + "**********************************" + Style.RESET_ALL)
    exit()

# نصب ماژول pyOpenSSL
result_pyopenssl = subprocess.run(install_pyopenssl, shell=True)
# بررسی نصب pyOpenSSL
if result_pyopenssl.returncode != 0:
    print(Fore.RED + "**********************************" + Style.RESET_ALL)
    print(Fore.RED + "Error installing pyOpenSSL module. Aborting script execution." + Style.RESET_ALL)
    print(Fore.RED + "**********************************" + Style.RESET_ALL)
    exit()

# اگر هر دو ماژول با موفقیت نصب شده باشند، ادامه اسکریپت اجرا می‌شود

print(Fore.GREEN + "All required modules installed successfully. Continuing script execution..." + Style.RESET_ALL)



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
    8080, 8880,
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
    print(Fore.YELLOW + "Port opened successfully: {}".format(cmd) + Style.RESET_ALL)

# دستور نصب Docker
docker_install_cmd = "curl -fsSL https://get.docker.com | sh"
subprocess.run(docker_install_cmd, shell=True)
print(Fore.GREEN + "**********************************" + Style.RESET_ALL)
print(Fore.GREEN + "Docker installed successfully." + Style.RESET_ALL)
print(Fore.GREEN + "**********************************" + Style.RESET_ALL)

# دستور git clone
git_clone_cmd = "git clone https://github.com/Gozargah/Marzban-node"
subprocess.run(git_clone_cmd, shell=True, cwd="/root")
print(Fore.GREEN + "**********************************" + Style.RESET_ALL)
print(Fore.GREEN + "Marzban Node cloned successfully." + Style.RESET_ALL)
print(Fore.GREEN + "**********************************" + Style.RESET_ALL)

# دستور ایجاد پوشه
mkdir_cmd = "mkdir -p /var/lib/marzban-node"

# اجرای دستور
subprocess.run(mkdir_cmd, shell=True)
print(Fore.YELLOW + "Directory /var/lib/marzban-node created successfully." + Style.RESET_ALL)

# دستور ایجاد پوشه و دانلود فایل‌ها
command = "mkdir -p /var/lib/marzban/assets/ && wget -O /var/lib/marzban/assets/geosite.dat https://github.com/v2fly/domain-list-community/releases/latest/download/dlc.dat && wget -O /var/lib/marzban/assets/geoip.dat https://github.com/v2fly/geoip/releases/latest/download/geoip.dat && wget -O /var/lib/marzban/assets/iran.dat https://github.com/bootmortis/iran-hosted-domains/releases/latest/download/iran.dat"

# اجرای دستور
subprocess.run(command, shell=True)
print(Fore.GREEN + "**********************************" + Style.RESET_ALL)
print(Fore.YELLOW + "Directory and files downloaded successfully. (iran block)" + Style.RESET_ALL)
print(Fore.GREEN + "**********************************" + Style.RESET_ALL)

# دستور ایجاد پوشه
mkdir_cmd = "mkdir -p /var/lib/marzban/xray-core"
subprocess.run(mkdir_cmd, shell=True)
print(Fore.YELLOW + "Directory /var/lib/marzban/xray-core created successfully." + Style.RESET_ALL)

# دیکشنری اطلاعات نسخه‌ها
available_versions = {
    "1": ("1.8.4 64", "https://github.com/XTLS/Xray-core/releases/download/v1.8.4/Xray-linux-64.zip"),
    "2": ("1.8.6 64", "https://github.com/XTLS/Xray-core/releases/download/v1.8.6/Xray-linux-64.zip"),
    "3": ("1.8.7 64", "https://github.com/XTLS/Xray-core/releases/download/v1.8.7/Xray-linux-64.zip"),
    "4": ("1.8.8 64", "https://github.com/XTLS/Xray-core/releases/download/v1.8.8/Xray-linux-64.zip"),
    "5": ("1.8.9 64", "https://github.com/XTLS/Xray-core/releases/download/v1.8.9/Xray-linux-64.zip"),
    "6": ("1.8.10 64", "https://github.com/XTLS/Xray-core/releases/download/v1.8.10/Xray-linux-64.zip"),
    "7": ("1.8.4 arm64", "https://github.com/XTLS/Xray-core/releases/download/v1.8.4/Xray-linux-arm64-v8a.zip"),
    "8": ("1.8.6 arm64", "https://github.com/XTLS/Xray-core/releases/download/v1.8.6/Xray-linux-arm64-v8a.zip"),
    "9": ("1.8.7 arm64", "https://github.com/XTLS/Xray-core/releases/download/v1.8.7/Xray-linux-arm64-v8a.zip"),
    "10": ("1.8.8 arm64", "https://github.com/XTLS/Xray-core/releases/download/v1.8.8/Xray-linux-arm64-v8a.zip"),
    "11": ("1.8.9 arm64", "https://github.com/XTLS/Xray-core/releases/download/v1.8.9/Xray-linux-arm64-v8a.zip"),
    "12": ("1.8.10 arm64", "https://github.com/XTLS/Xray-core/releases/download/v1.8.10/Xray-linux-arm64-v8a.zip")
}

while True:
    # نمایش نسخه‌های موجود به کاربر
    print("Available versions:")
    for idx, (version_num, (version_name, version_url)) in enumerate(available_versions.items(), start=1):
        if idx <= 6:
            print(Fore.YELLOW + f"{idx}: {version_name} - {version_url}")
        else:
            print(Fore.RED + f"{idx}: {version_name} - {version_url}")

    # درخواست انتخاب نسخه از کاربر
    selected_version_index = input("Enter the number of the version you want to download: ")

    # بررسی اگر شماره انتخاب شده در محدوده شماره‌های موجود نباشد
    if selected_version_index not in available_versions:
        print(Fore.YELLOW + "Error: Selected version number is not valid. Please choose a valid index." + Style.RESET_ALL)
        continue
    else:
        selected_version_name, selected_version_url = available_versions[selected_version_index]
        break

# دستور دانلود فایل با توجه به شماره انتخاب شده
download_cmd = f"wget -O /var/lib/marzban/xray-core/Xray-linux-64.zip {selected_version_url}"
result = subprocess.run(download_cmd, shell=True)

# بررسی موفقیت دانلود و چاپ پیام مناسب
if result.returncode == 0:
    print(Fore.GREEN + "File downloaded successfully." + Style.RESET_ALL)
else:
    print(Fore.RED + "Error: Download failed. Aborting script execution." + Style.RESET_ALL)


# دستور نصب پکیج unzip
apt_install_cmd = "apt install -y unzip"
subprocess.run(apt_install_cmd, shell=True)
print(Fore.GREEN + "**********************************" + Style.RESET_ALL)
print(Fore.GREEN + "Package 'unzip' installed successfully." + Style.RESET_ALL)
print(Fore.GREEN + "**********************************" + Style.RESET_ALL)


# دستور اکسترکت کردن فایل از حالت zip و حذف فایل zip
extract_cmd = "unzip /var/lib/marzban/xray-core/Xray-linux-64.zip -d /var/lib/marzban/xray-core/ && rm /var/lib/marzban/xray-core/Xray-linux-64.zip"
subprocess.run(extract_cmd, shell=True)
print(Fore.GREEN + "**********************************" + Style.RESET_ALL)
print(Fore.GREEN + "File extracted and zip file deleted successfully." + Style.RESET_ALL)
print(Fore.GREEN + "**********************************" + Style.RESET_ALL)

# ایجاد پوشه در صورت وجود نداشتن
directory = '/var/lib/marzban-node/'
if not os.path.exists(directory):
    os.makedirs(directory)

while True:
    # دریافت تعداد فایل‌های مورد نیاز از کاربر
    num_files = int(input("Enter the number of files needed certificate: "))

    # حلقه برای دریافت متن تا زمانی که خالی نباشد
    while True:
        # دریافت سرتیفیکیت دلخواه از کاربر
        print("Enter the Certificate. Press Enter on an empty line to finish:")
        text_parts = []
        while True:
            line = input()
            if not line.strip():  # اگر خط خالی باشد، دریافت متن متوقف می‌شود
                break
            text_parts.append(line)

        if text_parts:  # اگر متن وارد شده نبود، سوال مجددا پرسیده می‌شود
            text = '\n'.join(text_parts)
            break

    # حلقه برای ایجاد فایل‌ها با نام‌های مختلف
    for i in range(1, num_files + 1):
        with open(f"{directory}/ssl_client_cert_{i}.pem", "w") as file:
            file.write(text)

        print(Fore.YELLOW + f"File ssl_client_cert_{i}.pem created and text saved successfully." + Style.RESET_ALL)

    break


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
      SSL_CLIENT_CERT_FILE: "/var/lib/marzban-node/ssl_client_cert_9.pem"
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
      SSL_CLIENT_CERT_FILE: "/var/lib/marzban-node/ssl_client_cert_10.pem"
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
      SSL_CLIENT_CERT_FILE: "/var/lib/marzban-node/ssl_client_cert_11.pem"
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
      SSL_CLIENT_CERT_FILE: "/var/lib/marzban-node/ssl_client_cert_12.pem"
      XRAY_EXECUTABLE_PATH: "/var/lib/marzban/xray-core/xray"

    volumes:
      - /var/lib/marzban-node:/var/lib/marzban-node
      - /var/lib/marzban:/var/lib/marzban
      - /var/lib/marzban/assets:/usr/local/share/xray

  marzban-node-13:
    # build: .
    image: gozargah/marzban-node:latest
    restart: always
    network_mode: host

    environment:
      SERVICE_PORT: 52050
      XRAY_API_PORT: 52051
      SSL_CLIENT_CERT_FILE: "/var/lib/marzban-node/ssl_client_cert_13.pem"
      XRAY_EXECUTABLE_PATH: "/var/lib/marzban/xray-core/xray"

    volumes:
      - /var/lib/marzban-node:/var/lib/marzban-node
      - /var/lib/marzban:/var/lib/marzban
      - /var/lib/marzban/assets:/usr/local/share/xray

  marzban-node-14:
    # build: .
    image: gozargah/marzban-node:latest
    restart: always
    network_mode: host

    environment:
      SERVICE_PORT: 51050
      XRAY_API_PORT: 51051
      SSL_CLIENT_CERT_FILE: "/var/lib/marzban-node/ssl_client_cert_14.pem"
      XRAY_EXECUTABLE_PATH: "/var/lib/marzban/xray-core/xray"

    volumes:
      - /var/lib/marzban-node:/var/lib/marzban-node
      - /var/lib/marzban:/var/lib/marzban
      - /var/lib/marzban/assets:/usr/local/share/xray

  marzban-node-15:
    # build: .
    image: gozargah/marzban-node:latest
    restart: always
    network_mode: host

    environment:
      SERVICE_PORT: 50050
      XRAY_API_PORT: 50051
      SSL_CLIENT_CERT_FILE: "/var/lib/marzban-node/ssl_client_cert_15.pem"
      XRAY_EXECUTABLE_PATH: "/var/lib/marzban/xray-core/xray"

    volumes:
      - /var/lib/marzban-node:/var/lib/marzban-node
      - /var/lib/marzban:/var/lib/marzban
      - /var/lib/marzban/assets:/usr/local/share/xray
"""

# مسیر فایل docker-compose.yml
file_path = "/root/Marzban-node/docker-compose.yml"

# دستور برای پاک کردن محتوای فایل و جایگزینی با متن دلخواه
command = f"echo '{custom_text.strip()}' > {file_path} && chmod 644 {file_path}"
subprocess.run(command, shell=True)
print(Fore.GREEN + "**********************************" + Style.RESET_ALL)
print(Fore.GREEN + "File docker-compose.yml updated successfully." + Style.RESET_ALL)
print(Fore.GREEN + "**********************************" + Style.RESET_ALL)

# روشن شدن فایروال
ufw_enable_cmd = "ufw enable"
subprocess.run(ufw_enable_cmd, shell=True)
print(Fore.GREEN + "**********************************" + Style.RESET_ALL)
print(Fore.GREEN + "Firewall enabled successfully." + Style.RESET_ALL)
print(Fore.GREEN + "**********************************" + Style.RESET_ALL)

# تعیین مسیر پوشه
directory = "/root/Marzban-node"

# اگر پوشه وجود دارد، به آن تغییر مسیر دهید و دستور Docker Compose را اجرا کنید
if os.path.exists(directory):
    os.chdir(directory)
    print(Fore.YELLOW + "Changed directory successfully." + Style.RESET_ALL)

    # اجرای دستور Docker Compose
    command = "docker compose up -d"
    subprocess.run(command, shell=True)
else:
    print(Fore.RED + "Error: Directory does not exist." + Style.RESET_ALL)


print("*********************************************")
print("Created by Milad Ajourloo 🧑‍🚀")
print("3/19/2024 ⏰")
print("ID Telegram: @alecsander1997 ©️")
print("*********************************************")
