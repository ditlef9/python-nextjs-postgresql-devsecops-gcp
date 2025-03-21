## Publish Application

```commandline
gcloud auth login
gcloud functions deploy report-pdf --gen2 --runtime=python312 --region=europe-north1 --source=. --entry-point=main --trigger-http --timeout=540 --verbosity=info --project=applications-dev-453706 --memory=256Mi
```
