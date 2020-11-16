# scrapy_web_site_info

A command-line application that, given a list of website URLs as input, visits them
and finds, extracts and outputs the websites’ logo image URLs and all phone numbers (e.g.
mobile phones, land lines, fax numbers) present on the websites.

### Prerequisites

* [DOCKER](https://docs.docker.com/get-docker/)

## Running

```
$ docker build -t scrapy_web_site_info:0.0.1 -f ./Dockerfile
$ cat ./websites.txt | docker run -i scrapy_web_site_info:0.0.1
```