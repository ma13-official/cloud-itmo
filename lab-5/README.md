# Лабораторная 5


## Цель работы:
Сделать мониторинг сервиса, поднятого в кубере (использовать, например, prometheus и grafana). Показать хотя бы два рабочих графика, которые будут отражать состояние системы. Приложить скриншоты всего процесса настройки.

## Ход работы

Для выполнения работы было принято решение развернуть nginx и мониторить его.
kubectl был установлен вместе с Docker Desktop, поэтому проблем не возникло.
### Глава 1 - Nginx и Nginx-exporter
Был написан deplyment и service для nginx и nginx-exporter:
```
apiVersion: apps/v1
kind: Deployment
metadata:
 name: nginx-deployment
 labels:
   app: nginx
spec:
 replicas: 1
 selector:
   matchLabels:
     app: nginx
 template:
   metadata:
    labels:
      app: nginx
   spec:
     containers:
     - name: nginx
       image: nginx:latest
       ports:
       - name: http
         containerPort: 10
     - name: nginx-exporter
       image: nginx/nginx-prometheus-exporter:latest
       args:
         - --nginx.scrape-uri=http://127.0.0.1:1010/metrics
       ports:
        - name: metrics
          containerPort: 9113
---
apiVersion: v1
kind: Service
metadata:
 name: nginx-service
 labels:
   app: nginx
spec:
 type: LoadBalancer
 selector:
   app: nginx
 ports:
   - name: metrics
     port: 9113
     targetPort: 9113
   - name: http
     port: 10
     targetPort: 10
     protocol: TCP
```


