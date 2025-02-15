from notion_client import Client
import os
from dotenv import load_dotenv
from typing import Dict, Any

load_dotenv()
notion = Client(auth=os.getenv("NOTION_TOKEN"))

# 페이지 ID 직원 정보
page_id = "19bbab2ed2b180f3a3f1000cd54e4364"

# 페이지 내의 블록 조회
blocks = notion.blocks.children.list(block_id=page_id)

print("\n=== 페이지 내 데이터베이스 찾기 ===")
for block in blocks["results"]:
    if block["type"] == "child_database":
        database_id = block["id"]
        print(f"데이터베이스 ID: {database_id}")
        
        # 데이터베이스 구조(컬럼) 조회
        database = notion.databases.retrieve(database_id=database_id)
        print(f"\n데이터베이스 이름: {database['title'][0]['plain_text']}")
        print("\n컬럼 목록:")
        for prop_name, prop_info in database['properties'].items():
            print(f"- {prop_name} ({prop_info['type']})")
        
        # 데이터베이스 내용(rows) 조회
        rows = notion.databases.query(database_id=database_id)
        
        print("\n=== 데이터베이스 내용 ===")
        for row in rows["results"]:
            print("\n--- 새로운 행 ---")
            for prop_name, prop_value in row["properties"].items():
                value = None
                
                # 속성 타입에 따라 값 추출
                if prop_value["type"] == "title":
                    value = prop_value["title"][0]["plain_text"] if prop_value["title"] else ""
                elif prop_value["type"] == "rich_text":
                    value = prop_value["rich_text"][0]["plain_text"] if prop_value["rich_text"] else ""
                elif prop_value["type"] == "number":
                    value = prop_value["number"]
                elif prop_value["type"] == "select":
                    value = prop_value["select"]["name"] if prop_value["select"] else ""
                elif prop_value["type"] == "multi_select":
                    value = [item["name"] for item in prop_value["multi_select"]]
                elif prop_value["type"] == "date":
                    if prop_value["date"]:
                        start = prop_value["date"]["start"]
                        end = prop_value["date"].get("end", "")
                        value = f"{start} ~ {end}" if end else start
                elif prop_value["type"] == "email":
                    value = prop_value["email"]
                elif prop_value["type"] == "phone_number":
                    value = prop_value["phone_number"]
                elif prop_value["type"] == "checkbox":
                    value = prop_value["checkbox"]
                
                print(f"{prop_name}: {value}")
    