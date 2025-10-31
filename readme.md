# Инструмент визуализации графа зависимостей

## Этап 1: Минимальный прототип с конфигурацией

### Описание
CLI-приложение для чтения конфигурации из XML файла.

### Использование
1. Создайте файл `config.xml` в той же папке
2. Заполните его по примеру ниже
3. Запустите: `python graph.py`

### Пример config.xml
```xml
<?xml version="1.0" ?>
<configuration>
    <package_name>name</package_name>
    <repository_url>https://url</repository_url>
    <test_repo_mode>false_or_true</test_repo_mode>
    <package_version>1.0</package_version>
    <output_filename>my_graph.png</output_filename>
</configuration>