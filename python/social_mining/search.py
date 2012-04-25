import twitter
import nltk

def public(query, results_per_page, n_pages):
    """
    Shorthand for the public Twitter search
    It returns the full result object and the last item's id
    """
    t = twitter.Twitter(domain="search.twitter.com")
    results = []
    for page in xrange(1, n_pages):
        results.append(t.search(q=query, rpp=results_per_page, page=page))
    return results, results[0]['results'][0]['id']

def freq(result):
    """
    Produces a nltk FreqDist from a public result
    """
    words = []
    for page in result:
        for elem in page['results']:
            words += [w for w in elem['text'].split()]
    return nltk.FreqDist(words)
