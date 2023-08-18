# routing.py
from django.urls import re_path

from . import consumer

websocket_urlpatterns = [
    re_path(r'ws/stock_updates/$', consumer.home.as_asgi()),
    re_path(r'ws/stock_updates/expiry$', consumer.start.as_asgi()),
    re_path(r'ws/stock_updates/NIFTY1$', consumer.NIFTY1.as_asgi()),
    re_path(r'ws/stock_updates/NIFTY2$', consumer.NIFTY2.as_asgi()),
    re_path(r'ws/stock_updates/BANKNIFTY1$', consumer.BANKNIFTY1.as_asgi()),
    re_path(r'ws/stock_updates/BANKNIFTY2$', consumer.BANKNIFTY2.as_asgi()),
    re_path(r'ws/stock_updates/FINNIFTY1$', consumer.FINNIFTY1.as_asgi()),
    re_path(r'ws/stock_updates/FINNIFTY2$', consumer.FINNIFTY2.as_asgi()),
    re_path(r'ws/stock_updates/MIDCPNIFTY1$', consumer.MIDCPNIFTY1.as_asgi()),
    re_path(r'ws/stock_updates/MIDCPNIFTY2$', consumer.MIDCPNIFTY2.as_asgi()),
    re_path(r'ws/stock_updates/CRUDEOIL1$', consumer.CRUDEOIL1.as_asgi()),
    re_path(r'ws/stock_updates/CRUDEOIL2$', consumer.CRUDEOIL2.as_asgi()),
    re_path(r'ws/stock_updates/NATURALGAS1$', consumer.NATURALGAS1.as_asgi()),
    re_path(r'ws/stock_updates/NATURALGAS2$', consumer.NATURALGAS2.as_asgi()),
]
