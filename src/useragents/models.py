from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.db import models


class UserAgentDevice(models.Model):
    key = models.CharField(
        verbose_name=_('Key'),
        max_length=255,
        blank=True,
        null=True,
        unique=True,
        db_index=True,
    )
    user = models.ForeignKey(
        verbose_name=_('User'),
        to=get_user_model(),
        on_delete=models.SET_NULL,
        related_name='uad',
        db_index=True,
        blank=True,
        null=True,
    )
    user_agent_is_mobile = models.IntegerField(
        verbose_name=_('Mobile'),
        blank=True,
        null=True,
        choices=(
            (0, 'No'),
            (1, 'Yes'),
        ),
    )
    user_agent_is_tablet = models.IntegerField(
        verbose_name=_('Tablet'),
        blank=True,
        null=True,
        choices=(
            (0, 'No'),
            (1, 'Yes'),
        ),
    )
    user_agent_is_touch_capable = models.IntegerField(
        verbose_name=_('TouchCapable'),
        blank=True,
        null=True,
        choices=(
            (0, 'No'),
            (1, 'Yes'),
        ),
    )
    user_agent_is_pc = models.IntegerField(
        verbose_name=_('PC'),
        blank=True,
        null=True,
        choices=(
            (0, 'No'),
            (1, 'Yes'),
        ),
    )
    user_agent_is_bot = models.IntegerField(
        verbose_name=_('Bot'),
        blank=True,
        null=True,
        choices=(
            (0, 'No'),
            (1, 'Yes'),
        ),
    )
    user_agent_browser_family = models.CharField(
        verbose_name=_('BrowserFamily'),
        blank=True,
        null=True,
        max_length=255,
    )
    user_agent_browser_version = models.CharField(
        verbose_name=_('BrowserVersion'),
        blank=True,
        null=True,
        max_length=255,
    )
    user_agent_os_family = models.CharField(
        verbose_name=_('OSFamily'),
        blank=True,
        null=True,
        max_length=255,
    )
    user_agent_os_version = models.CharField(
        verbose_name=_('OSVersion'),
        blank=True,
        null=True,
        max_length=255,
    )
    user_agent_device_family = models.CharField(
        verbose_name=_('DeviceFamily'),
        blank=True,
        null=True,
        max_length=255,
    )
    user_agent_device_brand = models.CharField(
        verbose_name=_('DeviceBrand'),
        blank=True,
        null=True,
        max_length=255,
    )
    user_agent_device_model = models.CharField(
        verbose_name=_('DeviceModel'),
        blank=True,
        null=True,
        max_length=255,
    )
    ip = models.CharField(
        verbose_name=_('IP'),
        max_length=255,
        blank=True,
        null=True,
    )
    created_dt = models.DateTimeField(
        verbose_name=_('Created Datetime'),
        auto_now_add=True,
        db_index=True,
    )

    def __str__(self):
        return f'{self.key}'

    class Meta:
        verbose_name = _('UserAgentDevice')
        verbose_name_plural = _('UserAgentDevices')
