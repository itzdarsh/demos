# demos

1. Download the git and unzip the file
2. Install the dependency
   ```
   python -m pip install -r requirements.txt
   ```
         
3. Create Atlas M0 Cluster as explained in the https://www.mongodb.com/docs/atlas/tutorial/deploy-free-tier-cluster/ using UI
4. Copy the cluster URI and load the attached timeseries file
   ```
   mongoimport --uri <URI> --db test --collection tsDemo --type csv --headerline --file nifty50.csv
   ```
   _replace <URI> with the uri you copied by clcking connect button_
5. Run the `pytseries.py` to connect atlas cluster and play with the data
   ```
   python3 pytseries.py
   ```
