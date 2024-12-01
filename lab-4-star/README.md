docker-compose up -d
![image](https://github.com/user-attachments/assets/e30fb982-60e8-4ef1-a9e7-8d3cddbdfddf)

http://localhost:8200/
![image](https://github.com/user-attachments/assets/7b08b05a-d71f-4eb0-9d17-dc71da7af125)

docker exec -it vault sh
vault login root
vault login -address=http://127.0.0.1:8200 root
![image](https://github.com/user-attachments/assets/b1dc2e7f-d2d3-4ecb-aad2-df921b0aff80)

vault kv put secret/myapp DB_USER=myuser DB_PASSWORD=mypassword
vault kv get -address=http://127.0.0.1:8200 secret/myapp
vault token create -address=http://127.0.0.1:8200 -policy=root
![image](https://github.com/user-attachments/assets/26b28d5d-8b61-4ffc-9d95-a2158711df02)

Секреты
![image](https://github.com/user-attachments/assets/040f6afd-d56e-4e2a-a0f0-87582d4d7363)



![image](https://github.com/user-attachments/assets/c4552038-be3c-47e6-a888-171d6f69cb25)
