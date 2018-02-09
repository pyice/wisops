# -*- coding:utf-8 -*-
from .models import ServerInfo

import xadmin


class ServerInfoAdmin(object):
    list_display = ["hostname", "manage_ip"]


xadmin.site.register(ServerInfo, ServerInfoAdmin)
