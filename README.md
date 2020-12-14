# WebAPI_LoadTest_locust_Demo

### 说明

- locust运行测试脚本
- pipenv管理python虚拟环境
- docker让本地和服务器在相同环境上执行测试脚本

### 执行压测脚本基本指令

- locust -H http://localhost:8080/api/v1/app -u 30 -r 2 -t 60s --headless --csv example

### 配合docker采用分布式结构

如果并发较高，可以采用多个C端对服务器进行测试

- master机请使用docker-compose-master文件中的内容覆盖docker-compose.yml
  - -H是被测目标地址
  - 运行指令 docker-compose up -d
- worker机请使用docker-compose-worker文件中的内容覆盖docker-compose.yml
  
  - --master-host是master主机地址
  
  - 运行指令 docker-compose up -d

### 参考

- locust https://github.com/locustio/locust
- locust官方文档 https://docs.locust.io/en/stable/

