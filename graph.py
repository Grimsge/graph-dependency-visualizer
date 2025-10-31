import os #проверка существования config.xml
import xml.etree.ElementTree as ET #для чтения xml
import urllib.request
import urllib.error #для чтения ссылки

def read_xml():
    try:
        if not os.path.exists("config.xml"):
            print("файл config.xml не найден")
            return None
    
        tree = ET.parse("config.xml")
        root = tree.getroot()
        config = {}
        
        package_name_elem = root.find("package_name")
        if package_name_elem is None:
            print("Ошибка: тег package_name отсутствует")
        else:
            config["package_name"] = package_name_elem.text
            
        repository_url_elem = root.find("repository_url")
        if repository_url_elem is None:
            print("Ошибка: тег repository_url отсутствует")
        else:
            config["repository_url"] = repository_url_elem.text
            
        test_repo_mode_elem = root.find("test_repo_mode")
        if test_repo_mode_elem is None:
            print("Ошибка: тег test_repo_mode отсутствует")
        else:
            config["test_repo_mode"] = test_repo_mode_elem.text
            
        package_version_elem = root.find("package_version")
        if package_version_elem is None:
            print("Ошибка: тег package_version отсутствует")
        else:
            config["package_version"] = package_version_elem.text
            
        output_filename_elem = root.find("output_filename")
        if output_filename_elem is None:
            print("Ошибка: тег output_filename отсутствует")
        else:
            config["output_filename"] = output_filename_elem.text
            
        return config
        
    except Exception as e:
        print(f"Ошибка: {e}")
        return None

def dependencies_find(cargo_content): #Этап2
    if cargo_content is None:
        print("Нечего анализировать - cargo_content пустой")
        return
    
    deps_start = cargo_content.find("[dependencies]")
    if deps_start != -1:
        print("Секция [dependencies] найдена!")
    else:
        print("Секция [dependencies] не найдена")
        return
        
    deps_section = cargo_content[deps_start:]
    next_section = deps_section.find('[', 1)  

    if next_section != -1:
        deps_content = deps_section[:next_section]
    else:
        deps_content = deps_section

    print("Содержимое секции dependencies:")
    print(deps_content)
    
    
def url_raw_maker(repo_url): #Этап2
    raw_url = repo_url.replace("github.com", "raw.githubusercontent.com") + "/main/Cargo.toml"
    return raw_url

def download_cargo_toml(raw_url):
    try:
        with urllib.request.urlopen(raw_url) as response:
            cargo_content = response.read().decode('utf-8')
            return cargo_content
    except urllib.error.URLError as e:
        print(f"Ошибка загрузки: {e}")
        return None
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
        return None
    
def analyser(config): #Этап2
    repo_url = config["repository_url"]
    print(f"Анализ репозитория: {repo_url}")
    
    raw_url = url_raw_maker(repo_url)
    print(f"Raw URL: {raw_url}")
    
    cargo_content = download_cargo_toml(raw_url)
    if cargo_content is None:
        print("Файл Cargo.toml не был прочитан")
        return None
    else:
        print("Cargo.toml успешно загружен")
        return cargo_content

def main():
    config = read_xml()
    if config:
        print("*Конфигурационный файл прочитан")
        for key, value in config.items():
            print(f"{key}: {value}")
    else:
        print("Ошибка чтения конфигурации")
        return
        
    cargo_content = analyser(config)
    dependencies_find(cargo_content)
    

if __name__ == "__main__":
    main()
