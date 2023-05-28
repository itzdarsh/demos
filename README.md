# demos

1. Create Atlas M0 Cluster as explained in the https://www.mongodb.com/docs/atlas/tutorial/deploy-free-tier-cluster/ using UI
2. Copy the cluster URI and load the attached timeseries file
   ```
   mongoimport --uri <URI> --db test --collection tsDemo --type csv --headerline --file nifty50.csv
   ```
   _replace <URI> with the uri you copied by clcking connect button_
 3. Run the `pytseries.py` to connect atlas cluster and play with the data
   ```
   python3 pytseries.py
   ```
