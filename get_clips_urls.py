import json
import re
from datetime import datetime

import requests
from bs4 import BeautifulSoup
from munch import DefaultMunch


def get_clips_urls(episode_link):
    print('get urls 69')
    r = requests.get(episode_link)
    soup = BeautifulSoup(r.content, 'html.parser')
    s = soup.find('script', id='__NEXT_DATA__')
    tree = y = json.loads(s.text)
    tree = DefaultMunch.fromDict(tree)
    page_props = tree.props.pageProps

    urls = page_props.preselectedStory.premiumStory.playerStory.snapList
    urls = [e.snapUrls.mediaUrl for e in urls]
    # urls = [a.split('.111?')[0] for a in urls]

    episode = page_props.preselectedStory.premiumStory.playerStory.storyTitle.value
    show = page_props.publicProfileInfo.title
    episode_num = page_props.preselectedStory.premiumStory.episodeNumber
    season_num = page_props.preselectedStory.premiumStory.seasonNumber
    date = page_props.preselectedStory.premiumStory.timestampInSec.value
    date = datetime.fromtimestamp(int(date))
    date = str(date.date())
    title = str(episode) + '_' + str(show) + '_S' + str(season_num) + '_EP' + str(
        episode_num) + '_' + date
    title = re.sub(r'[^\w\d-]', '_', title)
    title = title + ".mp4"
    return title, urls


def get_title_urls_old(episode_link):
    r = requests.get(episode_link)
    soup = BeautifulSoup(r.content, 'html.parser')
    s = soup.find('script', id='__NEXT_DATA__')
    tree = y = json.loads(s.text)
    tree = DefaultMunch.fromDict(tree)
    page_props = tree.props.pageProps

    urls = page_props.preselectedStory.premiumStory.playerStory.snapList
    urls = [e.snapUrls.mediaUrl for e in urls]
    urls = [a.split('.111?')[0] for a in urls]

    episode = page_props.preselectedStory.premiumStory.playerStory.storyTitle.value
    show = page_props.publicProfileInfo.title
    episode_num = page_props.preselectedStory.premiumStory.episodeNumber
    season_num = page_props.preselectedStory.premiumStory.seasonNumber
    date = page_props.preselectedStory.premiumStory.timestampInSec.value
    date = datetime.fromtimestamp(int(date))
    date = str(date.date())
    title = str(episode) + '_' + str(show) + '_S' + str(season_num) + '_EP' + str(
        episode_num) + '_' + date
    title = re.sub(r'[^\w\d-]', '_', title)
    title = title + ".mp4"
    return title, urls
