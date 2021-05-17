# -*- coding: utf-8 -*-

import requests
import base64
import json
import rsa

APP_ID = 'ohMVKNBQ3kfPvbFg'


class HesaiOAAuth():
    _name = 'hs.oa.auth'
    _description = 'Hesai OA Auth'

    def get_oa_address_app_id(self):
        app_id = ''
        address_url = ''
        hs_oa_env = self.env['ir.config_parameter'].get_param('hs_oa_env')
        if hs_oa_env:
            ref_str = "hesai_oa.hs_oa_api_host_" + hs_oa_env
            host_settings = self.sudo().env.ref("hesai_oa.hs_oa_api_host_" + hs_oa_env)
            address_url = host_settings.value
            app_id_ins = self.sudo().env.ref("hesai_oa.hs_oa_app_id_" + hs_oa_env)
            app_id = app_id_ins.value

        return app_id, address_url

    def oa_regist(self):
        """
        调用ecology注册接口,根据appid进行注册,将返回服务端公钥和Secret信息
        """
        # 获取address,appid
        app_id, address_url = self.get_oa_address_app_id()
        if not address_url:
            return {"success": False, "error": u"OA环境/HOST配置错误"}
        if not app_id:
            return {"success": False, "error": u"OA App_ID未配置"}
        # 获取接口
        api_ins = self.sudo().env.ref("hesai_oa.hs_oa_api_auth_regist")
        if not (api_ins and api_ins.value):
            return {"success": False, "error": u"ecology注册接口未配置"}
        # 调用ecology注册接口
        (pubkey, privkey) = rsa.newkeys(1024, poolsize=8)  # 使用多进程加速生成
        pubkeybase64 = base64.b64encode(pubkey.save_pkcs1())
        HEADERS = {'appid': app_id, 'cpk': pubkeybase64}
        r = requests.post(address_url + api_ins.value, json={}, headers=HEADERS)
        ret = json.loads(r.text)

        return {"success": True, "data": ret}

    def oa_get_token(self):
        """
        调用ecology接口,根据注册系统返回信息进行获取token信息
        """
        regist_res = self.oa_regist()
        if not regist_res.get('success'):
            return regist_res
        regist_data = regist_res.get('data', {})
        pub_key = self.strkey(regist_data.get('spk'))
        sec = rsa.encrypt(regist_data.get('secrit').encode('utf-8'), pub_key)
        # 获取url
        app_id, address_url = self.get_oa_address_app_id()
        api_ins = self.sudo().env.ref("hesai_oa.hs_oa_api_auth_applytoken")
        if not (api_ins and api_ins.value):
            return {"success": False, "error": u"ecology获取token接口未配置"}
        # 请求获取token
        HEADERS = {'appid': app_id, 'secret': base64.b64encode(sec)}
        r = requests.post(address_url + api_ins.value, json={}, headers=HEADERS)
        ret = json.loads(r.text)
        if ret.get('status') and ret.get('code') == 0:
            token_ins = self.sudo().env.ref("hesai_oa.hs_oa_setting_token")
            token_ins.write({'value': ret.get('token')})

        return ret

    def strkey(self, strk):
        b_str = base64.b64decode(strk)

        if len(b_str) < 162:
            return False

        hex_str = ''

        # 按位转换成16进制
        for x in b_str:
            h = hex(ord(x))[2:]
            h = h.rjust(2, '0')
            hex_str += h

        # 找到模数和指数的开头结束位置
        m_start = 29 * 2
        e_start = 159 * 2
        m_len = 128 * 2
        e_len = 3 * 2

        modulus = hex_str[m_start:m_start + m_len]
        exponent = hex_str[e_start:e_start + e_len]
        modulus = int(modulus, 16)
        exponent = int(exponent, 16)
        pub_key = rsa.PublicKey(modulus, exponent)

        return pub_key

    def decrypt(self, pri, ciphertext):
    key = RSA.importKey(pri)
    dsize = SHA.digest_size
    input_text = ciphertext[:256]
    ret = ''
    while input_text:
        sentinel = Random.new().read(15 + dsize)
        cipher = PKCS1_v1_5.new(key)
        _message = cipher.decrypt(input_text, sentinel)
        # ret += _message[:-dsize]
        ret += _message
        ciphertext = ciphertext[256:]
        input_text = ciphertext[:256]
    return ret

s = HesaiOAAuth()
print(s.strkey("MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCAbZETaIipqH7puERgJ6VVkBGKOCK+JOfr7+A+VfobRLGeXVkuCRzFj0RhlqlODzCjEff6rm0WDrcfAM6BxfjCciCKx2EXqjklfgZyY/gGf8PYfVmPG55k37edba4MpG+R1fcMtsB5qRHTpEVfoVBlr8ys1VhA/7dv+JLwg5B+FQIDAQAB"))
