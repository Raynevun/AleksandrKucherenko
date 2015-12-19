0. Prerequisites
summarize-beacon uses dateutil lib to calculate datetime delta accurately. 
pip install python-dateutil
or 
sudo apt-get install python-dateutil
1. summarize-beacon
Run summarize-beacon without arguments to summarize last record from randomness beacon:
python ./bin/summarize-beacon
Or with --from --to arguments to summarize records by timestamps:
python ./bin/summarize-beacon --from "3 months 1 day 1 hour ago" --to "1 month 1 hour ago"
2. Unit tests
Run unit tests from command line to test summarize-beacon functions:
python unittest -m ./bin/test_summarize_beacon.py