import requests
import subprocess

# Функция для получения IP-адресов хуков GitHub
def get_github_hook_ips():
    url = "https://api.github.com/meta"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        github_hook_ips = data.get("hooks", [])
        return github_hook_ips
    else:
        print("Ошибка при получении IP-адресов хуков GitHub")
        return []

# Функция для обновления правил UFW
def update_ufw_rules(new_ips):
    # Удаляем старые правила для хуков GitHub
    subprocess.run("sudo ufw status numbered | grep 'from any to any' | grep 'GitHub Hook' | awk '{print $1}' | xargs -I {} sudo ufw delete {}", shell=True)
    
    # Добавляем новые правила
    ufw_allow_commands = []
    for ip in new_ips:
        ufw_allow_commands.append(f"sudo ufw allow from {ip} to any comment 'GitHub Hook'")  # Разрешить доступ из указанных IP ко всем портам с комментарием 'GitHub Hook'
        ufw_allow_commands.append(f"ufw route allow proto tcp from {ip} to any port 8080 comment 'GitHub Hook'")#now 8080
        ufw_allow_commands.append(f"ufw route allow proto tcp from {ip} to any port 3000 comment 'GitHub Hook'")
        # Добавьте другие правила UFW по мере необходимости

    for command in ufw_allow_commands:
        subprocess.run(command, shell=True)

# Получаем IP-адреса хуков GitHub
github_hook_ips = get_github_hook_ips()

# Обновляем правила UFW
update_ufw_rules(github_hook_ips)
