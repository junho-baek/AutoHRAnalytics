from fastapi import FastAPI, HTTPException
from notion_client import Client
from dotenv import load_dotenv
import os
from typing import Dict, List, Any, Optional

# 환경변수 로드
load_dotenv()

app = FastAPI()

# Notion 클라이언트 초기화
notion = Client(
    auth=os.getenv("NOTION_TOKEN"),
    version=os.getenv("NOTION_VERSION")
)

@app.get("/databases/{database_id}")
async def get_database(database_id: str) -> Dict[str, Any]:
    """데이터베이스 메타데이터 조회"""
    try:
        return notion.databases.retrieve(database_id=database_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/databases/{database_id}/query")
async def query_database(
    database_id: str,
    page_size: Optional[int] = 100,
    start_cursor: Optional[str] = None
) -> Dict[str, Any]:
    """데이터베이스 내용 조회"""
    try:
        return notion.databases.query(
            database_id=database_id,
            page_size=page_size,
            start_cursor=start_cursor
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) 