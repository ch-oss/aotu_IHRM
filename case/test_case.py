
import unittest
import requests

from api.test_ihrm import Ihrm
num = None


class TestIhrm(unittest.TestCase):

    #获取session对象和Ihrm对象
    @classmethod
    def setUpClass(cls) -> None:
        cls.session = requests.Session()
        cls.my_ihrm = Ihrm()
        cls.my_id = None



    #定义方法级别的teardown,关闭session对象
    def tearDown(self) -> None:
        self.session.close()

    #测试登录接口
    def test_01_login(self):
        #获取返回响应数据
        reponse1 = self.my_ihrm.login_ihrm(self.session)
        print("登录成功返回的数据:",reponse1.text)
        #根据响应数据进行断言
        self.assertEqual(10000,reponse1.json().get("code"))

    #测试新增员工接口
    def test_02_add_emp(self):
        #获取返回的响应数据
        reponse2 = self.my_ihrm.add_emp(self.session)

        num = reponse2.json().get("data").get("id")
        print("新增员工成功后返回的员工id:", num)


        #根据返回的响应做断言
        self.assertEqual(10000, reponse2.json().get("code"))

    #测试查询接口
    def test_03_query_new_emp(self):
        print("查询接口测试中")
        reponse3 = self.my_ihrm.query_emp(self.session)
        print("查询接口返回的数据:",reponse3.json())

        #断言
        self.assertIn("操作",reponse3.json().get("message"))

     #更员工信息
    def test_04_put_emp(self):
        reponse4 = self.my_ihrm.put_emp(self.session)
        print("更新员工返回的数据:",reponse4.text)
        #断言
        self.assertIn("操作", reponse4.json().get("message"))

    #删除员工信息
    def test_05_delete_emp_info(self):
        reponse5 = self.my_ihrm.del_emp(self.session)
        # 断言
        self.assertIn("操作", reponse5.json().get("message"))