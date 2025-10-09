import scrapy


class BoerickeSpider(scrapy.Spider):
    name = "boericke"
    allowed_domains = ["materiamedica.info"]
    start_urls = [
        "https://www.materiamedica.info/en/materia-medica/william-boericke/"
    ]

    def parse(self, response):
        # Extract all medicine page links
        links = response.css("a::attr(href)").getall()

        for link in links:
            if "/william-boericke/" in link:
                full_link = response.urljoin(link)
                yield scrapy.Request(full_link, callback=self.parse_medicine)

    def parse_medicine(self, response):
        # Extract the medicine name (last part of the URL, capitalized)
        medicine_name = response.url.split("/")[-1].replace("-", " ").title()

        # Extract all <p> tag text and join them into a single string
        paragraphs = response.css("p::text").getall()
        content = " ".join(p.strip() for p in paragraphs if p.strip())

        # Save as key-value format
        yield {medicine_name: content}
