# log_interface
## Запуск приложения с помощью Docker
- Запуск приложения
    ```CMD
    git clone https://github.com/sumrako/log_interface.git
    cd log_interface
    docker build -t log_interface .
    docker run -d --name log_interface -p 8000:8000 -w /code/app log_interface
    ```
После осуществите переход по ссылке `http:/localhost:8000/logs`
## Интерфейс приложения
![image](https://github.com/sumrako/log_interface/assets/67976572/88fb520e-c7c5-445d-b1ff-60cdf00f1656)
