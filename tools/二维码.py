import qrcode
from PIL import Image #二维码美化
# 生成二维码数据
data = "http://colagold.top"

# 创建二维码对象
qr = qrcode.QRCode(version=1, box_size=10, border=4)

# 添加数据到二维码对象
qr.add_data(data)
qr.make(fit=True)

# 创建二维码图片
img = qr.make_image(fill_color="black", back_color="white")

# 保存二维码图片
img.save("博客.png")

# 打开背景图像
background_img = Image.open("background1.jpg")

# 调整背景图像大小以适应二维码
background_img = background_img.resize(img.size)

# 将背景图像粘贴到二维码上
result = Image.new("RGB", (img.size[0], img.size[1]))
result.paste(background_img, (0, 0))
result.paste(img, (0, 0), mask=img)

# 保存美化后的二维码图片
result.save("styled_qrcode.png")