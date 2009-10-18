#!/usr/bin/python

import json
import pylast
import sys

API_KEY = "your-api-key"
API_SECRET = "your-api-secret"

class UserData:
    def __init__(self):
        self.data = []

class WeekArtistData:
    def __init__(self):
        pass

class ArtistPlayData:
    def __init__(self, name, count):
        self.bandName = name
        self.playCount = count

def crawl(username_filename):
    network = pylast.get_lastfm_network(api_key = API_KEY,
                                        api_secret = API_SECRET)
    for username in open(username_filename, 'r').readlines():
        try:
            crawl_user_data(username.strip(), network)
        except:
            sys.stderr.write('ERROR in processing user %s; continuing on.\n' %
                             username)

def crawl_user_data(username, network):
    print 'getting user data for %s...' % username
    user = network.get_user(username)
    user_data = UserData()
    user_data.name = username
    user_data.weeklyCharts = get_weekly_charts(user, network)
    outfile = open(make_filename(username), 'w')
    dump_user_data_to_file(user_data, outfile)
    outfile.close()

def get_weekly_charts(user, network):
    res = []
    for dates in user.get_weekly_chart_dates():
        res.append(get_weeks_artist_charts(
                       user.get_weekly_artist_charts(dates[0], dates[1]),
                       dates[0],
                       dates[1])
                  )
    return res

def get_weeks_artist_charts(topItems, begDate, endDate):
    weekData = WeekArtistData()
    weekData.beginningDate = begDate
    weekData.endDate = endDate
    weekData.data = [ArtistPlayData(x.item.get_name(), x.weight) for x in topItems]
    return weekData

def make_filename(username):
    return 'data/' + username + '.json'

def dump_user_data_to_file(user_data, outfile):
    json.dump({'username': user_data.name,
               'charts':
                 [ {'startDate': x.beginningDate,
                    'endDate': x.endDate,
                    'counts': [ { 'bandName': y.bandName,
                                  'playCount': y.playCount
                                }
                                for y in x.data
                              ]
                   }
                   for x in user_data.weeklyCharts
                 ]
              },
              outfile,
              sort_keys=True,
              indent=4
             )

if __name__ == '__main__':
    crawl(sys.argv[1])
