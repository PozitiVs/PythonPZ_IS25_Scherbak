#В исходном текстовом файле найти все домены из URL-адресов
import re

def extract_domains(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    pattern = r'https?://([\w.-]+)(?::\d+)?(?:/|$)'
    domains = re.findall(pattern, text)
    
    return domains

domains = extract_domains('radio_stations.txt')
print(f"Найдено доменов: {len(domains)}")
for domain in domains:
    print(domain)