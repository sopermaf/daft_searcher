from daftlistings import Daft, RentType
import json

import results


def main():
    '''Search and provid option to contact each new ad'''
    with open('config/contact_details.json') as contact_file:
        contact_details = json.load(contact_file)
    
    new_listings = search_apts()
    num_of_listings = len(new_listings)

    for i, listing in enumerate(new_listings):
        print(f"\n\n******ADVERTISMENT {i+1} of {num_of_listings}******")
        print(f"{listing.description}\n€{listing.price}\n{listing.daft_link}")
        
        contact = input("Contact Ad? [y/n]: ")
        while contact.lower() not in {'y', 'n'}:
            contact = input('Options are only ["y", "n"]: ')

        if contact.lower() == 'y':
            contact_advertiser(listing, **contact_details)


def search_apts():
    '''
    Search Apts using the config file settings
    Returns
    -------
    list (listings)
    '''
    with open('config/search_config.json') as search_config_file:
        search_config = json.load(search_config_file)

    daft = Daft()
    daft.set_county(search_config['county'])
    daft.set_listing_type(RentType.APARTMENTS)
    daft.set_min_price(search_config['price']['min'])
    daft.set_max_price(search_config['price']['max'])

    listings = daft.search()

    # filter out seen results
    listings_seen = results.get_listings_seen_set()
    new_listings = [listing for listing in listings if listing.daft_link not in listings_seen]
    results.update_listings_seen(*listings)

    print(f"Found {len(new_listings)} new listings")

    return new_listings


def contact_advertiser(listing, *, name, phone, email, msg):
    '''Contact listing using contact_information'''
    contact = listing.contact_advertiser(
        name=name,
        contact_number=phone,
        email=email,
        message="\n".join(msg)
    )

    if contact:
        print("Advertiser contacted")


if __name__=="__main__":
    main()
