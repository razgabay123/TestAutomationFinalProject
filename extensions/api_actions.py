import allure
import requests
from utilities.common_ops import get_data


headers = {
	"x-api-key": "reqres-free-v1"
}


class API_Actions:
	@staticmethod
	@allure.step("get API data")
	def get(data):
		response = requests.get(f"{get_data('API_URL')}users{data}", headers=headers)
		return response
	
	@staticmethod
	@allure.step("create API data")
	def post(data):
		response = requests.post(f"{get_data('API_URL')}users", f"{data}", headers=headers)
		return response
	
	@staticmethod
	@allure.step("register a user")
	def register(data):
		response = requests.post(f"{get_data('API_URL')}register", f"{data}", headers=headers)
		return response
	
	@staticmethod
	@allure.step("update API data")
	def put(id, data):
		response = requests.put(f"{get_data('API_URL')}users/{id}", f"{data}", headers=headers)
		return response
	
	@staticmethod
	@allure.step("delete API data")
	def delete(data):
		response = requests.delete(f"{get_data('API_URL')}users{data}", headers=headers)
		return response
	