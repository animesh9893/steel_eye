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

## use those points with any combination of search like ```?q=funk&maxPrice=1000```

| ## Route | ## Sending Fromat | ## Sending Example | ## Response Fromat | ## Description |
|---|---|---|---|---|
| ``` / ``` | n/a | n/a | ```{"error":false,"error_cause":null,"data":[{Trade Details}]}``` | This will return random trades details |
|```/check```| na | na | [checkResponse](#checkResponse) | Only for checking if database is working or not |
|---|---|---|---|---|
|```/search```| ```\``` | ```http://localhost:8000/search``` | [checkResponse](#searchWithNoParam) | Work Like normal ```/``` request |
|---|---|---|---|---|
|```/search?q=```| ```?q=``` | ```http://localhost:8000/search?q=funk``` | [checkResponse](#searchWithQParam) | Work Like normal ```/``` request |
|---|---|---|---|---|
|```/search?assetClass=```| ```?assetClass=``` | na | search assest class | na |
|---|---|---|---|---|
|```/search?size=```| ```?size=``` | na | response size | na |
|---|---|---|---|---|
|```/search?minPrice=```| ```?minPrice=``` | na | min price | na |
|---|---|---|---|---|
|```/search?maxPrice=```| ```?maxPrice=``` | na | max price | na |
|---|---|---|---|---|
|```/search?start=```| ```?start=``` | na | start date | na |
|---|---|---|---|---|
|```/search?tradeType=```| ```?tradeType=``` | na | tradetype buy or sell | na |
|---|---|---|---|---|
|```/search?pitId=```| ```?pitId=``` | na | pagination id need to pass if available or leave | na |
|---|---|---|---|---|
|```/search?sortD=```| ```?sortD=``` | na | # This will pass multiple times to sort descending pass field name as value | na |
|---|---|---|---|---|
|```/search?sortA=```| ```?sortA=``` | na | # This will pass multiple times to sort descending pass field name as value  | na |
|---|---|---|---|---|
|```/search?end=```| ```?end=``` | na | # End date | na |
|---|---|---|---|---|


# Their is So many functionality like Pingation and all
You can checkout code for that













[Endpoints](#org90176e9)
<a id="checkResponse"></a>
```{"resp":"{\n  \"name\" : \"instance-0000000000\",\n  \"cluster_name\" : \"8730d251708446b8a456404c603e9cce\",\n  \"cluster_uuid\" : \"qZqXxIq0TJ6JTWrGcQJ3Pg\",\n  \"version\" : {\n    \"number\" : \"8.3.1\",\n    \"build_type\" : \"docker\",\n    \"build_hash\" : \"b9a6b2867996ba92ceac66cb5bafc6db25e7910e\",\n    \"build_date\" : \"2022-06-29T18:39:55.731992798Z\",\n    \"build_snapshot\" : false,\n    \"lucene_version\" : \"9.2.0\",\n    \"minimum_wire_compatibility_version\" : \"7.17.0\",\n    \"minimum_index_compatibility_version\" : \"7.0.0\"\n  },\n  \"tagline\" : \"You Know, for Search\"\n}\n"}```



[Endpoints](#org90176e9)
<a id="searchWithNoParam"></a>
```
{"error":false,"error_cause":null,"data":[{"assetClass":"Drama Mystery Thriller","counterparty":"Huels, Hahn and Reichert","instrumentId":"318142211-8","instrumentName":"LMBS","tradeDateTime":"2021-07-07 12:52:00","tradeDetails":{"buySellIndicator":"BUY","price":912.97,"quantity":899},"tradeId":899,"trader":"Gabbie Dann"},{"assetClass":"Drama Romance","counterparty":"Gerhold Group","instrumentId":"055101820-8","instrumentName":"CRSP","tradeDateTime":"2021-07-07 14:57:00","tradeDetails":{"buySellIndicator":"SELL","price":65.36,"quantity":2946},"tradeId":2946,"trader":"Clair Whelband"},{"assetClass":"Drama Romance","counterparty":"Cormier-Kihn","instrumentId":"375816436-2","instrumentName":"TTMI","tradeDateTime":"2021-07-07 16:32:00","tradeDetails":{"buySellIndicator":"SELL","price":352.89,"quantity":395},"tradeId":395,"trader":"Abey Longfellow"},{"assetClass":"Documentary","counterparty":"Greenfelder Group","instrumentId":"189190094-3","instrumentName":"UFS","tradeDateTime":"2021-07-07 19:26:00","tradeDetails":{"buySellIndicator":"BUY","price":169.54,"quantity":9},"tradeId":9,"trader":"Mycah Blesing"},{"assetClass":"Documentary","counterparty":"Considine, Harber and MacGyver","instrumentId":"357013240-4","instrumentName":"SKYW","tradeDateTime":"2021-07-07 22:30:00","tradeDetails":{"buySellIndicator":"SELL","price":532.73,"quantity":1365},"tradeId":1365,"trader":"Quint Creany"},{"assetClass":"Children Drama","counterparty":"Stoltenberg, Denesik and Bartoletti","instrumentId":"594685714-2","instrumentName":"WB","tradeDateTime":"2021-07-08 13:01:00","tradeDetails":{"buySellIndicator":"BUY","price":110.2,"quantity":4092},"tradeId":4092,"trader":"Inna Ell"},{"assetClass":"Adventure Drama Romance","counterparty":"Rogahn and Sons","instrumentId":"047074052-3","instrumentName":"DELT","tradeDateTime":"2021-07-16 19:18:00","tradeDetails":{"buySellIndicator":"SELL","price":356.8,"quantity":4937},"tradeId":4937,"trader":"Gallard Ashall"},{"assetClass":"Documentary","counterparty":"Ortiz and Sons","instrumentId":"744383935-9","instrumentName":"APPN","tradeDateTime":"2021-07-17 02:40:00","tradeDetails":{"buySellIndicator":"BUY","price":868.62,"quantity":2511},"tradeId":2511,"trader":"Gilburt Mattiuzzi"},{"assetClass":"Action Adventure Drama","counterparty":"Vandervort LLC","instrumentId":"242922263-9","instrumentName":"MSD","tradeDateTime":"2021-07-17 05:12:00","tradeDetails":{"buySellIndicator":"SELL","price":437.13,"quantity":1224},"tradeId":1224,"trader":"Yulma Jouanny"},{"assetClass":"Crime Drama Romance","counterparty":"Sawayn Group","instrumentId":"625671270-6","instrumentName":"PSA^X","tradeDateTime":"2021-07-17 18:26:00","tradeDetails":{"buySellIndicator":"BUY","price":603.17,"quantity":5685},"tradeId":5685,"trader":"Farrel Benton"}]}
```


[Endpoints](#org90176e9)
<a id="searchWithQParam"></a>
```{"error":false,"error_cause":null,"data":[{"assetClass":"Children Comedy Romance","counterparty":"Funk LLC","instrumentId":"549871001-1","instrumentName":"IBOC","tradeDateTime":"2022-03-31 12:22:00","tradeDetails":{"buySellIndicator":"BUY","price":441.16,"quantity":5014},"tradeId":5014,"trader":"Rafaelita Bonas"},{"assetClass":"Drama","counterparty":"Funk-Boyle","instrumentId":"806301325-5","instrumentName":"ARDM","tradeDateTime":"2022-05-22 12:46:00","tradeDetails":{"buySellIndicator":"SELL","price":709.05,"quantity":1696},"tradeId":1696,"trader":"Mal McGunley"},{"assetClass":"Documentary","counterparty":"Funk and Sons","instrumentId":"766455428-4","instrumentName":"BATRK","tradeDateTime":"2021-12-14 09:41:00","tradeDetails":{"buySellIndicator":"BUY","price":273.89,"quantity":5106},"tradeId":5106,"trader":"Rourke MacLaughlin"},{"assetClass":"Documentary","counterparty":"Funk, Kirlin and Okuneva","instrumentId":"496102655-7","instrumentName":"CYHHZ","tradeDateTime":"2021-08-05 03:19:00","tradeDetails":{"buySellIndicator":"BUY","price":116.33,"quantity":1042},"tradeId":1042,"trader":"Merrili Furmage"}]}```


[Endpoints](#org90176e9)
<a id="searchWithQParam"></a>
``` 

```

# Created By Animesh Shrivatri (animesh9893)
