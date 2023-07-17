import scrapy


class SteamSpider(scrapy.Spider):
    name = 'steam_spider'

    url = 'https://store.steampowered.com/search/?category1=998&filter=topsellers&ndl=1&page=%s'
    page = 1
    start_urls = [url % page]

    parsed_games = 0

    def parse(self, response, **kwargs):
        games = response.css('#search_resultsRows a::attr(href)')
        for game in games:
            yield response.follow(game, callback=self.parse_tags, cookies={'birthtime': '943981201'})

        if self.parsed_games < 1000:
            self.page += 1
            yield response.follow(self.url % self.page, callback=self.parse)

    def parse_tags(self, response):
        if self.parsed_games == 1000:
            return

        self.parsed_games += 1

        yield {
            'appName': response.css('#appHubAppName::text').get(),
            'link': response.url.split('/?')[0],
            'tags': list(map(str.strip, response.css('a.app_tag::text').getall()))
        }
