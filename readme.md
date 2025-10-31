# Инструмент визуализации графа зависимостей

## Этап 1: Минимальный прототип с конфигурацией
- Чтение конфигурации из XML файла
- Валидация параметров
- Вывод настроек в формате ключ-значение

## Этап 2: Парсинг зависимостей из Cargo.toml 
- Загрузка Cargo.toml из GitHub репозитория
- Парсинг секции [dependencies]
- Извлечение имен и версий пакетов
- Использование только стандартных библиотек Python

## Использование

### 1. Создайте config.xml
```xml
<?xml version="1.0" ?>
<configuration>
    <package_name>ferris-says</package_name>
    <repository_url>https://github.com/rust-lang/ferris-says</repository_url>
    <test_repo_mode>false</test_repo_mode>
    <package_version>0.2.1</package_version>
    <output_filename>dependencies.png</output_filename>
</configuration>