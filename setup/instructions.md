# Run the docker-compose.yml file to create Postgresql and Adminer containers
- Command: docker-compose up
* This should be ran from the file where the docker-compose.yml file resides.
* The postgres container uses the .env file to load credentials. Make sure you create a .env file in the same directory and add the following fields in the file:

    POSTGRES_PASSWORD=<password>
    POSTGRES_USER=<user>
    POSTGRES_DB=car_prices

- Substitute <...> for the actual values you want to use

# To load the relevant tables in the db when it is created enter interactive mode of the container and run the commands from the car_offer_db_schema.sql file

    docker ps -a -> gives the data for existing containers; grab the id of the postgres container
    docker exec -it <postgres_container> bash -> enter the container shell
    
