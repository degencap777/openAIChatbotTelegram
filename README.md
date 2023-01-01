# This is OpenAI Telegram Bot 

# Use Heroku CLI to deploy this bot 

deploy repo to heroku
```
git add .
git commit -m "initial commit"
git push heroku master
```

Use the heroku ps command to scale web dynos (worker=1) [refer procfile]
```
heroku ps:scale worker=1
```

check logs details
```
heroku logs --tail
```