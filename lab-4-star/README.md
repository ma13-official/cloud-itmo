docker-compose up -d
![image](https://github.com/user-attachments/assets/e30fb982-60e8-4ef1-a9e7-8d3cddbdfddf)

http://localhost:8200/
![image](https://github.com/user-attachments/assets/7b08b05a-d71f-4eb0-9d17-dc71da7af125)

docker exec -it vault sh
vault login root
vault login -address=http://127.0.0.1:8200 root
![image](https://github.com/user-attachments/assets/b1dc2e7f-d2d3-4ecb-aad2-df921b0aff80)
