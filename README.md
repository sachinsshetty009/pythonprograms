# pythonprograms
A list of python program.

# Build Information

## Docker build (version: Docker version 20.10.8, build 3967b7d)
1) docker build . -t name            // Docker build
2) docker run -d --name name --rm -p 8090:8080 -p 8091:8081 -p 8092:8082 -ti name:latest // Docker run (multi port for test program 2)
3) docker exec -it name bash. // docker shell enter
4) cd ./programs/

### Run program 1
1) python3 ./program1/ -i 0 -o 0 --log // With log X(0) Y(0)
2) python3 ./program1/ -i 0 -o 1 --log // With log X(0) Y(1)
3) python3 ./program1/ -i 0 -o 1 and python3 ./program1/ -i 0 -o 0 // Without log X(0) Y(0) & X(0) Y(1)
4) python3 ./program1/UT // UT execution

### Run program 2
1) python3 ./program2/ -i ./program2/input.json
2) python3 ./program2/ -i ./program2/input1.json

### Run program 3
1) python3 ./program3/ 

Testing server 
1) Open browser and lauch three tabs.
2) Type the following IP request in the lauched tabs http://0.0.0.0:8090/, http://0.0.0.0:8091/ and http://0.0.0.0:8092/, respectively.
3) Post three request, the receiption of the server. Server will exit.


### Run program 4
1) python3 ./program4/  New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
