# this is a sample of an api with flask and mongodb

The database contains list of kitchen utensils with their uses

All items in the db can be viewed using https://api-testq.herokuapp.com/utensils?sort=

The sort query can take asc or desc to specify ascending and descending arrangement by names respectively

An item can be viewed using https://api-testq.herokuapp.com/utensils/NAME_OF_ITEM

An item can be deleted using https://api-testq.herokuapp.com/utensils/NAME_OF_ITEM and specifying the http verb as 'DELETE' (Hint: use postman)

An item can be updated or modified using https://api-testq.herokuapp.com/utensils/NAME_OF_ITEM and specifying the http verb as 'PUT' (Hint: use postman)

An item can be added using https://api-testq.herokuapp.com/utensils with the 'POST' method and sending a request in the format {"name": "name of item to add", "use" : "use of item"} (Hint: use postman)
