from django.utils.datastructures import SortedDict

from tower import ugettext_lazy as _

products = SortedDict([
    ('desktop', {
        'name': _('Firefox 3.6 or earlier on Desktops/Laptops/Netbooks'),
        'extra_fields': ['troubleshooting', 'ff_version', 'os', 'plugins'],
        'tags': ['desktop'],
        'categories': SortedDict([
        ('d1', {
            'name': _('Firefox is having problems with certain web sites'),
            'extra_fields': ['sites_affected'],
            'articles': [
                {'title': 'Firefox cannot load websites but other programs can',
                 'url': '/en-US/kb/Firefox+cannot+load+websites+but+other+programs+can'},
                {'title': 'Problems using Facebook in Firefox',
                 'url': '/en-US/kb/Problems+using+Facebook+in+Firefox'},
            ],
            'tags': ['websites'],
        }),
        ('d2', {
            'name': _('Firefox is crashing or closing unexpectedly'),
            'extra_fields': ['crash_id'],
            'articles': [
                {'title': 'Firefox crashes',
                 'url': '/en-US/kb/Firefox+Crashes'},
                {'title': 'Firefox crashes when you open it',
                 'url': '/en-US/kb/Firefox+crashes+when+you+open+it'},
                {'title': 'Firefox crashes when loading certain pages',
                 'url': '/en-US/kb/Firefox+crashes+when+loading+certain+pages'},
                {'title': 'Firefox crashes when you exit it',
                 'url': '/en-US/kb/Firefox+crashes+when+you+exit+it'},
                {'title': 'The Adobe Flash plugin has crashed',
                 'url': '/en-US/kb/The+Adobe+Flash+plugin+has+crashed'},
            ],
            'tags': ['crash'],
        }),
        ('d3', {
            'name': _('I have a problem with my bookmarks, cookies, history or settings'),
            'articles': [
                {'title': 'Deleting Cookies',
                 'url': '/en-US/kb/Deleting+cookies'},
                {'title': 'Enabling and disabling cookies',
                 'url': '/en-US/kb/Enabling+and+disabling+cookies'},
            ],
            'tags': ['data'],
        }),
        ('d4', {
            'name': _('I need help learning to use a Firefox feature'),
            'articles': [
                {'title': 'How to set the home page',
                 'url': '/en-US/kb/How+to+set+the+home+page'},
                {'title': 'Private Browsing',
                 'url': '/en-US/kb/Private+Browsing'},
                {'title': 'Bookmarks',
                 'url': '/en-US/kb/Bookmarks'},
                {'title': 'Tabbed browsing',
                 'url': '/en-US/kb/Tabbed+browsing'},
                {'title': 'Location bar autocomplete',
                 'url': '/en-US/kb/Location+bar+autocomplete'},
            ],
            'tags': ['learning'],
        }),
        ('d5', {
            'name': _('I have a problem with an extension or plugin'),
            'extra_fields': ['addon'],
            'html': 'Most extensions or plugins are not written by Mozilla '
                    'and you will need to contact the people or company who '
                    'made the extension/plugin for support, if you need help '
                    'removing an extension or plugin, see <a '
                    'href="/en-US/kb/Uninstalling+add-ons">Uninstalling '
                    'add-ons</a>.',
            'tags': ['addon'],
        }),
        ('d6', {
            'name': _('I have another kind of problem with Firefox'),
            'extra_fields': ['frequency', 'started'],
            'articles': [
                {'title': 'The Adobe Flash plugin has crashed',
                 'url': '/en-US/kb/The+Adobe+Flash+plugin+has+crashed'},
                {'title': 'What is plugin-container',
                 'url': '/en-US/kb/What+is+plugin-container'},
                {'title': 'How do I edit options to add Adobe to the list of allowed sites',
                 'url': '/en-US/kb/How+do+I+edit+options+to+add+Adobe+to+the+list+of+allowed+sites'},
                {'title': 'Menu bar is mising',
                 'url': '/en-US/kb/Menu+bar+is+missing'},
            ],
            'tags': ['general'],
        }),
        ])
    }),
    ('beta', {
        'name': _('Firefox 4 betas on Desktops/Laptops/Netbooks'),
        'extra_fields': ['troubleshooting', 'ff_version', 'os', 'plugins'],
        'tags': ['beta'],
        'categories': SortedDict([
        ('b1', {
            'name': _("I'm having trouble with the look and feel of the Firefox beta"),
            'tags': ['ui'],
        }),
        ('b2', {
            'name': _('Firefox is having problems with certain web sites'),
            'extra_fields': ['sites_affected'],
            'tags': ['websites'],
        }),
        ('b3', {
            'name': _('Firefox is crashing or closing unexpectedly'),
            'extra_fields': ['crash_id'],
            'tags': ['crash'],
        }),
        ('b4', {
            'name': _('I have a problem with an extension or plugin'),
            'extra_fields': ['addon'],
            'tags': ['addon'],
        }),
        ('b5', {
            'name': _('I have another kind of problem with Firefox'),
            'extra_fields': ['frequency', 'started'],
            'tags': ['general'],
        }),
        ('b6', {
            'name': _('I have feedback/suggestions about the beta'),
            'html': 'Firefox 4 beta versions have a feedback system built in.'
                    ' For more details, see our '
                    '<a href="http://www.mozilla.com/en-US/firefox/beta/feedback/">'
                    'beta feedback page</a>.',
            'deadend': True,
        }),
        ])
    }),
    ('mobile', {
        'name': _('Firefox on Mobile (Android or Maemo systems)'),
        'extra_fields': ['ff_version', 'os', 'plugins'],
        'tags': ['mobile'],
        'categories': SortedDict([
            ('m1', {
                'name': _('Firefox for mobile is having problems with certain web sites'),
                'extra_fields': ['sites_affected'],
                'tags': ['websites'],
            }),
            ('m2', {
                'name': _("I'm having trouble with the look and feel of Firefox for mobile"),
                'articles': [
                    {'title': 'How to navigate Web pages',
                     'url': '/en-US/kb/How+to+navigate+Web+pages'},
                    {'title': 'How to open a new tab',
                     'url': '/en-US/kb/How+to+open+a+new+tab'},
                    {'title': 'How to add a bookmark',
                     'url': '/en-US/kb/How+to+add+a+bookmark'},
                    {'title': 'How to use the Location Bar ',
                     'url': '/en-US/kb/How+to+use+the+Location+Bar'},
                ],
                'tags': ['ui'],
            }),
            ('m3', {
                'name': _('Firefox for mobile is crashing or closing unexpectedly'),
                'tags': ['crash'],
            }),
            ('m4', {
                'name': _('I have a problem with an extension or plugin'),
                'extra_fields': ['addon'],
                'html': 'Most extensions or plugins are not written by Mozilla '
                        'and you will need to contact the people or company who '
                        'made the extension/plugin for support, if you need help '
                        'removing an extension or plugin, see <a '
                        'href="http://mobile.support.mozilla.com'
                        '/en-US/kb/How+to+remove+or+disable+add-ons">'
                        'How to remove or disable add-ons</a>.',
                'tags': ['addon'],
            }),
            ('m5', {
                'name': _('I have feedback/suggestions about Firefox for Mobile'),
                'html': '<p>You can provide suggestions for '
                        '<strong>Firefox on Maemo</strong> in the '
                        '<a href="http://firefoxformobile.uservoice.com/forums/70215-firefox-for-maemo-ideas">'
                        'Maemo feedback forum</a>.</p>'
                        '<p>You can provide suggestions for '
                        '<strong>Firefox on Android</strong> in the '
                        '<a href="http://firefoxformobile.uservoice.com/forums/70211-firefox-for-android-ideas">'
                        'Android feedback forum</a>.</p>',
                'deadend': True,
            }),
        ])
    }),
    ('home', {
        'name': _('Firefox Home App for iPhone'),
        'tags': ['FxHome'],
        'categories': SortedDict([
            ('i1', {
                'name': _("I'm having trouble setting up Firefox Home on my iPhone"),
                'articles': [
                    {'title': 'How to set up Firefox Home on your iPhone',
                     'url': '/en-US/kb/How+to+set+up+Firefox+Home+on+your+iPhone'},
                ],
                'tags': ['iphone'],
            }),
            ('i2', {
                'name': _("I'm having trouble setting up Firefox Sync on my Desktop Firefox"),
                'articles': [
                    {'title': 'How to sync Firefox settings between computers',
                     'url': '/en-US/kb/How+to+sync+Firefox+settings+between+computers'},
                ],
                'tags': ['desktop', 'sync'],
            }),
            ('i3', {
                'name': _('Not all my data is syncing between Firefox '
                          'and Firefox Home or I have other problems syncing'),
                'articles': [
                    {'title': 'Firefox Home does not work ',
                     'url': '/kb/Firefox+Home+does+not+work'},
                    {'title': 'Cannot log in to Firefox Home App ',
                     'url': '/kb/Cannot+log+in+to+Firefox+Home+App'},
                    {'title': 'Replace your Sync information',
                     'url': '/kb/Replace+your+Sync+information'},
                ],
                'tags': ['sync'],
            }),
            ('i4', {
                'name': _('I have feedback/suggestions about Firefox Home for iPhone'),
                'html': 'You can provide suggestions in our '
                        '<a href="http://firefoxformobile.uservoice.com/forums/67057-firefox-home-ideas">'
                        'Firefox Home feedback forum</a>.',
                'deadend': True,
            }),
        ])
    }),
    ('sync', {
        'name': _('Firefox Sync'),
        'tags': ['sync'],
        'categories': SortedDict([
            ('s1', {
                'name': _("I'm having trouble setting up Firefox Sync on my Nokia or Android device"),
                'articles': [
                    {'title': 'How to sync Firefox settings with a mobile device',
                     'url': 'http://mobile.support.mozilla.com/en-US/kb/How+to+sync+Firefox+settings+with+a+mobile+device'},
                ],
                'tags': ['mobile'],
            }),
            ('s2', {
                'name': _("I'm having trouble setting up Firefox Home on my iPhone"),
                'articles': [
                    {'title': 'How to set up Firefox Home on your iPhone',
                     'url': '/en-US/kb/How+to+set+up+Firefox+Home+on+your+iPhone'},
                ],
                'tags': ['iphone'],
            }),
            ('s3', {
                'name': _("I'm having trouble setting up Firefox Sync on my Desktop Firefox"),
                'articles': [
                    {'title': 'How to sync Firefox settings between computers',
                     'url': '/en-US/kb/How+to+sync+Firefox+settings+between+computers'},
                ],
                'tags': ['desktop'],
            }),
            ('s4', {
                'name': _('I have other problems syncing data between computers or devices'),
                'articles': [
                    {'title': 'Firefox Sync is not working',
                     'url': '/en-US/kb/Firefox+Sync+is+not+working'},
                    {'title': 'Firefox Home does not work ',
                     'url': '/kb/Firefox+Home+does+not+work'},
                    {'title': 'Cannot log in to Firefox Home App ',
                     'url': '/kb/Cannot+log+in+to+Firefox+Home+App'},
                    {'title': 'Replace your Sync information',
                     'url': '/kb/Replace+your+Sync+information'},
                ],
                'tags': ['sync'],
            }),
            ('s5', {
                'name': _('I have feedback/suggestions about Firefox Home for iPhone'),
                'html': 'You can provide suggestions in our '
                        '<a href="http://assets2.getsatisfaction.com/mozilla_labs/products/mozilla_labs_weave_sync">'
                        'Firefox Sync feedback forum</a>.',
                'deadend': True,
            }),
        ])
    }),
    ('other', {
        'name': _("Thunderbird (Mozilla's email client) or other Mozilla product"),
        'html': 'Support for Thunderbird and other Mozilla products can be found at'
                ' <a href="http://www.mozilla.org/support">Mozilla Support</a>.',
        'categories': SortedDict([]),
        'deadend': True,
    }),
])

# Insert 'key' keys so we can go from product or category back to key:
for p_k, p_v in products.iteritems():
    p_v['key'] = p_k
    for c_k, c_v in p_v['categories'].iteritems():
        c_v['key'] = c_k
