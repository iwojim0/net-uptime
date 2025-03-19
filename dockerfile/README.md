1.Copy and edit config/app.json, config/services.json to current directory

2.Copy to current directory related png/ico files

3.`docker build --no-cache . -t net-uptime`

4.`docker run -it --name net-uptime -p 5000:5000 net-uptime`
