# How to Use

1. Setup `contact_details.json` using the example in the config file
2. Install pipenv from Pipfile
3. Run as `python search.py`

<br>

# Details

The program currently searches for apartments
between 800-1500 in Dublin City and stores
previously seen results in `daft_results.json` using the
url to ensure the new results are unique.

<br>

# Desired Features
## Results
1. Store in DB with all details
2. Option to contact previously seen listing
3. Show details on contacted properties
4. View stats on results found

### Run options
1. Config file for search settings
2. Use env vars as default for search
3. Flags for different modes,
    - get new listing
    - view listings for particular day
    - contact previous listing
    - stats mode