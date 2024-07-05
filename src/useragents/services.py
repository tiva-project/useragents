from django.utils.deprecation import MiddlewareMixin

from .models import UserAgentDevice


class UserAgentDeviceMiddleware(MiddlewareMixin):

    def process_request(self, request):
        uad_schema = self.user_agent_device_id(request)
        setattr(request, 'uad', uad_schema)

    def process_response(self, request, response):
        self.process_request(request)

        response.set_cookie(
            key='UAD',
            value=request.uad.key,
            max_age=60 * 60 * 24 * 365,
            httponly=False,
            secure=False
        )
        return response

    def user_agent_device(self, request):

        cookie_name = 'UAD'
        if not hasattr(request, 'COOKIES'):
            return None

        adk = request.COOKIES.get(cookie_name)

        try:
            obj = UserAgentDevice.objects.get(key=adk)
            self.uad_schema = obj
            return self.uad_schema

        except UserAgentDevice.DoesNotExist:
            self.uad_schema = request
            obj, _ = UserAgentDevice.objects.get_or_create(
                **self.uad_schema.model_dump()
            )
            self.uad_schema = obj
            return self.uad_schema
        except Exception as exc:
            raise exc.args[0]

    _uad_schema = None

    @property
    def uad_schema(self):
        return self._uad_schema

    @uad_schema.setter
    def uad_schema(self, request):
        from .schemas import UADSchema

        self._uad_schema = UADSchema(request)
