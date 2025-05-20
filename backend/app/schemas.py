from pydantic import BaseModel

class ChartResponse(BaseModel):
    chart_html: str