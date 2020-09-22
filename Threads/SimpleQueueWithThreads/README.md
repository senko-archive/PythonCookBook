this application uses 2 separate flask server one is getting data (which is randomized)
other is for sending data. Sending is slower than getting data (with time.sleep) and 
there is a queue which producer(gets from flask API) and consumer(sends other flask API)
uses mutually.
Both consumers and producers are threads.
