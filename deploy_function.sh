cp requirements.txt src/requirements.txt
gcloud functions deploy data_acquisition \
  --entry-point run_tweets_acquisition \
  --region europe-west2 \
  --runtime python37 \
  --trigger-http \
  --allow-unauthenticated
rm src/requirements.txt
