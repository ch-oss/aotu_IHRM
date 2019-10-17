# 人力资源类
import time
class Ihrm:

    # 连接登陆接口,并返回响应体
    def login_ihrm(self, session):
        login_data = \
            {"mobile": "13800000002", "password": "123456"}
        return session.post \
            (url="http://182.92.81.159/api/sys/login", json=login_data)

    # 新增员工接口,返回响应体
    def add_emp(self, session):
        # time_str = time.strftime("%H%M%%s")
        self.login_ihrm(session)
        add_data = {
                    "username": "tof",
                    "mobile": "17666666667",
                    "timeOfEntry": "2019-07-01",
                    "formOfEmployment": 1,
                    "workNumber": "1322131",
                    "departmentName": "开发部",
                    "departmentId": "1066240656856453120",
                    "correctionTime": "2019-11-30"}
        return session.post(url="http://182.92.81.159/api/sys/user",json=add_data)

    #查询员工
    def query_emp(self,session):
        #登录
        self.login_ihrm(session)
        #新增员工
        reponse_emp = self.add_emp(session)
        #提取出新增员工的id
        self.emp_id = reponse_emp.json().get("data").get("id")
        print("emp_id:",self.emp_id)
        #根据新增员工返回的员工id来查询新增员工的信息是否正确
        return session.get(url="http://182.92.81.159/api/sys/user/"+str(self.emp_id))

    #更新员工信息
    def put_emp(self,session):

        #登录
        self.login_ihrm(session)

        #更新信息
        new_emp_data = {"username":"tom-new"}
        return session.put(url="http://182.92.81.159/api/sys/user/"+str(self.emp_id),json=new_emp_data)

    #删除员工信息
    def del_emp(self,session):
        #登录
        self.login_ihrm(session)

        #删除员工信息
        return session.delete(url="http://182.92.81.159/api/sys/user/"+str(self.emp_id))


