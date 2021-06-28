# Docker Compose Elastic Stack
A Docker Compose project for microservices monitoring, based on ELK integrated with Filebeat and Logstash.

Description
------------------------------
This project makes microservices monitoring simple as one click!

Thanks to Filebeat for collecting our Nginx logs,
to Logstash for parsing and indexing these collected logs into ElasticSearch
And for Kibana about great visualizations of our data:

                                                Nothing is invisible! 

Prerequisites
------------
1. Updated Docker version (20.10.7)
2. Docker Compose (2.0.0)
2. Local image repository clean from version collisions against the project's images.


CookBook
------------------------------
1. clone the repository.
2. cd to the root directory called "DockerComposeElasticStack-main".
3. make sure your docker platform is running.
4. run docker compose up -d.
5. open kibana portal on "http://localhost:5601" or from inside the local compose network on "http://kibana:5601"
6. open the log view by choose the Discover section in the kibana menu.
7. open the data table visualization by choose the visualize section in the kibana menu.
5. Enjoy :)

Self-Test CookBook Using "ComposeTest"
------------------------------
This ComposeTest will check that things work as expected.
1. cd to composetest directory.
2. run docker compose up -d.

Two of the containers will access with https to nginx (on of them once, the second twice).
Six of the containers will access by http to nginx (once to six times according to the environment variable configured to the container).

We should see a large number of new hits in the "discover" section.
Additionally, on the data table visualization we will see the top 5 IPs who tried to access to Nginx on http.
The sixth container is not shown on this table because it is a top 5 table.

Now we can be sure that our microservices monitoring system is a war machine!

Some Credentials
------------------------------
Kibana Login:
1. Username: elastic
2. Password: Change0Me$

Change password by editing the ".env" file

Let's Tag Some Versions!
------------------------------
1. Filebeat,Logstash,ElasticSearch,Kibana: 7.9.2
2. Nginx: 1.21
3. Alpine: 3.14.0

