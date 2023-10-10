
# Приложение для Благотворительного фонда поддержки котиков QRKot.




### О проекте

Данный проект призван помочь всем котикам, и сделать мир лучше



### Запуск
Клонировать репозиторий и перейти в него в командной строке:

```
git clone 
```

```
cd cat_charity_fund
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```
Запуск
 ```
# Из дирректории cat_charity_fund

uvicorn app.main:app --reload   

 ```

### Технологии
Проект написан на Python и фреймворке FastAPI, а все используемые технологии удобно расположены в файле requirements.txt

### Автор
Самсонов Дмитрий