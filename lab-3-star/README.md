# Установка helm

Перед началом работы был установлен необходимый нам инструмент

![1.png](./images/1.png)


# Создание чарта

С помощью команды `helm create my-chart` был сгенерирован шаблон

![2.png](./images/2.png)

В файле [values.yaml](./my-chart/values.yaml) были изменены некоторые параметры в соответствии с параметрами сервисов из 3 лабы:
```yaml
image.repository: php-app
service.type: NodePort
```

Сюда же были вынесены переменные окружения, которые позже будут подтянуты при деплое сервисов:
```yaml
env:
  MYSQL_DATABASE: "cloud_lab3"
  MYSQL_USER: "dshevelev"
  MYSQL_PASSWORD: "1234"
  MYSQL_ROOT_PASSWORD: "0000"
```

Также в файле [deployment.yaml](./my-chart/templates/deployment.yaml) в `spec.template.spec.containers` был добавлен массив env: переменные окружения подтягиваются из values.yaml:

![3.png](./images/3.png)

Дальше были созданы две версии одного и того же образа, после чего были запушены в minikube:

![4.png](./images/4.png)


# Запуск первой версии приложения и обновление

![5.png](./images/5.png)

Сервис был запущен

![6.png](./images/6.png)

Было проверено, что это нужная версия приложения

![7.png](./images/7.png)

Затем чарт был обновлен до версии 1.1.0

![8.png](./images/8.png)

Как можно заметить, обновленная версия имеет некоторые изменения

![9.png](./images/9.png)