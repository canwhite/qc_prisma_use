### prisma_test
this orm lib fit for node and python, so select it to run test

### key point  
* push to db 
* gen client 
* model 

### how to use

1. python with prisma 
```
pre：
pip install -U prisma

firstly you need to create schema.prisma by yourself
include：
datasource 、 generator、model

then run:
prisma db push

push model to db ，and gen client

if model is change, it suggest that run prisma db push firstly ,
the run prisma genarate 


```

2. node with prisma
```
schema.prisma could generate automatically with running :
npx prisma init

then write model in schema.prisma 

and then: 
npx prisma migrate dev --name init
in order to push model to db

create client:
npx prisma generate 

if model is change, it suggest that run prisma migrate dev firstly in order to connect to db , and then , create client 

```


### cursor rules init
[rules](https://www.cursor-start.com/)
[python with prisma](https://prisma-client-py.readthedocs.io/en/stable/) 
[node with prisma](https://www.prisma.io/docs/getting-started/quickstart-sqlite)

