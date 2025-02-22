# AntMove

### Launch code locally 
1. **Via python2.7**

    Launch code: 
        ```python2.7 ant_movement.py```
        
    Launch tests:
        ```python2.7 test_ant_movement.py```

2. **Via make**

    Launch code: 
        ```make run```

    Launch tests:
        ```make test```

### Launch via Docker

1. Build docker image
    
    ```docker build -t ant-python .```

2. Run container
    
    ```docker run -d --name ant-move ant-python```
3. Launch code

    ```docker exec -ti ant-move python ant_movement.py```
4. Launch tests:

    ```docker exec -ti ant-move python test_ant_movement.py```