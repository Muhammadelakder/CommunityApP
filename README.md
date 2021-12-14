# Community
> منصه للتوصيل التشاركي   مجانيه
[![Screenshot-from-2021-12-13-15-18-28.png](https://i.postimg.cc/PrVcrC9n/Screenshot-from-2021-12-13-15-18-28.png)](https://postimg.cc/MvRt9pz9)

## متطلبات عمل التطبيق

1. **PostgreSQL and PostGIS**
    - [Download](https://www.postgresql.org/download/) .

    - [Install](https://postgis.net/install/).

2. **`python3.7` and `pip3`**

3. **[GDAL](https://gdal.org/)**

    - `sudo apt-get install libpq-dev python-dev`
    - `sudo apt-get install binutils libproj-dev gdal-bin`

    >NOTE : Try [WSL](https://ubuntu.com/wsl).

4. **Django and other dependencies**
    `pip install -r requirements.text`

## كيفية البدء

1. **انشاء قاعدة بيانات**
    >Create Postgresql Database &
    >add it to Django project.

2. **Create api key on [mapbox](https://mapbox.com/)**
    >open /home/modules/map.js &
    >add the access token.

3. **واخيرا شغل الاوامر التاليه**

    `python manage.py makemigrations stores`

    `python manage.py runserver`




# credits to:
    (https://egen.solutions/articles/thinking-of-building-a-contact-tracing-application-what-to-do-instead/).


# ساهم في المشروع
    
