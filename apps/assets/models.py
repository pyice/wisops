from django.db import models

# Create your models here.


class ServerInfo(models.Model):
    system_choices = (
        ('ubuntu', 'ubuntu'),
        ('centos7', 'centos7')
    )
    hostname = models.CharField(max_length=64, null=True, blank=True,
                                verbose_name="主机名")
    manage_ip = models.GenericIPAddressField(null=True, blank=True,
                                      verbose_name="管理IP")
    usage = models.CharField(max_length=64, null=True, blank=True,
                             verbose_name="用途")
    system = models.CharField(max_length=64, choices=system_choices,
                              default="cenots7", verbose_name="操作系统类型")
    cpu = models.IntegerField(null=True, blank=True, verbose_name="cpu个数")
    mem = models.CharField(max_length=32, null=True, blank=True,
                           verbose_name="内存")
    disk_total = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name=('是否启用'))
    add_time = models.DateTimeField(auto_now_add=True, null=True,
                                 verbose_name='创建时间', blank=True)
    update_time = models.DateTimeField(auto_now=True, null=True,
                                  verbose_name='更新时间', blank=True)

    class Meta:
        db_table = 'wisops_server_info_t'
        verbose_name = '服务器资产表'
        verbose_name_plural = '服务器资产表'

