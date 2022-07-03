# Steel Eye Assignment By Animesh Shrivatri

### In this assignment I created an API which is connected with elasticsearchcloud using API's. 

1.  [Introduction](#org4d07f0e)
2.  [About Database](#orgf12f703)
3.  [API framework](#org7105ef8)
4.  [Installation](#org7948595)
5.  [Endpoints](#org90176e9)
    3.  [Orders search](#orgc4edae7)
    4.  [Advanced search](#org6016d2e)
    5.  [Bonus points](#orgf4ad3e9)


<a id="org4d07f0e"></a>
### Introduction
This is web API created by Animesh Shrivatri using elastic search we where I created different different API's like Searching, Advance Searching, Sorting, Check Databse, Insert into database, etc..


<a id="orgf12f703"></a>
### About Database
Here for save setup time I use elastic cloud whose credentials are saved into config file
I implemented some of features like sorting, range, etc.. using elastic search queries.

<a id="org7105ef8"></a>
### API framework
This API is made up with FastAPI as assignment doc suggest and pydantic

<a id="org7948595"></a>
### Installation
clone the repo

``` git clone  ```

just install fastAPI and Server

``` pip install fastapi ```

``` pip install "uvicorn[standard]" ```

ans some more pkg like pandas, requests like that if not installed already

``` pip install pandas ```

``` pip install requests ```

To run the API

``` uvicorn main:app --reload ```


<a id="org90176e9"></a>
### Endpoint

When you run server then you saw proxy like ``` localhost:8000 ``` or something else just assume that is your base url

let assume proxy is ``` localhost:8000 ```

| ## Route | ## Sending Fromat | ## Sending Example | ## Response Fromat | ## Description |
|---|---|---|---|---|

