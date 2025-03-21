# VideoDownloader


##Build image using
docker build --pull --rm -f 'Dockerfile' -t 'youtubedownloader:latest' '.' 


##Run image using 
docker run --platform linux/amd64 -it -v ${pwd}:/app/downloads -p 9000:8080 youtubedownloade


##Test using powershell 
### URL can be passed inside body as url param
Invoke-WebRequest -Uri "http://localhost:9000/2015-03-31/functions/function/invocations" -Method Post
 -Body '{"url":"https://www.youtube.com/watch?v=QkdkLdMBuL0"}' -ContentType "application/json"
