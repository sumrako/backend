from fastapi import APIRouter, status, Query, Request
from schemas.web_log import WebLogQuery, WebLogResponse
from services.file.csv import LogService
from typing import List
from config import settings
from datetime import date
from typing import Optional, List, Annotated
from ipaddress import IPv4Address
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
log_router = APIRouter()
templates = Jinja2Templates(directory="../templates")

@log_router.get("/log", status_code=status.HTTP_200_OK)
async def get_log_data(request: Request,
        ips: List[str] = Query(default=None), 
        status_codes: List[str] = Query(default=None),
        request_types: List[str] = Query(default=None),
        protocols: List[str] = Query(default=None),
        start_date: Optional[date] = None,
        end_date: Optional[date] = None,
        url: Optional[str] = None):
    log_query = WebLogQuery(ips=ips, start_date=start_date,
                            end_date=end_date, status_codes=status_codes,
                            request_types=request_types, url=url, protocols=protocols)
    csv_service = LogService(settings.log_file)
    data = csv_service.get_data(log_query)
    return templates.TemplateResponse("main_template.html", {'request': request, 'data': data})

# @log_router.get("/log", response_model=HTMLResponse)
# async def get_log_data(ips: List[str] = Query(default=None), 
#         status_codes: List[str] = Query(default=None),
#         request_types: List[str] = Query(default=None),
#         protocols: List[str] = Query(default=None),
#         start_date: Optional[date] = None,
#         end_date: Optional[date] = None,
#         url: Optional[str] = None):
#     log_query = WebLogQuery(ips=ips, start_date=start_date,
#                             end_date=end_date, status_codes=status_codes,
#                             request_types=request_types, url=url, protocols=protocols)
#     csv_service = LogService(settings.log_file)
#     return templates.TemplateResponse("main_template.html", {'data': csv_service.get_data})
