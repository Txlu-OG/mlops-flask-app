#!/usr/bin/env bash

curl -X POST \
  https://txlu-og-crb0e7dqaga7eucx.canadacentral-01.azurewebsites.net/predict \
  -H "Content-Type: application/json" \
  -d '{"features":[2,3,4,5]}'