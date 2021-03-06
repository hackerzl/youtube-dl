from __future__ import unicode_literals

from .mtv import MTVServicesInfoExtractor


class BellatorIE(MTVServicesInfoExtractor):
    _VALID_URL = r'https?://(?:www\.)?bellator\.com/[^/]+/[\da-z]{6}(?:[/?#&]|$)'
    _TESTS = [{
        'url': 'http://www.bellator.com/fight/atwr7k/bellator-158-michael-page-vs-evangelista-cyborg',
        'info_dict': {
            'id': 'b55e434e-fde1-4a98-b7cc-92003a034de4',
            'ext': 'mp4',
            'title': 'Douglas Lima vs. Paul Daley - Round 1',
            'description': 'md5:805a8dd29310fd611d32baba2f767885',
        },
        'params': {
            # m3u8 download
            'skip_download': True,
        },
    }, {
        'url': 'http://www.bellator.com/video-clips/bw6k7n/bellator-158-foundations-michael-venom-page',
        'only_matching': True,
    }]

    _FEED_URL = 'http://www.spike.com/feeds/mrss/'
    _GEO_COUNTRIES = ['US']


class ParamountNetworkIE(MTVServicesInfoExtractor):
    _VALID_URL = r'https?://(?:www\.)?paramountnetwork\.com/[^/]+/[\da-z]{6}(?:[/?#&]|$)'
    _TESTS = [{
        'url': 'http://www.paramountnetwork.com/episodes/j830qm/lip-sync-battle-joel-mchale-vs-jim-rash-season-2-ep-13',
        'info_dict': {
            'id': '37ace3a8-1df6-48be-85b8-38df8229e241',
            'ext': 'mp4',
            'title': 'Lip Sync Battle|April 28, 2016|2|209|Joel McHale Vs. Jim Rash|Act 1',
            'description': 'md5:a739ca8f978a7802f67f8016d27ce114',
        },
        'params': {
            # m3u8 download
            'skip_download': True,
        },
    }]

    _FEED_URL = 'http://www.paramountnetwork.com/feeds/mrss/'
    _GEO_COUNTRIES = ['US']

    def _extract_mgid(self, webpage):
        root_data = self._parse_json(self._search_regex(
            r'window\.__DATA__\s*=\s*({.+})',
            webpage, 'data'), None)

        def find_sub_data(data, data_type):
            return next(c for c in data['children'] if c.get('type') == data_type)

        c = find_sub_data(find_sub_data(root_data, 'MainContainer'), 'VideoPlayer')
        return c['props']['media']['video']['config']['uri']
