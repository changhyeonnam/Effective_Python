import concurrent.futures
import requests
import threading
import time

thread_local = threading.local()

def get_session():
    if not hasattr(thread_local,"session"):
        thread_local.session = requests.Session()
    return thread_local.session

def download_stie(url):
    session = get_session()
    with session.get(url) as response:
        print(f'Read {len(response.content)} from {url}')

def downlaod_all_sites(sites):
    with requests.Session() as session:
        for url in sites:
            download_stie(url)

if __name__ == '__main__':
    sites=[
        "https://www.naver.com"
    ]*10
    start_time = time.time()
    downlaod_all_sites(sites)
    duration = time.time()-start_time
    print(f'Download  {len(sites)} in {duration} seconds')

