import urllib, json

def results(fields, original_query):
    search_specs = [
        ["search imgur", "~imgur", "http://m.imgur.com/search/"],
        ["searchimgur", "~imgur", "http://m.imgur.com/search/"],
        ["imgur", "~imgur", "http://m.imgur.com/search/"]
    ]
    for name, key, url in search_specs:
        if key in fields:
            search_url = url + urllib.quote_plus(fields[key])
            return {
                "title": "Search {0} for '{1}'".format(name, fields[key]),
                "run_args": [search_url],
                "html": """
                <script>
                setTimeout(function() {
                    window.location = %s
                }, 500);
                </script>
                """%json.dumps(search_url),
                "webview_user_agent": "Mozilla/5.0 (Linux; Android 4.4; Nexus 5 Build/_BuildID_) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Safari/537.36",
                "webview_links_open_in_browser": True
            }

def run(url):
    import os
    os.system('open "{0}"'.format(url))