import json

FILENAME = 'daft_results.json'


def update_listings_seen(*listings, filename=FILENAME):
    listings_seen = get_listings_seen_set(filename)
    
    listing_links = {listing.daft_link for listing in listings}
    listings_seen = listings_seen | listing_links

    write_listings_seen_list(filename, listings_seen)


def get_listings_seen_set(filename=FILENAME):
    '''Check for FileNotFoundError'''
    try:
        listings_seen = set(load_listings_seen(filename))
    except FileNotFoundError:
        return set()
    return listings_seen


def load_listings_seen(filename):
    '''Load a set of daft urls'''
    with open(filename) as f:
        listings = json.load(f)
    return listings


def write_listings_seen_list(filename, listings):
    '''Writes a list/set of listing urls to a json doc'''
    listings = list(listings)
    
    with open(filename, 'w+') as f:
        json.dump(listings, f)
