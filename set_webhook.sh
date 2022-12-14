echo Please provide webhook url?
read webhookurl 
echo Please provide web token?
read bottoken
curl ${webhookurl}telegram_open_ai
curl https://api.telegram.org/bot$bottoken/setWebhook?url=${webhookurl}telegram_open_ai