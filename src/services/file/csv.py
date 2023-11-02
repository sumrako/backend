from .abstract_file import FileDataService
import pandas as pd
from schemas.web_log import WebLogQuery, WebLogResponse
from pydantic import BaseModel
from datetime import datetime
import re

class LogService(FileDataService):
    def get_data(self, query: WebLogQuery):
        df = pd.read_csv(self.file_path)

        ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'

        df = df[df['IP'].str.match(ip_pattern, na=False)]
        df['Time'] = df['Time'].apply(lambda x: pd.to_datetime(x[1:], format='%d/%b/%Y:%H:%M:%S'))
        df[['Type', 'URL', 'Protocol']] = df['URL'].str.split(' ', expand=True)

        if query.url is not None:
             df = df.loc[df['URL'] == query.url]
        if query.ips is not None:
             df = df.loc[df['IP'].isin(query.ips)]
        if query.request_types is not None:
             df = df.loc[df['Type'].isin(query.request_types)]
        if query.protocols is not None:
             df = df.loc[df['Protocol'].isin(query.protocols)]
        if query.status_codes is not None:
             df = df.loc[df['Staus'].isin(query.status_codes)]
        if query.start_date is not None:
             df = df.loc[df['Time'] >= query.start_date]
        if query.end_date is not None:
             df = df.loc[df['Time'] < query.end_date]

        response_list = [WebLogResponse(ip=row['IP'], \
                                        time=row['Time'], \
                                        request_type=row['Type'], \
                                        request_url=row['URL'], \
                                        request_protocol=row['Protocol'], \
                                        status_code=row['Staus']).to_dict() for _, row in df.iterrows()]
        return response_list 