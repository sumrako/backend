from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional, List
from ipaddress import IPv4Address

class WebLogQuery(BaseModel):
    ips: Optional[List[str]]
    start_date: Optional[datetime]
    end_date: Optional[datetime]
    status_codes: Optional[List[str]]
    request_types: Optional[List[str]]
    url: Optional[str]
    protocols: Optional[List[str]]
    limit: int
    offset: int


class WebLogResponse(BaseModel):
    ip: IPv4Address
    time: datetime
    request_type: str
    request_url: str
    request_protocol: str
    status_code: int

    def to_dict(self):
        return {
            'ip': str(self.ip),
            'time': self.time.isoformat(),
            'request_type': self.request_type,
            'request_url': self.request_url,
            'request_protocol': self.request_protocol,
            'status_code': self.status_code
        }
