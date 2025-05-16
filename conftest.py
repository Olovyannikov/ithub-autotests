import pytest
import subprocess
import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

BASE_URL = os.getenv("BASE_URL", "http://localhost:8081")
TIMEOUT = 10


@pytest.fixture(scope="session", autouse=True)
def start_docker():
    print("🚀 Запуск docker compose...")
    env = os.environ.copy()
    env["OPENCART_PORT"] = "8081"
    env["PHPADMIN_PORT"] = "8888"
    env["OPENCART_HOST"] = "localhost"

    subprocess.run(["docker", "compose", "up", "-d"], env=env, check=True)

    # Ждём, пока OpenCart поднимется (можно сделать проверку HTTP)
    time.sleep(15)  # желательно заменить на реальную проверку доступности URL
    yield
    print("🛑 Остановка docker compose...")
    subprocess.run(["docker", "compose", "down"], env=env)


@pytest.fixture(scope="function")
def browser():
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(BASE_URL)
    yield driver
    driver.quit()