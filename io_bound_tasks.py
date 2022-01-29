import requests
import time

def download_stie(url, session):
    with session.get(url) as response:
        print(f'Read {len(response.content)} from {url}')

def downlaod_all_sites(sites):
    with requests.Session() as session:
        for url in sites:
            download_stie(url,session)

if __name__ == '__main__':
    sites=["https://www.naver.com"]*10
    start_time = time.time()
    downlaod_all_sites(sites)
    duration = time.time()-start_time
    print(f'Download  {len(sites)} in {duration} seconds')