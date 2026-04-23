#problem87
import logging

user_input = input("please input your name:")
print(user_input)

#problem88
from pprint import pprint
lst = [
    {"id":"0001","name":"admin"},
    {"id":"0002","name":"guest"},
    {"id":"0003","name":"test"},
]

print(lst)
pprint(lst)

#problem89
from tkinter.messagebox import showinfo
from tkinter.messagebox import askyesno
showinfo("Title","Message")
askyesno("Title","Message")

#problem90
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)
logger.info("hello world")
logger.error("hello world")
