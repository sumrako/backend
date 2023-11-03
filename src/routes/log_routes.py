from fastapi import APIRouter, status, Query, Request
from schemas.web_log import WebLogQuery
from typing import List
from config import settings
from datetime import date
from typing import Optional, List
from fastapi.templating import Jinja2Templates
from managers.data_managers import CSVDataManger
from services.log_service import CSVLogService

log_router = APIRouter()
templates = Jinja2Templates(directory="templates")

@log_router.get("/logs", status_code=status.HTTP_200_OK)
async def get_log_data(request: Request,
        ips: List[str] = Query(default=None), 
        status_codes: List[str] = Query(default=None),
        request_types: List[str] = Query(default=None),
        protocols: List[str] = Query(default=None),
        start_date: Optional[date] = None,
        end_date: Optional[date] = None,
        url: Optional[str] = None,
        limit: int = 17000,
        offset: int = 0):
    log_query = WebLogQuery(ips=ips, 
                            start_date=start_date,
                            end_date=end_date, 
                            status_codes=status_codes,
                            request_types=request_types, 
                            url=url, 
                            protocols=protocols,
                            limit=limit,
                            offset=offset)
    data_manager = CSVDataManger(settings.log_file)
    log_service = CSVLogService(data_manager)
    data = log_service.get_data(log_query)
    return templates.TemplateResponse("main_template.html", {'request': request, 'data': data})
