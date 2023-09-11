import os.path
import yaml


current_dir = os.path.dirname(os.path.realpath(__file__))
yaml_file = os.path.join(current_dir, 'test.yaml')

try:
    with open(yaml_file, "r") as f:
        # yaml_file1 =f.read()
        CONF = yaml.safe_load(f)
except Exception as e:
    raise e


# 定义用例所需的变量
URL = CONF.get("url", {})
ADMIN = CONF.get("admin", {})
COOKIE_URL = URL.get("cookie", None)
GET_URL = URL.get("get",None)
POST_URL = URL.get("post",None)
PUT_URL = URL.get("put",None)
DELETE_URL = URL.get("delete",None)
ADMIN_USERNAME = ADMIN.get("username", None)
ADMIN_PASSWD = ADMIN.get("password", None)