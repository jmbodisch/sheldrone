import unittest
import display

class TestGetEmbed(unittest.TestCase):
    replay = {
        'replayCode': 'AAAAAAAAAAAAAAAA',
        'historyDetail': {
        "vsMode": {
            "mode": "PRIVATE",
            "name": "Private Battle",
            "id": "VnNNb2RlLTU="
        },
        "leagueMatch": None,
        "vsRule": {
            "name": "Rainmaker",
            "id": "VnNSdWxlLTM="
        },
        "vsStage": {
            "name": "Humpback Pump Track",
            "id": "VnNTdGFnZS0xNw=="
        },
        "playedTime": "2024-07-25T01:19:45Z",
        "judgement": "LOSE",
        "player": {
            "weapon": {
            "name": "Inkbrush",
            "image": {
                "url": "https://api.lp1.av5ja.srv.nintendo.net/resources/prod/v2/weapon_illust/260428edbf919f5c9e8c8517516d6a7a8133cf7348d216768ab4fb9434053f08_1.png?Expires=1736467200&Signature=P6CalGbtkpUYBPaar0UTL1kRZvkvIXxfBohiV7pjvX5rK9ysZMHeSOTXYMBcLGgKvgdTJL6XyPMI0bvJNA1oREiuX3oB2imCxE7A9mRNrhqxVVYY93K2K7si2H~sPNNb0ngtp352-gRMFPMlTsGM-flb87R1qtr~mryUR6DaHzIe-Z7kVKjYQAWHFWol2saDlwQMhInKu8s3zdncZHTzMZF5DG9SXBnjB5eVcWU8Mr1LgEhLDnldvliH05IlK06vE6alNf2vhRcVIkpO768CS27J1-zXYB-NiLgWsIgtSMgj-W7Hx5ISV8ss~rrJwZDwEPR~K7iHv-~-7lSnkIyrDQ__&Key-Pair-Id=KNBS2THMRC385"
            },
            "id": "V2VhcG9uLTExMDA="
            },
            "festGrade": None,
            "id": "VnNQbGF5ZXItdS1hY2UyNXpkYXhpYXF0dXd2bG5tbTo6MjAyNDA3MjVUMDExNDE1X2NlNmMwNTY3LWNjOTQtNDQzMS1iMjE3LWM0MDljODRlYjk3YTp1LWFjZTI1emRheGlhcXR1d3Zsbm1t",
            "__isPlayer": "VsPlayer",
            "byname": "Evil Inkbrush User",
            "name": "Ж∵Damp",
            "nameId": "3848",
            "nameplate": {
            "badges": [
                {
                "image": {
                    "url": "https://api.lp1.av5ja.srv.nintendo.net/resources/prod/v2/badge_img/128247ad283ff01141e9f98597f5b4e91c7d2a7263e5a4cc017074207fb0ca06_0.png?Expires=1736467200&Signature=LrQm28K~wuWQ~ImDsNEGRCVALgAkyLcOjp6jjb2Ery7iTYx0vnV~jeysEEAriKd~VJkxZ7RtoPYNPQMOyTHyQjG-tX97y0-Eu8wA8gubtOfnGtXcLEyDwjYb-ozGxmwbhpcL3lukn0ieCAMOEY~2OiRVSPmoLtfZm40qFoern29c~XLfeBFIzsHTDI7Xlxim~pySmwzgWEl1z5gV-Qv8afoIETHcxPgKHMOYgzMjfOnMXM8wwrR-IWSpKHV88t-K5pKemwrneyud8g9QuoXM8QM3xcVPKJB2J4rI9iiDcxKpob4aMGP2n22odr7YQ5oOzrUTMXUSo2roZNvub9Q8lQ__&Key-Pair-Id=KNBS2THMRC385"
                },
                "id": "QmFkZ2UtNTIxMTAwMA=="
                },
                {
                "image": {
                    "url": "https://api.lp1.av5ja.srv.nintendo.net/resources/prod/v2/badge_img/f6107863de8324b72a37e8ab66a461458f2853d9fdce617bef473d85f555ac2d_0.png?Expires=1736467200&Signature=JHkBAnldzir80UlOplbyPaMq1gWZa8TsR1LB1MixAYLllNf2RlDT~EQXE2zNgqikULT9W604cuS34g2gGND6Guy7ZFRRxX8LfSWvyI6Xa0QXF5CP28i3A8nfJi3mxXXTLbWWaXg1ZxMyEyQIbB7oTdJdl70qvEWFETTTpAS1S~4XGqqm1~Ib4F5XVxIykAF-OdpG3B6VuC~ID1yhdg2yOPW60sOYLLqX2ctr1LC4ewb7h7C7Bfd1N2n0~5A-iwmZGRGh1k3r8neEopkXeCw-jj5Jgm0kqWh9djp0mbf81Qug8ATgeYbsAiggsGo9s1y5Zxtnul0B3Fa6nk1d8D1Gyw__&Key-Pair-Id=KNBS2THMRC385"
                },
                "id": "QmFkZ2UtMzEwMTAwMQ=="
                },
                {
                "image": {
                    "url": "https://api.lp1.av5ja.srv.nintendo.net/resources/prod/v2/badge_img/0a3d58a31c26959608fa3352cadf2d53cfb9fd001d17e32a019d1496748ce86f_0.png?Expires=1736467200&Signature=mfJW6S8GhrR3FDAizu5gkceX2O1oNUhMaZPPAO5gncxQaL4Xs4759vBFoTmeWgaT8mDo4BCHys8rircO352fyBwJOVDPrf37DY12m371gxixRJ8Phr5wue1fSVUnQAxa7sC8U2kr6JM5a0xrhnDXRa-ufGXvgicb8iBlPXTcr-wOn-cKIUghLUx6sLlRi9du~iWFK5Dc3E980LRn8aWE2GGZDUXVJtRY0m~zaF8kq5WZzjahCI6vExD8YwmzpmO8vo7gRinI1CZAekin~CdYHzeq-7YBQWYAJv4~W1kb3neU2RnW-heA1ZKu5tiOIgeRKTB6bjeI3Jx~dieD8ZyHyA__&Key-Pair-Id=KNBS2THMRC385"
                },
                "id": "QmFkZ2UtNDAwMDIwMQ=="
                }
            ],
            "background": {
                "textColor": {
                "a": 1,
                "b": 1,
                "g": 1,
                "r": 1
                },
                "image": {
                "url": "https://api.lp1.av5ja.srv.nintendo.net/resources/prod/v2/npl_img/ea655fb5842bbaae6d1f9d7bfa1b1f849496a929dbfd8086c1b13314609d8487_0.png?Expires=1736467200&Signature=DIJWfouTuHKiFARwBdyfLPZT7fvhrrvYQZdg8cicbJ-ScBhYDWjh7~UurdfNQLJ1zk5Id-fARM9ZhY~tswgiwqV9VKs7QCGYdEfIk~iwc1d6kt6AtkQ7UVH6nbLJ7FCQoofSod~ru6QUu~hh6LNCjL~BozWd0PpG6DYD1TsHxU6TPbzYhGPxc9-uc9OH4SLxLb7-AKU4aizc0LU84YMyVIKGa-N-TJEJ3ewTW-tYBWF4VvJIEWX6KMZOlEID2VtNCfxDuysrY7ZvYuoadFa8rlrZ6XyefH8d5M5tpduu3rnrmw0f4iM~j33qUSbvG53pvDAgqksWDdt1pzii18s5Dg__&Key-Pair-Id=KNBS2THMRC385"
                },
                "id": "TmFtZXBsYXRlQmFja2dyb3VuZC0yMDA1"
            }
            },
            "headGear": {
            "name": "Wharfside Cap",
            "image": {
                "url": "https://api.lp1.av5ja.srv.nintendo.net/resources/prod/v2/gear_img/bd1412ae26456c34eff53202c8238ea63b01f0c52b29d0947e6561107cae2414_1.png?Expires=1736467200&Signature=S~aXMaZq-3Jz6RZgGYBN1Dh5uHk~EHB-AGrq105JaspNMKDbDLaJ1ZJBfhTRDur3zm-5mVI43Hs9R6c-H0vRzoHDQpAfixYOAtnqGFcSmmtP~dnYulYmd9i32dcAfqEQoV07gWFyzreFv4BD84UztefXAGnM90B8sVQNxLsAaYFJ3xCwjsFcUxouTxSM9Zcf43AsZTUUOzOJV5THxay~CAn9Cr-WB-GsG7LdzdEwmago2G26sKYdzVvIhV4SWWkoxYCeYn~-RgwO9W9iYddD4ay8xJe4txVcrMj69-uWfgpOl49uPJRL2R0Tb~NOHFvbQ1sicyr88JqFbnXD-6MGpg__&Key-Pair-Id=KNBS2THMRC385"
            },
            "__isGear": "HeadGear",
            "primaryGearPower": {
                "name": "Quick Respawn",
                "image": {
                "url": "https://api.lp1.av5ja.srv.nintendo.net/resources/prod/v2/skill_img/aaa9b7e95a61bfd869aaa9beb836c74f9b8d4e5d4186768a27d6e443c64f33ce_0.png?Expires=1736467200&Signature=U~D47ucDbTjJGZC24NH0IfFcwkTI~neFJV-Hjv4xDNFpEhgB80HUQjVZN33ZiFTJOJf-YbGbStL4Nx6Xu9-BIyH2C4EprutGBBp06kJXrBBalizsp3YhUY9NuBerg3uJlXulwNJGfURZmVZNPA6my8pIvoED6C3g8dxbD54nOGfUHXQGZeTVGjr-3tZDh209tzO~7jn2K8fxL5aTrrDzx19E6-s3gHVdog9URYZ1R0vHFgK3C4jZq3voCnr4wNcwgI9NzJwHrCqoHf~ZNfylThiJ0~LRnp4n88CyNF0tnRqtWvlNa41dkbzYKPDXe0ihyO5hNMH0JmHvtNkFVFVMvA__&Key-Pair-Id=KNBS2THMRC385"
                }
            },
            "additionalGearPowers": [
                {
                "name": "Quick Respawn",
                "image": {
                    "url": "https://api.lp1.av5ja.srv.nintendo.net/resources/prod/v2/skill_img/aaa9b7e95a61bfd869aaa9beb836c74f9b8d4e5d4186768a27d6e443c64f33ce_0.png?Expires=1736467200&Signature=U~D47ucDbTjJGZC24NH0IfFcwkTI~neFJV-Hjv4xDNFpEhgB80HUQjVZN33ZiFTJOJf-YbGbStL4Nx6Xu9-BIyH2C4EprutGBBp06kJXrBBalizsp3YhUY9NuBerg3uJlXulwNJGfURZmVZNPA6my8pIvoED6C3g8dxbD54nOGfUHXQGZeTVGjr-3tZDh209tzO~7jn2K8fxL5aTrrDzx19E6-s3gHVdog9URYZ1R0vHFgK3C4jZq3voCnr4wNcwgI9NzJwHrCqoHf~ZNfylThiJ0~LRnp4n88CyNF0tnRqtWvlNa41dkbzYKPDXe0ihyO5hNMH0JmHvtNkFVFVMvA__&Key-Pair-Id=KNBS2THMRC385"
                }
                },
                {
                "name": "Quick Respawn",
                "image": {
                    "url": "https://api.lp1.av5ja.srv.nintendo.net/resources/prod/v2/skill_img/aaa9b7e95a61bfd869aaa9beb836c74f9b8d4e5d4186768a27d6e443c64f33ce_0.png?Expires=1736467200&Signature=U~D47ucDbTjJGZC24NH0IfFcwkTI~neFJV-Hjv4xDNFpEhgB80HUQjVZN33ZiFTJOJf-YbGbStL4Nx6Xu9-BIyH2C4EprutGBBp06kJXrBBalizsp3YhUY9NuBerg3uJlXulwNJGfURZmVZNPA6my8pIvoED6C3g8dxbD54nOGfUHXQGZeTVGjr-3tZDh209tzO~7jn2K8fxL5aTrrDzx19E6-s3gHVdog9URYZ1R0vHFgK3C4jZq3voCnr4wNcwgI9NzJwHrCqoHf~ZNfylThiJ0~LRnp4n88CyNF0tnRqtWvlNa41dkbzYKPDXe0ihyO5hNMH0JmHvtNkFVFVMvA__&Key-Pair-Id=KNBS2THMRC385"
                }
                },
                {
                "name": "Quick Respawn",
                "image": {
                    "url": "https://api.lp1.av5ja.srv.nintendo.net/resources/prod/v2/skill_img/aaa9b7e95a61bfd869aaa9beb836c74f9b8d4e5d4186768a27d6e443c64f33ce_0.png?Expires=1736467200&Signature=U~D47ucDbTjJGZC24NH0IfFcwkTI~neFJV-Hjv4xDNFpEhgB80HUQjVZN33ZiFTJOJf-YbGbStL4Nx6Xu9-BIyH2C4EprutGBBp06kJXrBBalizsp3YhUY9NuBerg3uJlXulwNJGfURZmVZNPA6my8pIvoED6C3g8dxbD54nOGfUHXQGZeTVGjr-3tZDh209tzO~7jn2K8fxL5aTrrDzx19E6-s3gHVdog9URYZ1R0vHFgK3C4jZq3voCnr4wNcwgI9NzJwHrCqoHf~ZNfylThiJ0~LRnp4n88CyNF0tnRqtWvlNa41dkbzYKPDXe0ihyO5hNMH0JmHvtNkFVFVMvA__&Key-Pair-Id=KNBS2THMRC385"
                }
                }
            ]
            },
            "clothingGear": {
            "name": "Dustcloud Hoodie",
            "image": {
                "url": "https://api.lp1.av5ja.srv.nintendo.net/resources/prod/v2/gear_img/98b7ecdadc047770c10a39b6972b4138055a3e9d4ca48a65bfe74ff4fa0a3caf_1.png?Expires=1736467200&Signature=sBGdHGHAI8QoCx~BEKL4X4d-PqwPbUwVEd6HJe-7mi3gjK-j~yK-qcvfVqrYR3nQTZJLYuh2USsDl2txiCrQgmYqSBKNycZaMiUKX3Ny97ZZn50v6oo7-JVpFf7iEyQceTMoLAebJ~STPw1SUVRm7I-lqDqFJwxabEA9weBXTBXo0wGLo59mVf-9DutGvluc19Nak9o6JUoswvj0C0E8ur2QwjBU42UPrz5X3-DzFtAnRxV-hXAN6YbnP6t84VAAciPl78UJ-6Xv5MPiWn1pSYg14tePHVVNV3wUMQN79eV683XKq6Po5yoSFevW6LGTq8Aiqj2GiiBQrSOmL5vcNw__&Key-Pair-Id=KNBS2THMRC385"
            },
            "__isGear": "ClothingGear",
            "primaryGearPower": {
                "name": "Ninja Squid",
                "image": {
                "url": "https://api.lp1.av5ja.srv.nintendo.net/resources/prod/v2/skill_img/2c0ef71abfb3efe0e67ab981fc9cd46efddcaf93e6e20da96980079f8509d05d_0.png?Expires=1736467200&Signature=FuTz~i9CY8AJB362XhP2W62PUeaKrbrrQ2m5sg~OHPhZvfQhc0EC2FWwo0Qaa0xyrGgK66q5gn0FeaFeQEUlC1yRHFlhyON2PUsKs5ehjVlaBpMb-JO3qO0cYXU7rvjWSjj9YNDXvcKbKkW3gUtQiWf-SOKMq-WXwKlwBT3LVrUh-M2CkXga3zjYYRdPr7LLaDGGrHd89G7zUCViVbABqbz2CvqcptxYFhEXxqGuRsKLRt5N0u9dFIJO~ZUnALxj6cOp3bRel4XzehmE2KsMI1LDulqzg3SZCZKf1K4dLn3HyHg265Kg2o5kx0szaopCYyl9e5jukvuLHxF9iV-mOg__&Key-Pair-Id=KNBS2THMRC385"
                }
            },
            "additionalGearPowers": [
                {
                "name": "Swim Speed Up",
                "image": {
                    "url": "https://api.lp1.av5ja.srv.nintendo.net/resources/prod/v2/skill_img/087ffffe40c28a40a39dc4a577c235f4cc375540c79dfa8ede1d8b63a063f261_0.png?Expires=1736467200&Signature=V1bmdvjjf6CqvFXvyHKirD-~J0KZGVofB87s2kUfZS9KYxuOpBxvGrSMr~B8SdF0fqn3PLpRnmF0dk0PnzKowB1AuQlH5JIsrMt~aTINeunVvzgsXjFE20r9xoxXYM7sKTTsyn-DElb8F2fAc1YYlU8P6iyeQaCI1E1E8V7grpIHd4f10ZVw4CllJVUQyom8mwxdF55Y0A1AgI8Wcly8jVkezyzr8viNm-QShQm5RJSlCPvqtDrxdiub3R~HkmRTQ4qIrY9GRBD4DvfF-bHDVJF8APcKhFgb2aXM-Ga2JJ8nzgUQmeEkj70TZGKhB7lmColQW3GmzKueGvejBsu-XQ__&Key-Pair-Id=KNBS2THMRC385"
                }
                },
                {
                "name": "Quick Super Jump",
                "image": {
                    "url": "https://api.lp1.av5ja.srv.nintendo.net/resources/prod/v2/skill_img/138820ed46d68bdf2d7a21fb3f74621d8fc8c2a7cb6abe8d7c1a3d7c465108a7_0.png?Expires=1736467200&Signature=mJtBRjRaStqy0fiRcjdti6SUTPrBndLpXhWsKDOUhifgrUXMTF9vng0taKomZRpX9qtG~sa~O11Oo1tLL~hda7zzV9vi6vkXWn3S8yPZaomAKcdD6DZddohwKA~VjWJi5TNK2I3KRVB4BetDuyata6bwCN~98uXleOp3GDXgKAPhn9foKj29ZR3oF0JTaqmZ8rHa6gWjawP8MtN7x1aiCvihj1plm3RIZKC0RAVWR2ZHdSbz65zR9~w0dER40598d2h1NHCgztSglwkNAUMbTA0SgrfpP2Gyep9HYRYW84qkoZMbGPWAraUjwgimTaAA-ZhwxdNDzXNP4~Sbf1uhbQ__&Key-Pair-Id=KNBS2THMRC385"
                }
                },
                {
                "name": "Quick Super Jump",
                "image": {
                    "url": "https://api.lp1.av5ja.srv.nintendo.net/resources/prod/v2/skill_img/138820ed46d68bdf2d7a21fb3f74621d8fc8c2a7cb6abe8d7c1a3d7c465108a7_0.png?Expires=1736467200&Signature=mJtBRjRaStqy0fiRcjdti6SUTPrBndLpXhWsKDOUhifgrUXMTF9vng0taKomZRpX9qtG~sa~O11Oo1tLL~hda7zzV9vi6vkXWn3S8yPZaomAKcdD6DZddohwKA~VjWJi5TNK2I3KRVB4BetDuyata6bwCN~98uXleOp3GDXgKAPhn9foKj29ZR3oF0JTaqmZ8rHa6gWjawP8MtN7x1aiCvihj1plm3RIZKC0RAVWR2ZHdSbz65zR9~w0dER40598d2h1NHCgztSglwkNAUMbTA0SgrfpP2Gyep9HYRYW84qkoZMbGPWAraUjwgimTaAA-ZhwxdNDzXNP4~Sbf1uhbQ__&Key-Pair-Id=KNBS2THMRC385"
                }
                }
            ]
            },
            "shoesGear": {
            "name": "Trifecta Sandals",
            "image": {
                "url": "https://api.lp1.av5ja.srv.nintendo.net/resources/prod/v2/gear_img/b91d5d1df8b187c249f4e333a1fe7e1b06d9ba9121aca27cde1e4db016ec4ff2_1.png?Expires=1736467200&Signature=m2Xd5wEBOZ8yuJ8CghDLl3IB5sHWL0n6Netja7Oz9SFrHwlPeyMdSTUBMKGXydYqijISFLfpPrZyYjAToPCDVQLhXZwN3BMsR~2PPkzaqVC6UGNd8-q9vOLO7pJBokVFoJmuhagUo4UQy348SWfg3ELpHUFTdcBHxLOlgc4jK1vQ-Vu4zNjl0q8m06Q14WFAguLzS8EGv07ycOeE~WCqSY0~Yvhu~Kd~TxNq4bOZsDqT-pPF28-UKulrHBHWKzlolOrlh4h30IT7fZ6cjafTDvCxKwkI92yEB6Nh-Qdgmc-1VB~l63Kzk-UarOHcX858RRkKMqPe9F1JQe0q6rUdzQ__&Key-Pair-Id=KNBS2THMRC385"
            },
            "__isGear": "ShoesGear",
            "primaryGearPower": {
                "name": "Stealth Jump",
                "image": {
                "url": "https://api.lp1.av5ja.srv.nintendo.net/resources/prod/v2/skill_img/f9c21eacf6dbc1d06edbe498962f8ed766ab43cb1d63806f3731bf57411ae7b6_0.png?Expires=1736467200&Signature=sJie3bTBg-5fhARN2Vasip~80A4oClSglwFjxhUf0pdtegoG3M1j1DB5w~Kquz5DCimtqCDBMlEq7GTZ2tR0Hg~3pn2OrrTWFHlaX2kQkebAYv7qPEIQSIn3nTzqZmO3HBuWYAve3BvVwDj-7a8CiKW1obQyS7uDHq3uHQ-bCciGBDy8cNBVOWuoqhp0XTKpAm~T7RQX2pcovwaEFLLenNMWLk79HM65Zzdo08Sd4CPTtMTUn6fHPufhbB10lGLKtpqfMXoyGgOMeLrf1sKiH~ZKBmY42oAj2Vo7XQqB~gph~4bOAtDYuU~v~rIjWIx1sRVFaJ9-Nk1nAdpSEy5K8w__&Key-Pair-Id=KNBS2THMRC385"
                }
            },
            "additionalGearPowers": [
                {
                "name": "Quick Respawn",
                "image": {
                    "url": "https://api.lp1.av5ja.srv.nintendo.net/resources/prod/v2/skill_img/aaa9b7e95a61bfd869aaa9beb836c74f9b8d4e5d4186768a27d6e443c64f33ce_0.png?Expires=1736467200&Signature=U~D47ucDbTjJGZC24NH0IfFcwkTI~neFJV-Hjv4xDNFpEhgB80HUQjVZN33ZiFTJOJf-YbGbStL4Nx6Xu9-BIyH2C4EprutGBBp06kJXrBBalizsp3YhUY9NuBerg3uJlXulwNJGfURZmVZNPA6my8pIvoED6C3g8dxbD54nOGfUHXQGZeTVGjr-3tZDh209tzO~7jn2K8fxL5aTrrDzx19E6-s3gHVdog9URYZ1R0vHFgK3C4jZq3voCnr4wNcwgI9NzJwHrCqoHf~ZNfylThiJ0~LRnp4n88CyNF0tnRqtWvlNa41dkbzYKPDXe0ihyO5hNMH0JmHvtNkFVFVMvA__&Key-Pair-Id=KNBS2THMRC385"
                }
                },
                {
                "name": "Swim Speed Up",
                "image": {
                    "url": "https://api.lp1.av5ja.srv.nintendo.net/resources/prod/v2/skill_img/087ffffe40c28a40a39dc4a577c235f4cc375540c79dfa8ede1d8b63a063f261_0.png?Expires=1736467200&Signature=V1bmdvjjf6CqvFXvyHKirD-~J0KZGVofB87s2kUfZS9KYxuOpBxvGrSMr~B8SdF0fqn3PLpRnmF0dk0PnzKowB1AuQlH5JIsrMt~aTINeunVvzgsXjFE20r9xoxXYM7sKTTsyn-DElb8F2fAc1YYlU8P6iyeQaCI1E1E8V7grpIHd4f10ZVw4CllJVUQyom8mwxdF55Y0A1AgI8Wcly8jVkezyzr8viNm-QShQm5RJSlCPvqtDrxdiub3R~HkmRTQ4qIrY9GRBD4DvfF-bHDVJF8APcKhFgb2aXM-Ga2JJ8nzgUQmeEkj70TZGKhB7lmColQW3GmzKueGvejBsu-XQ__&Key-Pair-Id=KNBS2THMRC385"
                }
                },
                {
                "name": "Sub Resistance Up",
                "image": {
                    "url": "https://api.lp1.av5ja.srv.nintendo.net/resources/prod/v2/skill_img/664489b24e668ef1937bfc9a80a8cf9cf4927b1e16481fa48e7faee42122996d_0.png?Expires=1736467200&Signature=NK-Nvkm0Z3TEiGd-RPecoRopUNAixTmSLyQ~msM7J6qmZGs2nMh6B4~1fJGQm5BkXHOFoHSmTOkE3-NGkyim-oKih4Nygd7qLtQvio7g2PFPPB8W1znqyNG1Xv46bpWpCDtf9dlx2cMfWIoq5lC~n5sFnoeGzL9cRhC7Td0JS6oHgD2kX~uFVPss0mnJwwjJc~5-Dw2BYrYidt0~zsMMwU2ALw85Z~ExLMuPxvXdhH7vzi0TDiOtgm23Q-jx1pkz-yB45TZnoMjoNyIXXJMcAJzeEqRIc1Y8IS3G7Og2eG7ZXIIGejQzlLebLZ7z2AoJTWXR-Wvp8HD2vXykRyKBoQ__&Key-Pair-Id=KNBS2THMRC385"
                }
                }
            ]
            }
        },
        "knockout": "NEITHER",
        "myTeam": {
            "result": {
            "paintPoint": None,
            "score": 17
            }
        },
        "id": "VnNIaXN0b3J5RGV0YWlsLXUtYWNlMjV6ZGF4aWFxdHV3dmxubW06OjIwMjQwNzI1VDAxMTQxNV9jZTZjMDU2Ny1jYzk0LTQ0MzEtYjIxNy1jNDA5Yzg0ZWI5N2E=",
        "awards": [
            {
            "name": "#1 Ground Traveler"
            },
            {
            "name": "#1 Damage Taker"
            },
            {
            "name": "#1 Ink Consumer"
            }
        ]
        }
    }
    def test_get_embed_happy_path(self):
        result = display.genEmbed(self.replay, ('a', 'a'))
        assert result is not None