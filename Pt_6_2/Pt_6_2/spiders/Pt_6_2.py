import scrapy


class SteamSpider(scrapy.Spider):
    name = 'steam_spider'
    url = 'https://store.steampowered.com/search/?category1=998&filter=topsellers&ndl=1&page=%s'
    page = 1
    start_urls = [url % page]
    parsed_games = 0

    def parse(self, response, **kwargs):
        games = response.css('a.search_result_row.ds_collapse_flag')
        for game in games:
            yield response.follow(game, callback=self.parse_tags, cookies={'birthtime': '943981201'})

        if self.parsed_games < 1000:
            self.page += 1
            yield response.follow(self.url % self.page, callback=self.parse)

    def parse_tags(self, response):
        if self.parsed_games < 1000:
            yield {
                'name': response.css("div.apphub_AppName::text").get(),
                'url': response.url,
                'tags': [tag.css("a::text").get().strip() for tag in response.css("a.app_tag")]
            }
        else:
            return
        self.parsed_games += 1
