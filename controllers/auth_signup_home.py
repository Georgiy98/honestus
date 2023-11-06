from odoo.addons.auth_signup.controllers.main import AuthSignupHome
from odoo.addons.web.controllers.home import SIGN_UP_REQUEST_PARAMS

SIGN_UP_REQUEST_PARAMS.add('mobile')


class AuthSignupHomeWithMobile(AuthSignupHome):
    def _prepare_signup_values(self, qcontext):
        res = AuthSignupHome._prepare_signup_values(self, qcontext)
        res['mobile'] = qcontext.get('mobile')
        return res
