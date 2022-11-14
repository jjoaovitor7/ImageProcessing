from masonite.views import View
from masonite.controllers import Controller
from masonite.request import Request
import base64
from io import BytesIO
import numpy as np
import cv2
import matplotlib.pyplot as plt


def get_image():
    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    return base64.b64encode(buffer.getbuffer()).decode("ascii")


class IndexController(Controller):
    def show(self, request: Request, view: View):
        if ("file_upload" in request.all()):
            img = request.input("file_upload").stream()
            img = np.frombuffer(img, np.uint8)
            img = cv2.imdecode(img, 1)

            type = int(request.input("type"))
            if (type == 1):
                return view.render("index", {
                    "data": img
                })

            if (type == 2):
                img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                plt.imshow(img, cmap="gray")
                return view.render("index", {
                    "data": f"<img src='data:image/png;base64,{get_image()}' />"
                })

            if (type == 3):
                img = -1 * img * 255
                plt.imshow(img)
                return view.render("index", {
                    "data": f"<img src='data:image/png;base64,{get_image()}' />"
                })
        else:
            return view.render("index")
