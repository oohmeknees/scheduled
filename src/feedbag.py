# import urllib3 as ul
# import re
# import datetime as dt
# from docxtpl import DocxTemplate
# from envelopes import Envelope, GMailSMTP
import asyncio
import logging

import aiofiles
import aiohttp
import pandas as pd

logging.basicConfig(level=logging.INFO)


def feeds(data: str, year: str):
    logging.info("starting main")
    f = pd.read_excel(data)
    f = f[f["Year"].isin([year, "All"])]
    f = f.drop(columns=["Year", "Authentication"])
    f["Name"] = "data/" + f["Name"].astype(str) + ".json"  # where to save the data
    f = dict(zip(f["Feed"], f["Name"]))
    logging.info("starting feeds")
    return f


async def download_file(url, filename):
    logging.info(f"downloading {url}")
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            async with aiofiles.open(filename, "wb") as file:
                await file.write(await response.read())
            r = f"Downloaded {filename}"
            logging.info(r)
            return r


urls = feeds("/home/john/projects/scheduled/tests/data/feeds.xlsx", "Y13")


async def download_all():
    logging.info(f"downloading {urls}")
    tasks = [download_file(url, filename) for url, filename in urls.items()]
    await asyncio.gather(*tasks)
    r = f"downloaded {urls}"
    logging.info(r)
    return r


def main():
    logging.info("starting main")
    asyncio.run(download_all())

    # read live feeds from spreadsheet
    # asyncio.run(download_all())
    # data = pd.read_json("data/Student Metadata.json")
    # print(data.head(10))
    # read CTL narrative
    # read documents / pdf folder
    # read map of subject name
    # read map of grade values

    # fetch reports
    # fetch Tracking Student Data
    # fetch Student Courses
    # fetch Tracking UCAS
    # fetch Tracking TRGT
    # fetch Tracking PRED
    # fetch Tracking CURR
    # fetch Tracking MOCK
    # fetch Tracking CtL
    # fetch Lesson Timetable
    # fetch Staff Emails
    # warn if the TRGT PRED CURR CtL MOCK and UCAS titles match

    # calculate Average KS2 per student
    # calculate average achievement for Year group
    # calculate average Pastoral for Year group
    # calculate average Lates for Year group
    # calculate average Phone for Year group
    # calculate average Curriculum for Year group
    # calculate average Homework for Year group
    # calculate average Detentions for Year group
    # calculate grades values

    # calculate the mode of CTL grades
    # calculate the appropriate narrative for the CTL mode

    # create the list of classes
    # calculate the subject codes

    # for each grades dataset
    # unpivot the grades
    # map the headings to the subject codes
    # merge into student data

    # reduce lesson timetable to unique class and staff
    # keep only first instance of staff for each class
    # merge in the staff emails

    # merge staff emails into student data

    # repeat fetches for previous grades

    # warn if PRED < CURR
    # calculate difference between PRED and TRGT
    # # warn if TRGT < PRED
    # warn if current tracking grade < previous tracking grade

    # calculate mean CTL value for each class
    # calculate mode for CTL for each class
    # calculate mean PRED value for each class
    # calculate mean TRGT value for each class
    # calculate mean difference between PRED and TRGT

    # create spreadsheet for class summaries
    logging.info("ending main")


if __name__ == "__main__":
    main()
