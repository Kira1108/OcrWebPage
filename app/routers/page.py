from fastapi import APIRouter
from .image import ocr_parser
from .text import text_parser
from pydantic import BaseModel
from typing import List,Optional
from app.db import db
import json
from urllib.parse import quote
import logging
import glob
import os
import base64

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)



router = APIRouter(
    prefix="/page",
    tags=["page"],
    responses={404: {"description": "Not found"}},
)

class UrlInfo(BaseModel):
    id:str
    text:List[str]
    paths:List[str]

def encode_base64(message):
    message_bytes = message.encode('utf-8')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('utf-8')
    return base64_message


def _parse(urlInfo):

    try:

        img_results = []
        for path in urlInfo.paths:

            logger.info('Detecting image' + path)

            try:
                image_result = ocr_parser.parse(path)
                status = 'success'
            except:
                image_result = dict()
                status = 'failed'

            image_result= {
                "path":path,
                "is_contain":any(image_result.values()),
                "detail":image_result,
                "status": status
            }

            img_results.append(image_result)


        logger.info("Detecting text")
        text_result = text_parser.parse(urlInfo.text)
        logger.info('Text detection done')

        return {
            "id":urlInfo.id,
            "code":1,
            'img_result':img_results,
            "text_result":{
                "is_contain":any(text_result.values()),
                "detail":text_result
            }
        }

    except:
        return {
            "id":urlInfo.id,
            "code":0
        }



@router.post("/img_paths")
async def parse_page(urlInfo:UrlInfo):
    result = _parse(urlInfo)
    logger.info('Writing Result to DataBase')

    try:
        sql = "update URL set url_result = '{}' where id = '{}'".format(json.dumps(result, ensure_ascii=False), urlInfo.id)
        db.execute(sql)
    except Exception as e:
        logger.Error("Error Writing DataBase")
        logger.Error(e)
    return result


class UrlFolderInfo(BaseModel):
    id:str
    text:List[str]
    path:str


def _parse_folder(UrlFolderInfo):

    try:

        img_results = []
        for path in glob.glob(os.path.join(UrlFolderInfo.path, "*")):

            logger.info('Detecting image' + path)

            try:
                image_result = ocr_parser.parse(path)
                status = 'success'
            except:
                image_result = dict()
                status = 'failed'

            image_result= {
                "path":path,
                "is_contain":any(image_result.values()),
                "detail":image_result,
                "status": status
            }

            img_results.append(image_result)


        logger.info("Detecting text")
        text_result = text_parser.parse(UrlFolderInfo.text)
        logger.info('Text detection done')

        try:
            img_overall= any([r['is_contain'] for r in img_results])
            text_overall = any(text_result.values())
            contain_sensitive = img_overall or text_overall
        except:
            logger.error("overall info error")

        return {
            "id":UrlFolderInfo.id,
            "code":1,
            "contain_sensitive":contain_sensitive,
            'img_result':img_results,
            "text_result":{
                "is_contain":any(text_result.values()),
                "detail":text_result
            }
        }

    except:
        return {
            "id":UrlFolderInfo.id,
            "code":0
        }

@router.post("/")
async def parse_page_folder(urlFolderInfo:UrlFolderInfo):
    result = _parse_folder(urlFolderInfo)
    logger.info('Writing Result to DataBase')

    try:
        message = encode_base64(json.dumps(result, ensure_ascii=False))
        sql = "update URL set url_result = '{}' where id = '{}'".format(message, urlFolderInfo.id)
        db.execute(sql)
    except Exception as e:
        logger.error("Error Writing DataBase")
        logger.error(e)
    return result
