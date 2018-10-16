# Hello World as a Service (HWaaS)

## Requirements  
 We want to make Hello World as a Service (HWaaS.) For some reason, clients are actually paying us to print "hello, world!" repeatedly in the terminal. Because we want to be webscale, we'll use rq, which will allow us to have multiple servers printing hello world, and multiple clients submitting requests to print hello world.
 
 Please write the following:
 

 - A function that simply prints the only argument given to it
 - A client that, once a second, calls this function via rq to print "hello, world!"
 - A script for starting HWaaS, including the rq worker and the client.
 - On dev machines, we'll execute it like so: `./hwaas 1 1`, which will start 1 rq worker, and 1 client. This will print hello world once a second, allowing the devs to easily debug and improve the application.
 - On prod, we'll execute it like so: `./hwaas 10 1000`, which will start 10 servers, and 1000 clients. This will print hello world a thousand times a second, which will make the clients pay us a lot of money.
 
Feel free to use your choice of containerization of other technologies for the script. However it's important that:

This script is trivially runnable on mac, i.e. the user should not need to install redis, rq, etc. to get up and running. They should be able to just run `hwaas`.

There's minimal risk of dropped hello worlds if a lot of rq workers / clients are running.
 
## Design Decisions 

 - Utilized Python rq module to establish queuing for parallel operaations 
     - Redis container implemented to provide queuing mechanism
     
 - Docker compose was used to handle containerization and orchestration
    
       
 - Usability & Output:     
     - A simple bash script to call the appropriate docker compose bits was implemented to remain platform/OS agnostic
       
  
## Future Improvements  
  
 -  Better wrapper script (hwaas) to provide more robust handling of execution
 -  Implement a Flask API to handle POST of items to the queue in a Asyncronous fashion.
      
## Usage  
 - Build  
	 - Prequisites:
		 - docker 

	```		 
	git clone https://github.com/ride808/hwaas.git  
	cd hwaas 
	docker-compose build --no-cache
	```
 - Run  

	 - Using Bash Script:
	 
	```
	./hwaas <number of workers>  <number of clients>
	ex.
	./hwaas 1 1
	
	To exit the bash script utilize CTRL-C
	```
- Using Docker Compose

	```
docker-compose up -d
docker-compose scale worker=1
docker-compose logs -f worker | grep -i " Hello World" &
docker-compose run -e CLIENTS=1 client 
```

